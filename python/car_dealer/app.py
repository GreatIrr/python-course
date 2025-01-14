from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///car_dealer.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# Models
class Dealer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)


class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(100), nullable=False)
    color = db.Column(db.String(50), nullable=False)
    dealer_id = db.Column(db.Integer, db.ForeignKey('dealer.id'), nullable=False)


# Routes
@app.route('/dealers', methods=['POST', 'GET', 'DELETE'])
def handle_dealers():
    if request.method == 'POST':
        data = request.get_json()
        name = data.get('name')
        location = data.get('location')
        if not name or not location:
            return jsonify({'error': 'Name and location are required'}), 400
        dealer = Dealer(name=name, location=location)
        db.session.add(dealer)
        db.session.commit()
        return jsonify({'message': 'Dealer added',
                        'dealer': {'id': dealer.id, 'name': dealer.name, 'location': dealer.location}}), 201

    if request.method == 'GET':
        dealers = Dealer.query.all()
        return jsonify({'dealers': [{'id': d.id, 'name': d.name, 'location': d.location} for d in dealers]}), 200

    if request.method == 'DELETE':
        data = request.get_json()
        dealer_id = data.get('id')
        if not dealer_id:
            return jsonify({'error': 'Dealer ID is required'}), 400
        dealer = Dealer.query.get(dealer_id)
        if not dealer:
            return jsonify({'error': 'Dealer not found'}), 404
        db.session.delete(dealer)
        db.session.commit()
        return jsonify({'message': 'Dealer deleted'}), 200


@app.route('/cars', methods=['POST', 'GET', 'DELETE'])
def handle_cars():
    if request.method == 'POST':
        data = request.get_json()
        model = data.get('model')
        color = data.get('color')
        dealer_id = data.get('dealer_id')
        if not model or not color or not dealer_id:
            return jsonify({'error': 'Model, color, and dealer_id are required'}), 400
        if not Dealer.query.get(dealer_id):
            return jsonify({'error': 'Dealer not found'}), 404
        car = Car(model=model, color=color, dealer_id=dealer_id)
        db.session.add(car)
        db.session.commit()
        return jsonify({'message': 'Car added',
                        'car': {'id': car.id, 'model': car.model, 'color': car.color, 'dealer_id': car.dealer_id}}), 201

    if request.method == 'GET':
        dealer_id = request.args.get('dealer_id')
        model = request.args.get('model')
        color = request.args.get('color')

        query = Car.query

        if dealer_id:
            query = query.filter_by(dealer_id=dealer_id)
        if model:
            query = query.filter_by(model=model)
        if color:
            query = query.filter_by(color=color)

        cars = query.all()
        return jsonify(
            {'cars': [{'id': c.id, 'model': c.model, 'color': c.color, 'dealer_id': c.dealer_id} for c in cars]}), 200

    if request.method == 'DELETE':
        data = request.get_json()
        car_id = data.get('id')
        if not car_id:
            return jsonify({'error': 'Car ID is required'}), 400
        car = Car.query.get(car_id)
        if not car:
            return jsonify({'error': 'Car not found'}), 404
        db.session.delete(car)
        db.session.commit()
        return jsonify({'message': 'Car deleted'}), 200


if __name__ == '__main__':
    if not os.path.exists('car_dealer.db'):
        with app.app_context():  # Ensure the application context is pushed
            db.create_all()
    app.run(host='0.0.0.0', port=5000)


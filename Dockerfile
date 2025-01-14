# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install Pipenv
RUN pip install pipenv

# Copy Pipfile and Pipfile.lock (if available) to the container
COPY Pipfile Pipfile.lock ./

# Install dependencies using Pipenv
RUN pipenv install --system --deploy

# Copy the application code into the container
COPY . .

# Expose the port that the app will run on
EXPOSE 5000

# Command to run the application
CMD ["python", "python/car_dealer/app.py"]

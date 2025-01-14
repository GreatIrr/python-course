# Python Syntax
import random

x = 5
y = "Hello, World!"

# This is a comment.
print("Hello, World!")

print(f'x = ', x)

# Python Comments

# This is a comment
print("Hello, World1!")
print("Hello, World2!")  # This is a comment

# print("Hello, World!")
print("Cheers, Mate!")

"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")

# Python Variables

q = 5
w = "John"
print(q)
print(w)

e = 4  # x is of type int
e = "Sally"  # x is now of type str
print(e)

a = str(3)  # x will be '3'
s = int(3)  # y will be 3
d = float(3)  # z will be 3.0

print(a)
print(s)
print(d)

z = 5
zz = "John"
print(type(z))
print(type(zz))

g = 4
G = "Sally"
print(g)
print(G)
# A will not overwrite a

xx, yy, zz = "Orange", "Banana", "Cherry"
print(xx)
print(yy)
print(zz)

xxx = yyy = zzz = "Orange"
print(xxx)
print(yyy)
print(zzz)

fruits = ["apple", "banana", "cherry"]
x1, y1, z1 = fruits
print(x1)
print(y1)
print(z1)

x2 = "awesome"


def myfunc():
    print("Python is " + x2)


myfunc()


def myfuncky():
    global pp
    pp = "fantastic"
    print("Python is " + pp)


myfuncky()

print("Python is " + pp)
x4 = "awesome"


def myfunc4():
    global x4
    x4 = "blablabla"


myfunc4()

print("Python is " + x4)

# data types

llist = ["apple", "banana", "cherry"]
print(llist)
ttuple = ("apple", "banana", "cherry")
print(ttuple)
rrange = range(6)
for i in rrange:
    print(i)
print(rrange)
ddict = {"name": "John", "age": 36}
print(ddict)
print(ddict.get('name'))
print(ddict.get('age'))
sset = {"apple", "banana", "cherry"}
print(sset)
ffrozenset = frozenset({"apple", "banana", "cherry"})
print(ffrozenset)

# numbers

xn = 1  # int
yn = 2.8  # float
zn = 1j  # complex

# convert from int to float:
an = float(xn)

# convert from float to int:
bn = int(yn)

# convert from int to complex:
cn = complex(xn)

print(an)
print(bn)
print(cn)

print(random.randrange(1, 10))

# strings

astr = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""  # or ''' fjfjfjfj '''
print(astr)

bstr = "Hello, World!"
print(bstr[2:5])
print(bstr[:5])
print(bstr[2:])

print(bstr[-5:-2])

age = 36
txt = "My name is John, I am " + str(age)
print(txt)

txt1 = f"My name is not John, I am not {age}"
print(txt1)

price = 59
txt2 = f"The price is {price:.5f} dollars"
print(txt2)

txt3 = f"The price is {20 * 59} dollars"
print(txt3)

print(bool("Hello"))
print(bool(15))
print(bool(0))
print(bool("abc"))
print(bool(["apple", "cherry", "banana"]))
print(bool([]))
print(bool(()))

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))


class MyClass:
    def __len__(self):
        return 0


myobj1 = MyClass()
print(myobj1)
print(bool(myobj1))

x5 = 200
print(isinstance(x5, int))


print(7 // 3)
print(round(7.254626, 3))
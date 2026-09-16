import math

def greetings(uname="Guest"):
    print("Hello,",uname)
greetings("Akhil")
greetings()


def dosum(a,b):
    return a+b
summ=dosum(4,5)
print(summ)


def domul(a,b):
    return a*b
print(domul(4,5))
print(domul("h",5))


def circle(radius):
    area= math.pi * (radius ** 2)
    circumference= 2 * math.pi * radius
    return area, circumference

area,circumference=circle(7)
print(round(area,2),round(circumference,2))


# Lambda function
cube= lambda x:x**3
print(cube(3))


# *args-> takes any number of tuple arguments in a function
def sum_all(*args):
    return sum(args)

print(sum_all(1,2,3))
print(sum_all(1,2,3,4,5,6,7))


# **kwargs-> takes keyword arguments in a function
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print (f"{key}: {value}", end=", ")

print_kwargs(name="Akhil", roll_no="3")
print_kwargs(name="Akhil")
print_kwargs(name="Akhil", roll_no="3", city="Patiala")


# yield-> used in a function to return a generator object, which can be iterated over using a for loop or converted into a list using the list() function.
def my_generator(limit):
    for i in range(limit):
        yield i

for num in my_generator(5):
    print(num)


# recursive funtion
def factorial(n):
    if n==0 or n==1:
        return 1

    return n * factorial(n-1)
print(factorial(5))
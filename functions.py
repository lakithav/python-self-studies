"""
import math
import datetime

print(math.sqrt(100))
print(datetime.datetime.now())


def function1(arg1):
    print(arg1)

function1("Hello, World!")


def sum(num1, num2):
    print(num1 + num2)

sum(10, 20)


def rectangle(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

print(rectangle(5, 3))


#default parameters
def student(subject='Math',marks=70):
    print("Subject:", subject)
    print("Marks:", marks)
student("Science")

#positional arguments

def student(subject, marks):
    print("Subject:", subject)
    print("Marks:", marks)

student("Math", 80)
student(88,"Science") #This will cause an error because the arguments are not in the correct order.
"""
#keyword arguments

def student(subject, marks):
    print("Subject:", subject)
    print("Marks:", marks)

student(subject="Math", marks=80)

#variable length arguments

def total(*numbers):
    sum = 0
    for num in numbers:
        sum += num
    print("Total:", sum)

total(10, 20, 30)
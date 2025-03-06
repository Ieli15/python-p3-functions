#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

def greet(name):
    name = "Guido"
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    print("Hello, " + name + "!")

def add(num1, num2):
    num1 = 45
    num2 = 55
    return num1 + num2  

result = add(10, 20)  
print(result) 


def halve(number):
    return number / 2  

print(halve(100))  
print(halve(99))   


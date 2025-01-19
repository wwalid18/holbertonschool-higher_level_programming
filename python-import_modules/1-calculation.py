#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5
    print(f"{a} + {b} = {add(a, b)}\n{a} - {b} = {sub(a, b)}\n{a} * {b} = {mul(a, b)}\n{a} / {b} = {div(a, b)}")

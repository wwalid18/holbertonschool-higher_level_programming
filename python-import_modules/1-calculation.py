#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5
print(f"""
{a} + {b} = {add(a, b)}
{a} - {b} = {sub(a, b)}
{a} * {b} = {mul(a, b)}
{a} / {b} = {div(a, b)}
""")

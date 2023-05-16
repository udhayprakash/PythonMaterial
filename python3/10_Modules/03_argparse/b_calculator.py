#!/usr/bin/python
"""
Purpose: command-line calculator
"""
import argparse


def addition(n1, n2):
    return n1 + n2


def subtraction(s1, s2):
    return s1 - s2


def multiplication(m1, m2, m3):
    return m1 * m2 * m3


# Step 1: created parser object
parser = argparse.ArgumentParser(description="Script to add two/three numbers")

# Step 2: add arguments to parser object
parser.add_argument("-num1", help="First value", type=int, default=0)
parser.add_argument("-num2", help="Second Value", type=int, default=0)
parser.add_argument("-num3", help="optonal value", type=float, default=0.0)


# Step 3: Built parser objects and extract values
args = parser.parse_args()

num1 = args.num1
num2 = args.num2
print(f" {type(num1) =} {num1 = }")
print(f" {type(num2) =} {num2 = }")
print(f" {type(args.num3) =} {args.num3 = }")
print()

# Default Values are None for the args
print(f"{addition(num1, num2)                 =}")
print(f"{subtraction(num1, num2)              =}")
print(f"{multiplication(num1, num2,args.num3) =}")

# python b_calculator.py
# python b_calculator.py -num1 10
# python b_calculator.py -num1 10 -num2 20
# python b_calculator.py -num1 10 -num2 20 -num3 30

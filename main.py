#!/usr/bin/python3
import sys

def read_numbers_from_file(filename):
    with open(filename, 'r') as file:
        numbers = [int(line.strip()) for line in file]
    return numbers

def getFactors(number):
    p = 2
    while (number % p != 0):
        p += 1
    q = number // p
    return p, q

if __name__ == "__main__":
    filename = sys.argv[1]
    numbers = read_numbers_from_file(filename)
    for number in numbers:
        p, q = getFactors(number)
        print(f"{number} = {q} * {p}")
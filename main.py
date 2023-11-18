#!/usr/bin/python3
import sys

def read_numbers_from_file(filename):
    #check if file exists
    try:
        f = open(filename)
    except FileNotFoundError:
        print("File not found")
        sys.exit(1)
    #check if file is empty
    if f.readline() == "":
        print("File is empty")
        sys.exit(1)
    #read numbers from file
    with open(filename, "r") as f:
        numbers = []
        for line in f:
            numbers.append(int(line))
    return numbers

def getFactors(number):
    p = 2
    while (number % p != 0):
        p += 1
    q = number // p
    return p, q

if __name__ == "__main__":
    #check if filename is given
    if len(sys.argv) < 2:
        print("Usage: main.py <filename>")
        sys.exit(1)
    filename = sys.argv[1]
    numbers = read_numbers_from_file(filename)
    for number in numbers:
        p, q = getFactors(number)
        print(f"{number} = {q} * {p}")
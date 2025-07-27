
import numpy as np
from global_variables import *
##creating 1D array
def dim1():
    name = input("Give a name for the array: ")
    noElements = int(input("Enter number of elements: "))
    values = [int(x) for x in input(f"Enter values (space-separated): ").split()]
    if len(values) != noElements:
        print("Oops! Number of elements doesn't match. Try again.")

    else:
        Arry1 = np.array(values)
        arrays[name] = Arry1
        print(f"\n{name} = {Arry1}\n")

##creating 2D array
def dim2():
    name = input("Give a name for the array: ")
    rows2 = int(input("Number of rows: "))
    cols2 = int(input("Number of columns: "))
    values = []

    for i in range(rows2):
        while True:
            row = [int(x) for x in input(f"Enter row {i + 1} values (space-separated): ").split()]
            if len(row) != cols2:
                print("Oops! Number of elements doesn't match columns. Try again.")
            else:
                values.append(row)
                break

    Arry2 = np.array(values)
    arrays[name] = Arry2
    print(f"\n{name} =\n{Arry2}\n")

##creating 3D array
def dim3():
    name = input("Give a name for the array: ")
    blocks = int(input("Enter number of blocks: "))
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    values = []

    for i in range(blocks):
        block = []
        for j in range(rows):
            row = [int(x) for x in input(f"Enter {cols} values for Block {i+1}, Row {j+1} (space-separated): ").split()]
            while len(row) != cols:
                print(f" You must enter exactly {cols} values!")
                row = [int(x) for x in input(f"Re-enter values for Block {i+1}, Row {j+1}: ").split()]
            block.append(row)
        values.append(block)

    Array3 = np.array(values)
    arrays[name] = Array3
    print(f"\n{name} =\n{Array3}\n")

##creating 4D array
def dim4():
    name = input("Give a name for the 4D array: ")
    pages = int(input("Enter number of pages: "))
    blocks = int(input("Enter number of blocks per page: "))
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    values = []

    for p in range(pages):
        page = []
        for b in range(blocks):
            block = []
            for r in range(rows):
                row = [int(x) for x in input(f"Enter page no : {p+1}, block no : {b+1} values for Row {r+1}: ").split()]
                while len(row) != cols:
                    print(f" Please enter exactly {cols} values.")
                    row = [int(x) for x in input(f"Re-enter values for Row {r+1}: ").split()]
                block.append(row)
            page.append(block)
        values.append(page)

    Array4 = np.array(values)
    arrays[name] = Array4
    print(f"\n{name} =\n{Array4}\n")


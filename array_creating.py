
import numpy as np
from global_variables import *
##function regarding 1D arrays
def dim1():
    name1 = input("Give a name for the array: ")
    noElements = int(input("Enter number of elements: "))
    values = [int(x) for x in input(f"Enter values (space-separated): ").split()]
    Arry1 = np.array(values)
    arrays[name1] = Arry1
    print(f"\n{name1} = {Arry1}\n")

##function regarding 2D arrays
def dim2():
    name2 = input("Give a name for the array: ")
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
    arrays[name2] = Arry2
    print(f"\n{name2} =\n{Arry2}\n")
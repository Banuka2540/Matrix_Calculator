import numpy as np
from global_variables import *

def slice_arrays():
    getAr = input("to Slice 1D arrays press 1 and to add 2D arrays press 2 ")
    if getAr == "1":
        input_str1 = input(str("enter the name 1D array you want to Slice : "))
        if input_str1 in arrays:
            input_str3 = int(input("enter the starting index : "))
            input_str4 = int(input("enter the Ending index : "))
            input_str5 = int(input("enter the Step  : "))
            x = arrays[input_str1]
            y = x[input_str3:input_str4:input_str5]
            print(y)
    elif getAr == "2":
        input_str1 = input("Enter the name of the 2D array you want to slice: ")
        if input_str1 in arrays:
            try:
                row_start = int(input("Enter starting row index: "))
                row_end = int(input("Enter ending row index: "))
                col_start = int(input("Enter starting column index: "))
                col_end = int(input("Enter ending column index: "))
                x = arrays[input_str1]
                y = x[row_start:row_end, col_start:col_end]
                print("Sliced 2D array:\n", y)
            except Exception as e:
                print("Error during slicing:", e)
        else:
            print("Oops! No such array exists. Try again.")
    else:
        print("Invalid option. Press 1 or 2 only.")

def indexing_arrays():
    getAr = input("to index 1D arrays press 1 and to index 2D arrays press 2 ")
    if getAr == "1":
        input_str1 = input(str("enter the name 1D array you want to index : "))
        if input_str1 in arrays:
            input_str3 = int(input("enter the index : "))
            y = arrays[input_str1]
            print(y[input_str3])
        else:
            print("Oops! No such array exists. Try again.")
    elif getAr == "2":
        input_str1 = input(str("enter the name 2D array you want to Split : "))
        if input_str1 in arrays:
            input_str3 = int(input("enter the Row index : "))
            input_str4 = int(input("enter the Column index : "))
            y = arrays[input_str1]
            print(y[input_str3, input_str4])
        else:
            print("Oops! No such array exists. Try again.")

def filtering_arrays():
    getAr = input("To filter 1D arrays press 1, for 2D arrays press 2: ")
    if getAr in ["1", "2"]:
        input_str1 = input("Enter the array name to filter: ")
        if input_str1 in arrays:
            x = np.array(arrays[input_str1])
            condition = input("Enter filter condition using 'x' (e.g., x > 5): ")

            try:
                result = x[eval(condition)]
                print("Filtered Result:\n", result)
            except Exception as e:
                print("Error in condition:", e)
        else:
            print("Array not found.")
    else:
        print("Invalid option.")

#create try catch functions for this
import numpy as np
from global_variables import *


def reshape_arrays():
    nf = input("enter 2 to reshape 2D array : ")
    match int(nf):
        case "2":
            input_str1 = input("enter the name 2D array you want to reshape : ")
            if input_str1 in arrays:
                input_str2 = int(input("enter the no of rows you want to reshape : "))
                input_str3 = int(input("enter the no of columns you want to reshape : "))
                x = arrays[input_str1].reshape(input_str2, input_str3)
                print(x)
            else:
                print("Oops! No such array exists. Try again.")
        case _:
            print("Enter only 2 ")





def flattern_arrays():
        input_str1 = input(str("enter the name 2D array you want to flatten : "))
        if input_str1 in arrays:
            print(arrays[input_str1].flatten())
        else:
            print("Oops! No such array exists. Try again.")


def  transpose_arrays():
    input_str1 = input(str("enter the name 2D array you want to transpose : "))
    if input_str1 in arrays:
        print(np.transpose(arrays[input_str1]))
    else:
        print("Oops! No such array exists. Try again.")

def split_arrays():
    getAr = input("to split 1D arrays press 1 and to add 2D arrays press 2 ")
    if getAr == "1":
        input_str1 = input(str("enter the name 1D array you want to Split : "))
        if input_str1 in arrays:
            x = np.split(arrays[input_str1], 2 )
            #other numbers that cannot divide by 2?
            print(x)
        else:
            print("Oops! No such array exists. Try again.")
    elif getAr == "2":
        input_str1 = input(str("enter the name 2D array you want to Split : "))
        if input_str1 in arrays:
            np.split(arrays[input_str1], 2 )
        else:
            print("Oops! No such array exists. Try again.")
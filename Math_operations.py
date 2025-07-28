#create try catch functions (error handling)
import numpy as np
from global_variables import *
##1D Array adding
def oneDadd():
    try :
        print("--- only for 1D arrays ---")
        input_str1 = input(str("enter the first name of array you want to add : "))
        input_str2 = input(str("enter the second name of array you want to add : "))
        if arrays[input_str1].ndim !=1 or  arrays[input_str2].ndim !=1 :
            raise ValueError("Please enter only 1D arrays.")
        if arrays[input_str1].shape !=arrays[input_str2].shape :
            raise ValueError("Arrays must have the same shape.")
        print("added array : ", sum)
    except Exception as e:
        print(f"error {e}\n")

#array multiply
def arraymultiply():
    print("--- only for 1D arrays ---")
    try :
        input_str1 = input(str("enter the first name of array you want to multiply : "))
        input_str2 = input(str("enter the second name of array you want to multiply : "))
        if arrays[input_str1].ndim != 1 or arrays[input_str2].ndim != 1:
            raise ValueError("Please enter only 1D arrays.")
        if arrays[input_str1].shape != arrays[input_str2].shape:
            raise ValueError("Arrays must have the same shape.")
        multi = arrays[input_str1] * arrays[input_str2]
        print("multiplied array : " , multi)
    except:
        print("check the array names / array dimensions  again !! \n")

##Finding dotProduct
def dotproduct():
    try :
        getAr = input("for 1D arrays press 1 and for 2D arrays press 2 ")
        input_str1 = input(str("enter the first name of array you want to dot product : "))
        input_str2 = input(str("enter the second name of array you want to dot product : "))
        if getAr == "1":
            product = arrays[input_str1].dot(arrays[input_str2])
            print(product)
        elif getAr == "2":
            product = arrays[input_str1] @ (arrays[input_str2])
            print(product)
        else:
            print("Enter only 1 or 2 ")
    except:
        print("check the array names / array dimensions  again !! \n")


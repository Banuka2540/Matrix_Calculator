#create try catch functions (error handling)
import numpy as np
from global_variables import *
##1D Array adding
def oneDadd():
    input_str1 = input(str("enter the first name of array you want to add : "))
    input_str2 = input(str("enter the second name of array you want to add : "))
    sum = arrays[input_str1] + arrays[input_str2]
    print("added array : " , sum)

##2D Array adding
def twoDadd():
    input_str1 = input(str("enter the first name of array you want to multiply : "))
    input_str2 = input(str("enter the second name of array you want to multiply : "))
    multi = arrays[input_str1] * arrays[input_str2]
    print(multi)

##Finding dotProduct
def dotproduct():
    getAr = input("to add two 1D arrays press 1 and to add two 2D arrays press 2 ")
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
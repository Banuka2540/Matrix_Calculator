import numpy as np
from global_variables import *
from array_creating import *
from Math_operations import *
from array_manipulations import *
from slice_indexing_filtering import *
from Graphical_representations import *

while True :
    f = input(
        "💡 what are the Functions do u want to do? "
        "\n 1 .Creating arrays[1D/2D/3D/4D] "
        "\n 2 .Math operations[Adding/Multiplication/DotProducts] "
        "\n 3. Array Manipulation "
        "\n 4 .Slicing, Indexing, Filtering "
        "\n 5 .View Created arrays "
        "\n 6 .Graphical Representation "
        "\n 7 .Exit "
        "\n\n enter the number : ")
    match f:
        case "1":
            while True:
                noofDim = input("Enter number of dimensions (1 / 2 / 3 / 4 ) or 'q' to quit: ")

                match noofDim:
                    case "1":
                        dim1()
                    case "2":
                        dim2()
                    case "3":
                        dim3()
                    case "4":
                        dim4()
                    case "5":
                        break
                    case _:
                        print("Invalid input. Please enter 1, 2, 3, 4, 5")
        case "2":
            created_arrays()
            while True:
                cf = input("What operation do you want to Perform : "
                           "\n1. Adding "
                           "\n2. Multiplication "
                           "\n3. DotProducts "
                           "\n4. Exit "
                           "\n\n enter the number : ")
                match cf:
                    case "1":
                        oneDadd()
                    case "2":
                        arraymultiply()
                    case "3":
                        dotproduct()
                    case "4":
                        break
                    case _:
                        print("Invalid input. Please enter 1, 2, 3 or 4. ")
                
        case "3":
            created_arrays()
            while True:
                f = input("what are the Functions do u want to do? "
                          "\n1. reshape "
                          "\n2. flatten "
                          "\n3. Transpose "
                          "\n4. split into equal parts "
                          "\n5. Exit "
                          "\n \n enter the number :")
                match f:
                    case "1":
                        reshape_arrays()
                    case "2":
                        flattern_arrays()
                    case "3":
                        transpose_arrays()
                    case "4":
                        split_arrays()
                    case "5":
                        break
                    case _:
                        print("Invalid input. Please enter 1, 2, 3 4 0r 5. ")
        case "4":
            created_arrays()
            while True:
                cf = input(
                    "What operation do you want to Perform : "
                    "\n1. slicing "
                    "\n2. indexing "
                    "\n3. Filtering "
                    "\n4. Exit "
                    "\n\n enter the number : ")
                match cf:
                    case "1":
                        slice_arrays()
                    case "2":
                        indexing_arrays()
                    case "3":
                        filtering_arrays()
                    case "4":
                        break
                    case _:
                        print("Invalid input. Please enter 1, 2, 3 or 4. ")

        case "5":
            view_arrays()

        case "6":
            charts()

        case "7":
            break

        case _:
            print("Invalid input. Please enter 1, 2, 3 , 4, 5, 6, 7")













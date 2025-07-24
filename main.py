import numpy as np
arrays = {}

##function regarding 1D arrays
def dim1():
    name1 = input("Give a name for the array: ")
    noElements = int(input("Enter number of elements: "))
    values = []

    for i in range(noElements):
        values.append(int(input(f"Enter element {i + 1}: ")))

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

##1D Array adding
def oneDadd():
    input_str1 = input(str("enter the first name of array you want to add : "))
    input_str2 = input(str("enter the second name of array you want to add : "))
    sum = arrays[input_str1] + arrays[input_str2]
    print(sum)

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
    elif getAr == "2":
        product = arrays[input_str1] @ (arrays[input_str2])

def reshape_arrays():
    input_str1 = input("enter the name 2D array you want to reshape : ")
    if input_str1 in arrays:
        input_str2 = int(input("enter the no of rows you want to reshape : "))
        input_str3 = int(input("enter the no of columns you want to reshape : "))
        x = arrays[input_str1].reshape(input_str2, input_str3)
        print(x)
    else:
        print("Oops! No such array exists. Try again.")

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
            condition = input("Enter filter condition using 'x' (e.g., x > 5): ")
            x = arrays[input_str1]
            try:
                result = x[eval(condition)]
                print("Filtered Result:\n", result)
            except Exception as e:
                print("Error in condition:", e)
        else:
            print("Array not found.")
    else:
        print("Invalid option.")





while True :
    f = input(
        "what are the Functions do u want to do? \n 1 .Creating arrays[1D/2D] \n 2 .Math operations[Adding/Multiplication/DotProducts] \n 3. Array Manipulation \n 4 .Slicing, Indexing, Filtering \n 5 .Exit \n enter the number : ")
    match f:
        case "1":
            while True:
                noofDim = input("Enter number of dimensions (1 or 2) or 'q' to quit: ")

                match noofDim:
                    case "1":
                        dim1()
                    case "2":
                        dim2()
                    case "q":
                        break
                    case _:
                        print("Invalid input. Please enter 1, 2, or 'q'.")
        case "2":
            if arrays:
                print("\n Created Arrays:")
                for name, arr in arrays.items():
                    print(f"{name} =\n{arr}\n")
            else:
                print("⚠️ No arrays have been created yet.\n")
            cf = input("What operation do you want to Perform : \n1. Adding \n2. Multiplication \n3. DotProducts \n4. Exit")
            match cf:
                case "1":
                    oneDadd()
                case "2":
                    twoDadd()
                case "3":
                    dotproduct()
                case "4":
                    break
                
        case "3":
            if arrays:
                print("\n Created Arrays:")
                for name, arr in arrays.items():
                    print(f"{name} =\n{arr}\n")
            else:
                print("⚠️ No arrays have been created yet.\n")
            f = input("what are the Functions do u want to do? \n1. reshape \n2.flatten \n3.Transpose \n4. split into equal parts \n5. Exit \n")
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


        case "4":
            if arrays:
                print("\n Created Arrays:")
                for name, arr in arrays.items():
                    print(f"{name} =\n{arr}\n")
            else:
                print("⚠️ No arrays have been created yet.\n")

            cf = input(
                "What operation do you want to Perform : \n1. slicing \n2. indexing \n3. Filtering \n4. Exit")
            match cf:
                case "1":
                    slice_arrays()
                case "2":
                    indexing_arrays()
                case "3":
                    filtering_arrays()
                case "4":
                    break


        case "5":
            break













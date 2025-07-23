import numpy as np
arrays = {}


def Dim1():
    name1 = input("Give a name for the array: ")
    noElements = int(input("Enter number of elements: "))
    values = []

    for i in range(noElements):
        values.append(int(input(f"Enter element {i + 1}: ")))

    Arry1 = np.array(values)
    arrays[name1] = Arry1
    print(f"\n{name1} = {Arry1}\n")


def Dim2():
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


while True :
    f = input(
        "what are the Functions do u want to do? \n 1 .Creating arrays[1D/2D] \n 2 .Math operations[Adding/Multiplication/DotProducts] \n 3. Array Manipulation \n 4 .Slicing, Indexing, Filtering \n 5 .Exit \n enter the number : ")
    if f == "5" :
        break
    match f:
        case "1":
            while True:
                noofDim = input("Enter number of dimensions (1 or 2) or 'q' to quit: ")

                match noofDim:
                    case "1":
                        Dim1()
                    case "2":
                        Dim2()
                    case "q":
                        break
                    case _:
                        print("Invalid input. Please enter 1, 2, or 'q'.")
        case "2":
            if arrays:
                print("\n📌 Created Arrays:")
                for name, arr in arrays.items():
                    print(f"{name} =\n{arr}\n")
            else:
                print("⚠️ No arrays have been created yet.\n")
            cf = input("What operation do you want to Perform : ")
            if cf == "1":
                input_str = input(str("enter the names of arrays you want to add : "))
                arraynames = [name.strip() for name in input_str.split(",")]

                print("You entered:")
                for name in arraynames:
                    print(name)
                













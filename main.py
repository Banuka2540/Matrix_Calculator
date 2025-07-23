import numpy as np

noofDim = input("enter no of dimentions : ")

def Dim1():
    noElements = input("Enter no of Elements : ")
    arr1 = []
    for i in range(int(noElements)):
        arr1.append(int(input(f"Enter {i+1} th element : ")))
    Arry1 = np.array(arr1)
    print(Arry1)

def Dim2():
    rows2 = int(input("no of Rows: "))
    cols2 = int(input("no of Columns: "))
    arr2 = []
    for i in range(rows2):
        row = [int(x) for x in input(f"Enter row {i + 1} elements separated by space: ").split()]
        if len(row) != cols2:
            print("Oops! Number of elements doesn't match columns. Try again.")
        arr2.append(row)

    Arry2 = np.array(arr2)
    print(Arry2)

def Dim3():
    depth = int(input("Enter number of layers (depth): "))
    rows = int(input("Enter number of rows per layer: "))
    cols = int(input("Enter number of columns per row: "))

    cube = []

    for d in range(depth):
        print(f"Entering data for layer {d + 1}:")
        layer = []
        for r in range(rows):
            row = []
            for c in range(cols):
                val = int(input(f"Enter element at layer {d + 1}, row {r + 1}, column {c + 1}: "))
                row.append(val)
            layer.append(row)
        cube.append(layer)

        Arry3 = np.array(cube)
        print(Arry3)

def Dim4():
    import numpy as np

    w = int(input("4D blocks: "))
    d = int(input("Layers per block: "))
    r = int(input("Rows per layer: "))
    c = int(input("Columns per row: "))

    temp = []

    for w_idx in range(w):
        print(f"Enter values for block {w_idx + 1}:")
        block = []
        for d_idx in range(d):
            print(f" Layer {d_idx + 1}:")
            layer = []
            for r_idx in range(r):
                row = list(map(int, input(f"  Row {r_idx + 1} (space-separated): ").split()))
                if len(row) != c:
                    print("Wrong number of columns! Exiting...")
                    exit()
                layer.append(row)
            block.append(layer)
        temp.append(block)

    array_4d = np.array(temp)
    print(array_4d)


match noofDim:
    case "1":
        Dim1()
    case "2":
        Dim2()
    case "3":
        Dim3()
    case "4":
        Dim4()
    case _:
        print("no dimension is selected")

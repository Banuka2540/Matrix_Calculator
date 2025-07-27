arrays = {'a1':[0,1,2,3,4,5],'a2':[2,3,4,1,2,3],'a3':['a','b','c','d','e','f']}

def view_arrays():
    print(arrays)

def created_arrays():
    if arrays:
        print("\n Created Arrays:")
        for name, arr in arrays.items():
            print(f"{name} =\n{arr}\n")
    else:
        print("⚠️ No arrays have been created yet.\n")
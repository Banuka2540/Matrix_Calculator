arrays = {}

def view_arrays():
    print(arrays)

def created_arrays():
    if arrays:
        print("\n Created Arrays:")
        for name, arr in arrays.items():
            print(f"{name} =\n{arr}\n")
    else:
        print("⚠️ No arrays have been created yet.\n")
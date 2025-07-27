import numpy as np 
import matplotlib.pyplot as plt


from global_variables import *

def charts():
    type  = input("enter what type of chart you want: \n1. Line Charts \n2. Bar charts \n3. Histograms \n4. Pie Charts \nenter the number :  ")
    match type:
        case "1":
            x = input("enter the name of first array :")
            y = input("enter the name of second array :")
            try:
                xplot = arrays[x]
                yplot = arrays[y]
                plt.plot(xplot, yplot)
                plt.show()
            except KeyError:
                print("check the name of the arrays ")
            except ValueError:
                print("check the length of the arrays ")
        case "2":
            x = input("enter the name of first array :")
            y = input("enter the name of second array :")
            try:
                xplot = arrays[x]
                yplot = arrays[y]
                plt.subplot(2,1,1)
                plt.bar(xplot, yplot)
                plt.subplot(2, 1, 2)
                plt.barh(xplot, yplot)
                plt.show()
            except KeyError:
                print("check the name of the arrays ")
            except ValueError:
                print("check the length of the arrays ")
        case "3":
            x = input("Enter the name of array for histogram: ")
            try:
                data = arrays[x]
                plt.hist(data, bins=10, edgecolor='black')

                plt.show()
            except KeyError:
                print(" Array name not found.")
        case "4":
            x = input("Enter the name of array for pie diagram: ")
            try :
                plt.pie(arrays[x],autopct='%1.1f%%')
                plt.axis('equal')
                plt.show()
            except:
                print("check the name of the arrays ")
        case _:
            print("Wrong input")


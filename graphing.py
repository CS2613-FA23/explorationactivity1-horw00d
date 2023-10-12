import matplotlib.pyplot as plt
import numpy as np
import csv
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

dimension = input("Please input whether you want to graph 2D or 3D data: ")

def bar(my_list, count):
    plt.style.use('_mpl-gallery')
    x = 0.5 + np.arange(count)
    y = my_list

    fig, ax = plt.subplots()
    ax.bar(x, y, width=1, edgecolor="black", linewidth=0.7)

    ax.set(title='Bar Chart', xlim=(0, count), xticks=np.arange(1, count), ylim=(0, count), yticks=np.arange(1, count))
    plt.show()
    
if dimension == "2D":
    value = input("Would you like to enter your -OWN- data or read a .-CSV- file?: ")
    my_list = []
    count = 0
    if value == "OWN":
        count = int(input("How many values would you like to enter?: "))
        my_list = [0] * count
        for i in range(count):
            my_list[i] = int(input())
    else:
        file = open(input("What is the file name?: "))
        csvreader = csv.reader(file)
        for row in csvreader:
            for value in row:
                my_list.append(value)
        count = len(my_list)
    bar(my_list, count)

def shape3D(shapeFunction, colormap=cm.Purples, linewidth=1):
    X = np.arange(-5, 5, 0.25)
    Y = np.arange(-5, 5, 0.25)
    X, Y = np.meshgrid(X, Y)
    
    R = np.sqrt(X**2 + Y**2)
    Z =shapeFunction(R)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.plot_surface(X, Y, Z, cmap=colormap, rstride=1, cstride=1, linewidth=linewidth, antialiased=True)

    ax.set_title('3D Surface Plot')
    plt.show()

if dimension == "3D":
    shapeOptions = {
        'Sine Wave': lambda r: np.sin(r),
        'Cosine Wave': lambda r: np.cos(r),
        'Sphere': lambda r: np.sqrt(1 - np.square(r)),
        'Cylinder': lambda r: np.sqrt(1 - np.square(r)),
        'Hyperbolic Paraboloid': lambda r: r,
        'Elliptical Paraboloid': lambda r: np.square(r),
        'Gaussian Function': lambda r: np.exp(-0.5 * r)
    }

    print("Please choose one of the following options for shapes:")
    for option in shapeOptions:
        print(option)

    shapeChoice = input("Enter your choice: ")

    cmChoice = input("Enter a colormap in the following format (e.g., 'Greens'): ")

    lnWidth = int(input("Please enter the desired line width: "))

    shape3D(shapeOptions[shapeChoice], getattr(cm, cmChoice), lnWidth)



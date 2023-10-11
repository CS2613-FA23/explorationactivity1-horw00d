[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/oB7VDeFN)
# ExplorationActivity1
## 1. Which package/library does the sample program demonstrate?

This program demonstrates the functionality of the Matplotlib.

## 2. How does someone run your program?

This program can be run through a terminal that is currently in the same directory as the program. By using the Python package installer (pip), you can run the following command and it will install the Matplotlib library [1]:

 - pip install matplotlib

From there, you can run the program and interact with it through the terminal with keyboard input by following the instrictions printed by the program.

## 3. What purpose does your program serve?
This program is used to help the user visualize data and graphing in useful ways while also testing the functionality of the Matplotlib library. The 2D option within the program takes in a list of values in one of two formats chosen by the user and displays it with a barchart, while the 3D option allows the user to visualize a complex 3D shape of their choice using customizable input.

## 4. What would be some sample input/output?

Here is some sample input/output for the 2D option:  

**python graphing.py**  
Please input whether you want to graph 2D or 3D data: **2D**  
Would you like to enter your -OWN- data or read a .-CSV- file?: **OWN**  
How many values would you like to enter?: **5**  
3  
1  
2  
4  
5  
*Program will open interactive GUI and display graph*

-----------------------------------------------  

Here is some sample input/output for the 3D option:  
**python graphing.py**  
Please input whether you want to graph 2D or 3D data: **3D**  
Please choose one of the following options for shapes:  
Sine Wave  
Cosine Wave  
Sphere  
Cylinder  
Hyperbolic Paraboloid  
Elliptical Paraboloid  
Gaussian Function  
Enter your choice: Sphere  
Enter a colormap in the following format (e.g., 'Greens'): **Reds**  
Please enter the desired line width: **1**  
*Program will open interactive GUI and display graph*

 References:
 [1]https://matplotlib.org/stable/users/getting_started/

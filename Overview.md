## 1. Which package/library does the sample program demonstrate?

The library selected for this Exploration Activity is Matplotlib for Python.

## 2. What is the package/library?

The purpose of this library is to interact with Python programs and create graphic visulaizations of different types of data[1]. The graphing options include 3D and 2D plotting which allows for a large variety of possibilities for representing data. These graphs are very customizable in both their layout like colour, axes and titles as well as what they can take in for user input[2]. These capabilties can be useful for visualizing large datasets that are difficult to find trends or graphing a complex 3D shape in an engineering setting. The library is useful because it is integrated with the Numpy library making it a powerful data visualization tool because of its data structure and mathematical tools[3][4]. The intention behind the library is to be a good open-source alternative to MATLAB that could be used with the diverse capabilities of Python[5].

This program can be run through a terminal that is currently in the same directory as your Python script or also from a Jupyter notbook. By using the Python package installer (pip), you can run the following command and it will install the Matplotlib library:

 - pip install matplotlib  
[6]

From there, you can reference the library documentation and customize and plot your graphs which will be displayed through an interactive GUI window.

## 3. What are the functionalities of the package/library?

Add the following import statement at the top of your program to more easily reference Matplotlib's functionality:
 - import matplotlib.pyplot as plt

__Creating a 2D bar chart:__  

    #These lines will determine which style your graph will mimic and also what values will represent the X and Y axes of your graph    
    plt.style.use('_mpl-gallery')  
    x = 0.5 + np.arange(count)  
    y = my_list  
  
    #Creating the fig which is the entire plotting area and the ax which is our individual graph to be displayed  
    fig, ax = plt.subplots()
    ax.bar(x, y, width=1, edgecolor="black", linewidth=0.7)  

    #Setting the title of the graph and the lenght limits/arrangements for our x and y axes#  
    ax.set(title='Bar Chart', xlim=(0, count), xticks=np.arange(1, count), ylim=(0, count), yticks=np.arange(1, count))  
    #Displaying our plot via an interactive GUI window when this point of the program is reached*  
    plt.show()
*Here's an example of what that output could look like:*  
![Alt text](image-2.png)     
__Creating a 3D graph:__  
    
    #Creating the 3D surface plot
    X = np.arange(-5, 5, 0.25)
    Y = np.arange(-5, 5, 0.25)
    X, Y = np.meshgrid(X, Y)
    
    #Usign the Euclidean distance formula to caluclate the distance from the origin to each point on the grid
    R = np.sqrt(X**2 + Y**2)

    #Caluclates the Z values using the shape that the user inputed
    Z =shapeFunction(R)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    #Generate the surface plot using X, Y and Z arrays. Altering the colormap and line width of the graph using user-input.  
    ax.plot_surface(X, Y, Z, cmap=colormap, rstride=1, cstride=1, linewidth=linewidth, antialiased=True)
    
    #Set the title of the graph for display purposes
    ax.set_title('3D Surface Plot')

    #Displaying our plot via an interactive GUI window when this point of the program is reached*  
    plt.show()

*Here's an example of what that output could look like:*  
![Alt text](image-3.png)
  
## 4. When was it created?   
This library was created by John Hunter in 2002. This was initially a project used to help ECoG data for patients that were experiencing epilepsy. 

## 5. Why did you select this package/library?
I chose to explore this library because we hadn't done much graphical representation such as GUIs or HTML in the CS2613 course yet and I figured that this would be a fun and interesting challenge. The library seemed like it would have useful applications in the future when working with large data sets and graphical visualization. When exploring the documentation, it seemed relatively reivial to implement into a Python script and I was impressed by its graphing capabilities.

## 6. How did learning the package/library influence your learning of the language?
Learning this library gave me an interesting experience with Python and opened my eyes to its possibilities in terms of how user input can be transformed into something much more visually stimulating than simple terminal output. It allowed me to be creative in terms of how I designed the program to work and how to familiarize myself with programming concepts that we hadn't yet learned by looking at documentation. I would say that overall this library taught me to be a more independant and explorative programmer.

## 7. How was your overall experience with the package/library? 
I would definitley recommend Matplotlib to other programmers who are working on a project related to graphing or someone who is curious about exploring a new easy-to-use library with fun output. It may not be a library that is useful in all aspects of programming, but I think it could add some breadth to your coding abilities. I will personally continue to use this library as I am currently working on a personal project that interacts with the Spotify API through Python to collect user statistics and I think those would be neat to graph. I'm sure that in future courses it will also be useful when analyzing large data sets. I don't plan on uninstalling the library any time soon, and I'm glad that I had the opportunity to explore it.

References:  
[1]https://matplotlib.org/  
[2]https://matplotlib.org/stable/plot_types/index.html  
[3]https://matplotlib.org/stable/users/explainquick_start.html  
[4]https://www.tutorialspoint.com/numpy/numpy_matplotlib.htm  
[5]https://www.activestate.com/resources/quick-reads/what-is-matplotlib-in-python-how-to-use-it-for-plotting/  
[6]https://matplotlib.org/stable/users/getting_started/   
[7]https://www.scaler.com/topics/matplotlib/matplotlib-in-python/

# Traveling Salesman Problem Solver for Circuit Board Design

This Python project provides a graphical user interface (GUI) application to solve the Traveling Salesman Problem (TSP) for circuit board design. The TSP is a classic optimization problem where the goal is to find the shortest possible route that visits a given set of components and returns to the starting component. In the context of circuit board design, this can be useful for optimizing the order in which components are connected on the board.

## Features

- **User-Friendly GUI:** The application utilizes the Tkinter library to create a user-friendly interface where users can input the number of components and the distance matrix between them.

- **TSP Solver:** The core of the application includes a TSP solver algorithm that generates all possible permutations of component indices and finds the optimal route with the minimum total distance.

- **Graph Visualization:** The application uses the NetworkX and Matplotlib libraries to visualize the optimal route on a directed graph, providing a clear representation of the circuit board layout.

## How to Use

1. **Input Number of Components:** Enter the number of components in the designated entry field.

2. **Enter Distance Matrix:** Fill in the distance matrix, representing the distances between each pair of components. The matrix is dynamically generated based on the number of components entered.

3. **Click Solve:** Click the "Solve" button to calculate the optimal route and minimum distance. A new window will appear with the results, including the optimal route and minimum distance.

4. **Graph Visualization:** The results window also includes a visualization of the circuit board layout, showing the optimal route with labeled distances.

## Requirements

- Python 3.x
- Tkinter
- Matplotlib
- NetworkX

## Contributing

Feel free to contribute to this project by opening issues, providing feedback, or submitting pull requests. Your input is highly appreciated!


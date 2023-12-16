import itertools
import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
import networkx as nx

def tsp(components, distance_matrix):
    # Generate all possible permutations of component indices
    permutations = list(itertools.permutations(components))

    # Initialize the minimum distance and optimal route
    min_distance = float('inf')
    optimal_route = []

    # Iterate over all permutations and calculate the total distance
    for route in permutations:
        distance = calculate_distance(route, distance_matrix)
        if distance < min_distance:
            min_distance = distance
            optimal_route = route

    return optimal_route, min_distance

def calculate_distance(route, distance_matrix):
    distance = 0
    for i in range(len(route) - 1):
        # Assuming distances between components are given in a distance matrix
        distance += distance_matrix[route[i]][route[i + 1]]

    # Add distance from the last component back to the starting component
    distance += distance_matrix[route[-1]][route[0]]
    return distance

def visualize_graph(optimal_route, distance_matrix):
    num_components = len(optimal_route)

    # Create a directed graph
    G = nx.DiGraph()

    # Add nodes to the graph
    for component in optimal_route:
        G.add_node(component)

    # Add edges to the graph
    for i in range(num_components - 1):
        start_node = optimal_route[i]
        end_node = optimal_route[i + 1]
        distance = distance_matrix[start_node][end_node]
        G.add_edge(start_node, end_node, weight=distance)

    # Add edge from the last node back to the starting node
    start_node = optimal_route[num_components - 1]
    end_node = optimal_route[0]
    distance = distance_matrix[start_node][end_node]
    G.add_edge(start_node, end_node, weight=distance)

    # Set positions for the nodes
    pos = nx.spring_layout(G)

    # Draw the graph
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=10, arrows=True)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Set title and show the graph
    plt.title("Optimal Route Visualization")
    plt.show()

def solve_tsp():
    try:
        num_components = int(num_components_entry.get())
        components = list(range(num_components))

        # Initialize the distance matrix
        distance_matrix = []
        for i in range(num_components):
            row = []
            for j in range(num_components):
                row.append(int(distance_entries[i][j].get()))
            distance_matrix.append(row)

        # Call the tsp function
        optimal_route, min_distance = tsp(components, distance_matrix)

        # Display results in a separate window
        result_window = tk.Toplevel(window)
        result_window.title("TSP Results")

        optimal_route_label = ttk.Label(result_window, text="Optimal Route:")
        optimal_route_label.pack()
        optimal_route_text = ttk.Label(result_window, text=str(optimal_route))
        optimal_route_text.pack()

        min_distance_label = ttk.Label(result_window, text="Minimum Distance:")
        min_distance_label.pack()
        min_distance_text = ttk.Label(result_window, text=str(min_distance))
        min_distance_text.pack()

        # Visualize the graph
        visualize_graph(optimal_route, distance_matrix)

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numeric values.")

# Create the main window
window = tk.Tk()
window.title("Circuit Board Design - TSP Solver")

# Create components for user input
num_components_label = ttk.Label(window, text="Number of Components:")
num_components_label.grid(row=0, column=0, padx=10, pady=10)
num_components_entry = ttk.Entry(window)
num_components_entry.grid(row=0, column=1, padx=10, pady=10)

distance_matrix_label = ttk.Label(window, text="Distance Matrix:")
distance_matrix_label.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

distance_entries = []

table_frame = ttk.Frame(window)
table_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

for i in range(10):
    distance_row = []
    for j in range(10):
        distance_entry = ttk.Entry(table_frame, width=8)
        distance_entry.grid(row=i, column=j, padx=5, pady=5)
        distance_row.append(distance_entry)
    distance_entries.append(distance_row)

solve_button = ttk.Button(window, text="Solve", command=solve_tsp)
solve_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Start the GUI event loop
window.mainloop()

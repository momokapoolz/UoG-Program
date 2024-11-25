import networkx as nx
import matplotlib.pyplot as plt

# Create a graph object
MyGraph = nx.Graph(Name="Station", type="station")

def task1():
    stations = [
        # First line
        ('Hyde Park Corner', {'position': (0, 0)}),
        ('Green Park', {'position': (1, 1)}),
        ('Piccadilly Circus', {'position': (2, 1)}),
        ('Leicester Square', {'position': (3, 1)}),
        ('Covent Garden', {'position': (4, 2)}),
        ('Holborn', {'position': (5, 3)}),

        # Second line
        ('Notting Hill Gate', {'position': (0, 1)}),
        ('Marble Arch', {'position': (1, 2)}),
        ('Bond Street', {'position': (2, 3)}),
        ('Oxford Circus', {'position': (3, 3)}),
        ('Tottenham Court Road', {'position': (4, 3)}),

        # Third line
        ('Russell Square', {'position': (6, 3)}),
        ('King\'s Cross St. Pancras', {'position': (7, 3)}),
        ('Caledonian Road', {'position': (8, 3)}),
        ('Holloway Road', {'position': (9, 3)}),
        ('Arsenal', {'position': (10, 3)}),
        ('Finsbury Park', {'position': (11, 3)}),
    ]

    # Define the edges with distances
    edges = [
        # First line
        ('Hyde Park Corner', 'Green Park', 0.64),
        ('Green Park', 'Piccadilly Circus', 0.8),
        ('Piccadilly Circus', 'Leicester Square', 0.3),
        ('Leicester Square', 'Covent Garden', 0.5),
        ('Covent Garden', 'Holborn', 0.6),

        # Second line
        ('Notting Hill Gate', 'Marble Arch', 1.4),
        ('Marble Arch', 'Bond Street', 0.8),
        ('Bond Street', 'Oxford Circus', 0.3),
        ('Oxford Circus', 'Tottenham Court Road', 0.5),
        ('Tottenham Court Road', 'Holborn', 0.6),

        # Third line
        ('Russell Square', 'King\'s Cross St. Pancras', 0.5),
        ('King\'s Cross St. Pancras', 'Caledonian Road', 1.2),
        ('Caledonian Road', 'Holloway Road', 0.7),
        ('Holloway Road', 'Arsenal', 0.7),
        ('Arsenal', 'Finsbury Park', 0.6),
    ]

    # Add nodes and edges to the graph
    MyGraph.add_nodes_from(stations)
    MyGraph.add_edges_from(edges)

    # Get positions from node attributes
    position = {station: data['position'] for station, data in MyGraph.nodes(data=True)}

    # Draw the graph
    plt.figure(figsize=(10, 6))
    nx.draw(MyGraph, position, with_labels=True, node_color='blue', node_size=500, font_size=7, font_color='black',
            edge_color='blue', width=2)

    # Draw edge labels
    edge_labels = {(u, v): label for u, v, label in edges}
    nx.draw_networkx_edge_labels(MyGraph, position, edge_labels=edge_labels, font_size=7, font_color="red")

    # Add legend
    plt.legend(['Piccadilly Line and others'], loc='lower right', fontsize=12)

    plt.title("Tube Stations and Distances")
    plt.show()

task1()

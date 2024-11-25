import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

MyGraph = nx.Graph(Name="Graph1",type="demo")

#First line: dark blue line: Piccaddly
MyGraph.add_node('Hyde Park Corner', npos=(3, 4), ccn='#00008B')
MyGraph.add_node('Green Park', npos=(4, 5), ccn='#00008B')
MyGraph.add_node('Piccadlly Circus', npos=(5.5 , 5), ccn='#00008B')
MyGraph.add_node('Leicester Square', npos=(6, 6), ccn='#00008B')
MyGraph.add_node('Convent Garden', npos=(7, 7), ccn='#00008B')
MyGraph.add_node('Holborn', npos=(8, 8), ccn='#00008B')

###Second line: red: Central
MyGraph.add_node('Lancaster Gate', npos=(2, 8), ccn='#FF0000')
MyGraph.add_node('Marble Arch', npos=(3, 8), ccn='#FF0000')
MyGraph.add_node('Bond Street', npos=(4, 8), ccn='#FF0000')
MyGraph.add_node('Oxford Cirtrus', npos=(5, 8), ccn='#FF0000')
MyGraph.add_node('Totteham Court Road', npos=(6, 8), ccn='#FF0000')
#MyGraph.add_node('Holborn', npos=(8, 8), ccn='#00008B')

###Third line: brown: Bakerloo
MyGraph.add_node('Edware Road', npos=(1, 10), ccn='#A52A2A')
MyGraph.add_node('Marylebone', npos=(2, 10), ccn='#A52A2A')
MyGraph.add_node('Regent Park', npos=(4, 9), ccn='#A52A2A')
#MyGraph.add_node('Oxford Cirtrus', npos=(5, 8), ccn='#FF0000')
#MyGraph.add_node('Piccadlly Circus', npos=(5.5, 5), ccn='#00008B')
MyGraph.add_node('Charring Cross', npos=(6, 4), ccn='#A52A2A')

###Fourth line: light blue: Victoria
MyGraph.add_node('Plimico', npos=(4, 0), ccn='#ADD8E6')
MyGraph.add_node('Victoria', npos=(4, 2), ccn='#ADD8E6')
#MyGraph.add_node('Green Park', npos=(4, 5), ccn='#00008B')
#MyGraph.add_node('Oxford Cirtrus', npos=(5, 8), ccn='#FF0000')
MyGraph.add_node('Warren Street', npos=(6, 9), ccn='#ADD8E6')
MyGraph.add_node('King Cross', npos=(8, 11), ccn='#ADD8E6')










#line
##DarkBlueLine
MyGraph.add_edge('Hyde Park Corner', 'Green Park', cce='#00008B')
MyGraph.add_edge('Green Park', 'Piccadlly Circus', cce='#00008B')
MyGraph.add_edge('Piccadlly Circus', 'Leicester Square', cce='#00008B')
MyGraph.add_edge('Leicester Square', 'Convent Garden', cce='#00008B')
MyGraph.add_edge('Convent Garden', 'Holborn', cce='#00008B')


##RedLine
MyGraph.add_edge('Lancaster Gate', 'Marble Arch', cce='#FF0000')
MyGraph.add_edge('Marble Arch', 'Bond Street', cce='#FF0000')
MyGraph.add_edge('Bond Street', 'Oxford Cirtrus', cce='#FF0000')
MyGraph.add_edge('Oxford Cirtrus', 'Totteham Court Road', cce='#FF0000')
MyGraph.add_edge('Totteham Court Road', 'Holborn', cce='#FF0000')


#BrownLine
MyGraph.add_edge('Edware Road', 'Marylebone', cce='#A52A2A')
MyGraph.add_edge('Marylebone', 'Regent Park', cce='#A52A2A')
MyGraph.add_edge('Regent Park', 'Oxford Cirtrus', cce='#A52A2A')
MyGraph.add_edge('Oxford Cirtrus', 'Piccadlly Circus', cce='#A52A2A')
MyGraph.add_edge('Piccadlly Circus', 'Charring Cross', cce='#A52A2A')


#LightBlueLine
MyGraph.add_edge('Plimico', 'Victoria', cce='#ADD8E6')
MyGraph.add_edge('Victoria', 'Green Park', cce='#ADD8E6')
MyGraph.add_edge('Green Park', 'Oxford Cirtrus', cce='#ADD8E6')
MyGraph.add_edge('Oxford Cirtrus', 'Warren Street', cce='#ADD8E6')
MyGraph.add_edge('Warren Street', 'King Cross', cce='#ADD8E6')


# Extract attributes from the graph to dictionaries
pos = nx.get_node_attributes(MyGraph, 'npos')
nodecolour = nx.get_node_attributes(MyGraph, 'ccn')
edgecolour = nx.get_edge_attributes(MyGraph, 'cce')

# Place the dictionary values in array
nodearray = nodecolour.values()
edgearray = edgecolour.values()

# Draw the graph's nodes and edges
nx.draw_networkx(MyGraph, pos, node_color=nodearray)
nx.draw_networkx_edges(MyGraph, pos, edge_color=edgearray)

#distance
distances = {
    ('Hyde Park Corner', 'Green Park'): 0.5,
    ('Green Park', 'Piccadilly Circus'): 0.4,
    ('Piccadilly Circus', 'Leicester Square'): 0.3,
    ('Leicester Square', 'Covent Garden'): 0.2,
    ('Covent Garden', 'Holborn'): 0.5,
    ('Lancaster Gate', 'Marble Arch'): 0.8,
    ('Marble Arch', 'Bond Street'): 0.4,
    ('Bond Street', 'Oxford Circus'): 0.3,
    ('Oxford Circus', 'Tottenham Court Road'): 0.4,
    ('Edgware Road', 'Marylebone'): 0.3,
    ('Marylebone', 'Regent Park'): 0.5,
    ('Regent Park', 'Charing Cross'): 1.5,
    ('Pimlico', 'Victoria'): 0.6,
    ('Victoria', 'Green Park'): 0.8,
    ('Warren Street', 'King Cross'): 1.2
}


# Get the list of distances
distance_values = np.array(list(distances.values()))

# Calculate total sum
total_sum = np.sum(distance_values)

# Calculate average
average = np.mean(distance_values)

# Calculate standard deviation
std_deviation = np.std(distance_values)

# Print the results
print(f"Total distance: {total_sum}")
print(f"Average: {average}")
print(f"Standard Deviation: {std_deviation}")

#
#
#
#
# # Calculate midpoint for annotation
# midpoint = [(pos['Hyde Park Corner'][0] + pos['Green Park'][0]) / 2, (pos['Hyde Park Corner'][1] + pos['Green Park'][1]) / 2]
# plt.annotate('0.5', midpoint, textcoords="offset points", xytext=(0,10), ha='center', color='#000000')
#
# midpoint1 = [(pos['Green Park'][0] + pos['Piccadlly Circus'][0]) / 2, (pos['Green Park'][1] + pos['Piccadlly Circus'][1]) / 2]
# plt.annotate('0.4', midpoint1, textcoords="offset points", xytext=(0,10), ha='center', color='#000000')
#
# midpoint2 = [(pos['Piccadilly Circus'][0] + pos['Leicester Square'][0]) / 2, (pos['Piccadilly Circus'][1] + pos['Leicester Square'][1]) / 2]
# plt.annotate('0.3', midpoint2, textcoords="offset points", xytext=(0,10), ha='center', color='#000000')
#
# midpoint3 = [(pos['Leicester Square'][0] + pos['Covent Garden'][0]) / 2, (pos['Leicester Square'][1] + pos['Covent Garden'][1]) / 2]
# plt.annotate('0.2', midpoint3, textcoords="offset points", xytext=(0,10), ha='center', color='#000000')
#
# midpoint4 = [(pos['Covent Garden'][0] + pos['Holborn'][0]) / 2, (pos['Covent Garden'][1] + pos['Holborn'][1]) / 2]
# plt.annotate('0.5', midpoint4, textcoords="offset points", xytext=(0,10), ha='center', color='#000000')
#
# midpoint5 = [(pos['Lancaster Gate'][0] + pos['Marble Arch'][0]) / 2, (pos['Lancaster Gate'][1] + pos['Marble Arch'][1]) / 2]
# plt.annotate('0.8', midpoint5, textcoords="offset points", xytext=(0,10), ha='center', color='#000000')
#
# midpoint6 = [(pos['Marble Arch'][0] + pos['Bond Street'][0]) / 2, (pos['Marble Arch'][1] + pos['Bond Street'][1]) / 2]
# plt.annotate('0.4', midpoint6, textcoords="offset points", xytext=(0,10), ha='center', color='#000000')
#
# midpoint7 = [(pos['Bond Street'][0] + pos['Oxford Circus'][0]) / 2, (pos['Bond Street'][1] + pos['Oxford Circus'][1]) / 2]
# plt.annotate('0.3', midpoint7, textcoords="offset points", xytext=(0,10), ha='center', color='#000000')
#
# midpoint8 = [(pos['Oxford Circus'][0] + pos['Tottenham Court Road'][0]) / 2, (pos['Oxford Circus'][1] + pos['Tottenham Court Road'][1]) / 2]
# plt.annotate('0.4', midpoint8, textcoords="offset points", xytext=(0,10), ha='center', color='#000000')
#
# midpoint9 = [(pos['Edgware Road'][0] + pos['Marylebone'][0]) / 2, (pos['Edgware Road'][1] + pos['Marylebone'][1]) / 2]
# plt.annotate('0.3', midpoint9, textcoords="offset points", xytext=(0,10), ha='center', color='#000000')
#
# midpoint10 = [(pos['Marylebone'][0] + pos['Regent Park'][0]) / 2, (pos['Marylebone'][1] + pos['Regent Park'][1]) / 2]
# plt.annotate('0.5', midpoint10, textcoords="offset points", xytext=(0,10), ha='center', color='#000000')
#
# midpoint11 = [(pos['Regent Park'][0] + pos['Charing Cross'][0]) / 2, (pos['Regent Park'][1] + pos['Charing Cross'][1]) / 2]
# plt.annotate('1.5', midpoint11, textcoords="offset points", xytext=(0,10), ha='center', color='#000000')
#
# midpoint12 = [(pos['Pimlico'][0] + pos['Victoria'][0]) / 2, (pos['Pimlico'][1] + pos['Victoria'][1]) / 2]
# plt.annotate('0.6', midpoint12, textcoords="offset points", xytext=(0,10), ha='center', color='#000000')
#
# midpoint13 = [(pos['Victoria'][0] + pos['Green Park'][0]) / 2, (pos['Victoria'][1] + pos['Green Park'][1]) / 2]
# plt.annotate('0.8', midpoint13, textcoords="offset points", xytext=(0,10), ha='center', color='#000000')
#
# midpoint14 = [(pos['Warren Street'][0] + pos['King Cross'][0]) / 2, (pos['Warren Street'][1] + pos['King Cross'][1]) / 2]
# plt.annotate('1.2', midpoint14, textcoords="offset points", xytext=(0,10), ha='center', color='#000000')


# Visualise the graph
plt.title("City Transportation Layout")
plt.show()


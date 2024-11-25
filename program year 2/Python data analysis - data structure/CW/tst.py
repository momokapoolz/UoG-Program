import matplotlib.pyplot as plt
import math

# Position of the locations
pos = {
    'Hyde Park Corner': (3, 4),
    'Green Park': (4, 5),
    'Piccadilly Circus': (5.5, 5),
    'Leicester Square': (6, 6),
    'Covent Garden': (7, 7),
    'Holborn': (8, 8),
    'Lancaster Gate': (2, 8),
    'Marble Arch': (3, 8),
    'Bond Street': (4, 8),
    'Oxford Circus': (5, 8),
    'Tottenham Court Road': (6, 8),
    'Edgware Road': (1, 10),
    'Marylebone': (2, 10),
    'Regent\'s Park': (4, 9),
    'Charing Cross': (6, 4),
    'Pimlico': (4, 0),
    'Victoria': (4, 2),
    'Warren Street': (6, 9),
    'King\'s Cross': (8, 11)
}

# Distances between locations (in miles) based on real-world data
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
    ('Marylebone', 'Regent\'s Park'): 0.5,
    ('Regent\'s Park', 'Charing Cross'): 1.5,
    ('Pimlico', 'Victoria'): 0.6,
    ('Victoria', 'Green Park'): 0.8,
    ('Warren Street', 'King\'s Cross'): 1.2
}

# Plotting the distances on the graph
for loc1, loc2 in distances.keys():
    # Calculate midpoint
    midpoint = [(pos[loc1][0] + pos[loc2][0]) / 2, (pos[loc1][1] + pos[loc2][1]) / 2]

    # Annotate the distance
    distance = distances[(loc1, loc2)]
    plt.annotate(f'{distance}', midpoint, textcoords="offset points", xytext=(0, 10), ha='center', color='#000000')

# Assuming the rest of the graph plotting code is here...

# Display the plot with distances annotated
plt.title('City Transportation Layout with Distances')
plt.show()

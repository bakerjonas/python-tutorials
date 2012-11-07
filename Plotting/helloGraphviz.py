import networkx as nx
import matplotlib.pyplot as plt

# Crate graph object
G = nx.Graph()

# First add nodes
G.add_node('A')
G.add_node('B')
G.add_node('C')
G.add_node('D')

# and calculate position of nodes
pos = nx.spring_layout(G, iterations=200)

# Then add edges
G.add_edge('A', 'B')
G.add_edge('A', 'C')
G.add_edge('C', 'D')

# Set edge styles and labels
nx.draw_networkx_edges(G, pos, edgelist=[('A', 'C')], style='dotted')
nx.draw_networkx_edge_labels(G, pos, edge_labels={('C', 'D'): 'a label'})

# Set node styles
nx.draw(G, pos, node_color=['red', 'green', 'blue', 'yellow'])

# Show graph
plt.show()

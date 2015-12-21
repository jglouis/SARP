import networkx as nx
import matplotlib.pyplot as plt

graph = nx.DiGraph()
#graph.add_nodes_from([2,3])
graph.add_weighted_edges_from([
        (1,2,1),(2,3,4),
        (1,4,2), (2,5,5),(3,6,7),
        (4,5,11),(5,6,12),
        (4,7,9),(5,8,16),(6,9,14),
        (7,8,15),(8,9,18)])


nx.draw(graph)

plt.show()
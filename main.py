try:
    import matplotlib.pyplot as plt
except:
    raise

import networkx as nx

G=nx.MultiDiGraph()

G.add_edge(1,2,weight=1)
G.add_edge(2,1,weight=3)
G.add_edge(2,3,weight=4)
G.add_edge(3,2,weight=6)
G.add_edge(1,4,weight=2)
G.add_edge(4,1,weight=8)
G.add_edge(2,5,weight=5)
G.add_edge(5,2,weight=10)
G.add_edge(3,6,weight=7)
G.add_edge(6,3,weight=13)
G.add_edge(5,4,weight=11)
G.add_edge(5,5,weight=21)
G.add_edge(5,6,weight=12)

G.add_edge(4,7,weight=9)
G.add_edge(8,5,weight=16)
G.add_edge(6,9,weight=14)
G.add_edge(9,6,weight=19)

G.add_edge(7,8,weight=15)
G.add_edge(8,7,weight=17)
G.add_edge(8,9,weight=18)
G.add_edge(9,8,weight=20)


elarge=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] >0.5]
esmall=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] <=0.5]

pos=nx.spring_layout(G) # positions for all nodes

# nodes
nx.draw_networkx_nodes(G,pos,node_size=700)

# edges
nx.draw_networkx_edges(G,pos,edgelist=elarge,
                    width=6)
nx.draw_networkx_edges(G,pos,edgelist=esmall,
                    width=6,alpha=0.5,edge_color='b',style='dashed')

# labels
nx.draw_networkx_labels(G,pos,font_size=20,font_family='sans-serif')

plt.axis('off')
plt.savefig("multigraph.png") # save as png
plt.show()
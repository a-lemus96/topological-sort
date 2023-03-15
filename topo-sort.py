# standard library modules
from typing import Any, List

# third-party modules
import matplotlib.pyplot as plt
import networkx as nx # we use it just for plotting with networkx.drawing module

# custom modules
import dfs
import bgwgraph as bgwg
    

# initialize test graph 
keys = ['belt', 'jacket', 'pants', 'shirt', 'shoes',
        'socks', 'tie', 'undershorts', 'watch']
edges = [('belt', 'jacket'), ('pants', 'belt'), ('pants', 'shoes'), 
         ('shirt', 'belt'), ('shirt', 'tie'), ('socks', 'shoes'),
         ('tie', 'jacket'), ('undershorts', 'pants'), ('undershorts', 'shoes')]

G = bgwg.DiGraph(keys, edges)
print(f"Acyclic graph with {G.size_nodes()} nodes and {G.size_edges()} edges\n")
for node in G.nodes:
    print(f"Node: {node},\t\tAdjacent Nodes: {G.adj[node]}")

# call DFS to compute finishing times for each vertex
sorting = dfs.dfs(G)
print(f"\nTopologial sorting with '{keys[0]}' as source: {sorting}")

"""# create nx.DiGraph object just for plotting purposes
G_nx = nx.DiGraph()
G_nx.add_nodes_from(keys)
G_nx.add_edges_from(edges)

fig, ax = plt.subplots(layout='constrained')
ax = nx.draw(G_nx, with_labels=True, font_weight='bold')
plt.savefig('out/digraph.png')
plt.close()"""

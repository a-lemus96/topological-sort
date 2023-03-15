# standard library modules
from typing import Any, List

# third-party modules
import networkx as nx # just for plotting

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
print(G.size_nodes(), G.size_edges())
for node in G.get_nodes():
    print(f"Node: {node.key}, Adj: {G.get_adj(node)}")

# call DFS to compute finishing times for each vertex
sorting = dfs.dfs(G)

[print(node.key) for node in sorting]

# plot topological ordered graph

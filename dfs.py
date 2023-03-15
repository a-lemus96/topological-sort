# standard library modules
from typing import Any, List

# custom modules
import bgwgraph as bgwg


def dfs(G: bgwg.DiGraph) -> List[Any]:
    """Performs Depth-First Search algorithm on graph G starting from the first
    source BGW node in G node list.
    ----------------------------------------------------------------------------
    Args:
        G: directed acyclic graph. If G contains nodes the problem has been
           shown to have no solution
    Returns:
        sorting: list of ordered nodes in decreasingorder based on their
        finish timestamp"""
    sorting = [] # list to containg topological sorting
    time = 0 # initialize timestamp


    def dfs_visit(key: Any, t0: int = 0) -> int:
        """Implements recursive function to visit all nodes reachable from a
        source BGW node. It updates their timestamp and their color accordingly.
        ------------------------------------------------------------------------
        Args:
            node: key for node object to explore
            t0: initial timestamp prior to calling this fn
        Returns:
            time: timestamp after finishing this fn call"""
        time = t0 + 1 # a white node has just been discovered
        G.nodes[key].td = time
        G.nodes[key].set_color('gray') # update G's data
        u = G.nodes[key]

        # iterate over adjacency list of node u
        for child_key in G.adj[key]:
            # retrieve object associated to that key
            v = G.nodes[child_key]
            if v.get_color() == 'white': # explore this edge
               G.nodes[child_key].set_parent(u)
               time = dfs_visit(child_key, time)
        
        G.nodes[key].set_color('black') # blacken node; it is finished
        time = time + 1
        G.nodes[key].tf = time
        sorting.append(key) # append blacked node to sorting list

        return time
    
    
    for key in G.nodes:
        if G.nodes[key].get_color() == 'white':
            dfs_visit(key)
    
    return list(reversed(sorting))

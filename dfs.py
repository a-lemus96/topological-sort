# standard library modules
from typing import Any, List

# custom modules
import bgwgraph as bgwg


def dfs(G: bgwg.DiGraph) -> List[Any]:
    """Performs Depth-First Search algorithm on graph G starting from a random
    source BGW node.
    ----------------------------------------------------------------------------
    Args:
        G: directed acyclic graph. If G contains nodes the problem has been
           shown to have no solution
    Returns:
        sorting: list of ordered nodes in increasing order order based on their
        finish timestamp"""
    sorting = [] # list to containg topological sorting
    time = 0 # initialize timestamp


    def dfs_visit(node: bgwg.BGWNode, t0: int = 0) -> int:
        """Implements recursive function to visit all nodes reachable from a
        source BGW node. It updates their timestamp and their color accordingly.
        ------------------------------------------------------------------------
        Args:
            node: BGW node object to explore
            t0: initial timestamp prior to calling this fn
        Returns:
            time: timestamp after finishing this fn call"""
        time = t0 + 1 # a white node has just been discovered
        node.td = time
        node.set_color('gray')
        for child_key in G.get_adj(node):
            # retrive object associated to that key
            child_node = [child_key]['node']
            if child_node.get_color() == 'white': # explore this edge
               child_node.set_parent(node) 
               time = dfs_visit(child_node, time)
        
        node.set_color('black') # blacken node; it is finished
        time = time + 1
        node.tf = time
        sorting.append(node) # append blacked node to sorting list

        return time
    
    
    for node in G.get_nodes():
        if node.get_color() == 'white':
            dfs_visit(node)


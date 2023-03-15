# Topological Sort Algorithm Implementation

Implementation of the Topological Sort algorithm for directed acyclic graphs. The implementation defines its own abstract data types for nodes -`BGWNode`- and directed graphs -`DiGraph`- within `bgwgraph.py` file.
It is well known that NetworkX package is better suited for representing and processing graphs as it encompasses broader scenarios and algorithms than the ones presented here. However, this implementation is intended for academic purposes; specifically, to get a better insight at how the DFS (Depth-First Search) algorithm is used to produce a topological sorting of a directed acyclic graph. Any comments and suggestions are far more than welcome.

### What is a topological sorting of a directed acyclic graph (DAG)?
---
Just for those of you who are not familiar with the problem, a DAG is defined as a set of nodes and edges connecting those nodes that includes the notion of direction. For example, an edge from a node A to a node B is treated differently than its counterpart: an edge connecting node B to node A.

DAGs have plenty of applications in Computer Science (CS). The one we are focused in this project is to represent the precedence among events. For instance, consider the case of the following DAG representing the event of putting on a piece of clothing when dressing up in the morning:

![image](https://user-images.githubusercontent.com/95151624/225194059-798f354e-8567-42e6-92c3-2c0df8c8c049.png)

A directed edge from one node to another indicates that the first piece of clothing must be donned before the second one. A topological sorting of a DAG gives a linear ordering of the nodes such that for every directed edge connecting node A with node B, node A appears before B in the linear ordering. An possible ordering produced by a topological sorting for the previous DAG is the following:

![image](https://user-images.githubusercontent.com/95151624/225195096-5aa72b6a-18e7-408f-bd8f-a5fc79aad9d2.png)

This is easily interpreted as a possible ordering that one could follow to get dressed in the morning!

The topological sorting algorithm relies heavily on a well-known graph-based search algorithm: Depth-First Search (DFS) which is implemented inside `dfs.py` module. As we will see in the following testing section, we will get a slightly different but still logically valid response. This is because DFS algorithm and hence topological sorting depend on initial conditions.

### Adjacency list representation for our graph
---
We will assume that, speaking in high-level terms, the graph is encoded as an adjacency list, in contrast to an adjacency matrix. An adjacency list is simply a record of all nodes and all outgoing connections from them. You can see how this list looks for the test case in the next section!

### Running the project
---
When you are located at the project folder, simply run `python topo-sort.py` on your terminal and the output should be like the following:

![image](https://user-images.githubusercontent.com/95151624/225196515-ee95f5bc-c815-4bd6-af83-3fdb3f4e7cd4.png)

The sorting considers that "belt" node is the source node, speaking in DFS common jargon. Observe that the linear ordering displayed in terminal respects the precedence among the various garments. So now you have an ordering you can follow if you feel a bit confused in the morning or you simply want to try a different routine for getting dressed.

# standard library modules
from typing import Any, List, Tuple
from typing_extensions import Self


class BGWNode:
    """Black-Gray-White colored node."""

    def __init__(self, key: Any) -> Self:
        """Constructor method for BGWNode class. It initializes node to have
        WHITE as initial color value.
        ------------------------------------------------------------------------
        Args:
            key: any hashable id for the node"""
        # private instance attributes
        self.__color = 'white'
        self.__parent = None

        # public instance attributes
        self.key = key
        self.td = 0 # discovery timestamp
        self.tf = 0 # final timestamp


    # Public Methods

    def get_color(self):
        """Retrieve node's color.
        ---------------------------------------------------------------------"""
        return self.__color

    def set_color(self, new_color: str) -> bool:
        """Update node's color. The method verifies that the new_color attribute
        is exactly one of the following strings: 'white', 'gray', 'black'.
        ------------------------------------------------------------------------
        Args:
            new_color: proposed color for the instance node. Must agree with the
                       previous requirements
        Returns:
            bool: True if succesful, otherwise raises an exception"""
        if new_color in ['white', 'gray', 'black']:
            self.__color = new_color

        else:
            err_msg = "ValueError: invalid color value for .new_color attribute"
            raise Exception(err_msg)

        return True


    def get_parent(self) -> Self:
        """Retrieve node's parent.
        ---------------------------------------------------------------------"""
        return self.__parent

    def set_parent(self, new_parent: Self) -> bool:
        """Update node's parent. The method verifies that the new_parent
        attribute is a BGWNode instance.
        ------------------------------------------------------------------------
        Args:
            new_parent: proposed parent for the instance node. Must be an
                        instance of BGWNode
        Returns:
            bool: True if succesful, otherwise raises an exception"""
        if isinstance(new_parent, BGWNode):
           self.__parent = new_parent 

        else:
            err_msg = "ValueError: new_parent is not a BGWNode instance"
            raise Exception(err_msg)

        return True



class DiGraph:
    """Directed graph class definition. It may handle any arbitrary built-in or
    custom object. It is intented to be used for algorithms that require the
    BGWNode datatype."""

    def __init__(
            self, 
            nodes: List[Any] = [], 
            edges: List[Tuple[Any]] = []
            ) -> Self:
        """Class constructor. asdfasdfasdf description goes here
        ------------------------------------------------------------------------
        """
        # private instance attributes
        self.__type = BGWNode
        self.__n_edges = 0
        self.__n_nodes = 0

        # public instance attributes
        self.nodes = {} # dictionary for BWGNode objects
        self.adj = {}

        for node in nodes: # initialize keys and values 
            bgw_node = BGWNode(node) 
            self.nodes[node] = bgw_node
            self.adj[node] = [] # initialize adjacency list
            self.__n_nodes += 1 # increase number of nodes

        for edge in edges: # organize edges as an adjacency list
            if len(edge) != 2:
                err_msg = f"ValueError: {edge} edge must be a 2-tuple"

                raise Exception(err_msg)
            
            if type(edge) is not tuple:
                err_msg = f"TypeError: {edge} edge must be a 2-tuple"

                raise Exception(err_msg)

            # if edge meets previous criteria, add to adjacency list
            parent, child = edge
            if child not in self.adj[parent]:
                (self.adj[parent]).append(child) 
                self.__n_edges += 1 # increase number of edges 


    # Private Methods

    def __valid_adj(lst: List[Any] = []) -> bool:
        """Validate if a list lst is a valid adjacency list for the self.__type
        class operations.
        ------------------------------------------------------------------------
        Args:
            lst: Python list object
        Returns:
            bool: True if lst meets self.__type criteria, False otherwise"""
        is_list = isinstance(lst, list)
        is_empty = len(lst) == 0
        type_check = all(isinstance(n, self.__type) for n in lst) # check types

        return is_list and (is_empty or type_check)


    # Public Method

    def size_nodes(self) -> int:
        return self.__n_nodes

    def size_edges(self) -> int:
        return self.__n_edges

        return True

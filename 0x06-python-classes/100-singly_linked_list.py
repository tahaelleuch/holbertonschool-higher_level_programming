#!/usr/bin/python3


class Node:
    """Representation of a node"""

    def __init__(self, data, next_node=None):
        """initializes the l list
        Args:
            data (int): data
            next_node (Node): the next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """getter of data
        Return:
            data of the node
        """
        return self.__data

    @data.setter
    def data(self, value):
        """setter of data
        Args:
            value (int): data of the node
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """getter of next_node
        Returns:
           the next node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """setter of next_node
        Args:
            value (Node): next node in the linked list
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

    def __str__(self):
        """representation of Node instance
        Returns:
            The node
        """
        return str(self.__data)

class SinglyLinkedList:
    """Representation of a linked list"""
    def __init__(self):
        """Initialization of linked list
        """
        self.__head = None

    def sorted_insert(self, value):
        """insert new Node
        Args:
            value (int): data of the new node
        """
        new = Node(value)
        tmp = self.__head
        if tmp is None or tmp.data >= value:
            if tmp:
                new.next_node = tmp
            self.__head = new
            return
        while tmp.next_node is not None:
            if tmp.next_node.data >= value:
                break
            tmp = tmp.next_node
        new.next_node = tmp.next_node
        tmp.next_node = new

    def __str__(self):
        """representation of SinglyLinkedList instance
        Returns:
            The linked list
        """
        string = ""
        tmp = self.__head
        while tmp is not None:
            string += str(tmp)
            if tmp.next_node is not None:
                string += "\n"
            tmp = tmp.next_node
        return string

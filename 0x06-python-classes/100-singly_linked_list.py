#!/usr/bin/python3
"""Write a class Node that defines a node of a singly linked list"""


class Node():
    """ Class: Node """

    def __init__(self, data, next_node=None):
        """Initialize the Node object"""
        
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """return data"""
        return self.__data

    @data.setter
    def data(self, value):
        """evalue of the value of data"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """return next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """evalue of the value of next"""
        if value != None:
            raise TypeError("data must be an integer")
        self.__next_node = value

class SinglyLinkedList:
    """ Class: SinglyLinkedList """

    def __init__(self):
        self.head = None
    
    def sorted_insert(self, data):
        newNode = Node(data)
        if(self.head):
            current = self.head
            while(current.next_node):
                current = current.next_node
            current.next_node = newNode
        else:
            self.head = newNode 

    def my_print(self, data):
        current = self.head
        while(current.next_node):
            print("{:d}".format(current.data))
            current = current.next_node




'''Linked List Implementation in Python'''

'''Node of the linked list'''
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.root = None
    
    
    def add_node(self, val):
        new_node = Node(val)
        if self.root == None:
            self.root = new_node
        else:
            new_node.next = self.root
            self.root = new_node
            
    def delete_first_node(self):
        root = self.root
        self.root = self.root.next
        del root
    
    def print_list(self):
        root = self.root
        while(root):
            print(root.val, end = " ")
            root = root.next
        print()
    
if __name__ == '__main__':
    obj = LinkedList()
    for i in range(0, 9):
        obj.add_node(i)
    obj.print_list()
    obj.delete_first_node()
    obj.print_list()
    
    
    
    
    
    

# Author: Seda Tarverdyan | Copyright (c) 2024 | Use of this code requires keeping this copyright notice.
class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None

    def __repr__(self):
        return str(self.data)  


class SinglyLinkedList:
    def __init__(self, initial_data=None):
        self.head = None
        if initial_data is not None:
            for value in initial_data:
                self.insert_ending(value)

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)  
            node = node.next
        return str(nodes)  
    
    def traversal(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' ')
            current_node = current_node.next  
        print()  

    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head  
        self.head = new_node  

    def insert_ending(self, value):
        new_node = Node(value)
        if self.head is None:  
            self.head = new_node  
            return
        
        
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node  
    def adding_two_lists(self, second):
        result = SinglyLinkedList()
        carry = 0 #kam 0 kam 1
        node1 = self.head
        node2 = second.head
        while node1 is not None or node2 is not None or carry:
            value1 = node1.data if node1 else 0
            value2 = node2.data if node2 else 0
        
            total = value1 + value2 + carry
            carry = total // 10 #ete carryn 10ic mec a 1, ete che 0
            result.insert_ending(total % 10)
            #gnum e hajord nodery
            if node1 is not None:
                node1 = node1.next
            if node2 is not None:
                node2 = node2.next
        return result
    
l1 = SinglyLinkedList([2,4,3])

l2 = SinglyLinkedList([5,6,4])

result_list = l1.adding_two_lists(l2)
print(result_list)

l3 = SinglyLinkedList([9, 9, 9, 9, 9, 9, 9])

l4 = SinglyLinkedList([9, 9, 9, 9])
result_list1 = l3.adding_two_lists(l4)
print(result_list1)

# Array to Linked List

# Node Class Creation
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def arrayToList(self, arr):
        if not arr:
            return None
            
        head= Node(arr[0])
        current = head
        
        for i in arr[1:]:
            current.next = Node(i)
            current = current.next
        return head 
        
    def print_LinkedList(head):
        current = head
        while current:
            print(current.data, end= "->" if current.next else "\n")
            current = current.next
        
        
# Linked list insertion 

class Node:
    def __init__(self,data) :
        self.data = data
        self.next = None

        
              
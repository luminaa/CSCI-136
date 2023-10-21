"""
Practice problem

A) Create a singly linked list with the following values:

13 --> 11 --> 9 -->14 -->12 --> 8 -->6 -->7
B) Implement a function to split the linked list into two halves.
 
C) Implement the merge function to merge two sorted linked lists.
 
D) Implement the merge sort function for the linked list.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = None

    def append(self, data): #append to the end of linked list
        if self.head is None:
            self.head = Node(data)
            return
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)
    
    def print_list(self): #prints linked list to console
        current = self.head
        output = ""
        while current.next:
            output += str(current.data) + " --> "
            current = current.next
        output += str(current.data)
        print(output)

    def find_middle(self): #finds middle node of linked list
        slow = self.head
        fast = self.head
        while fast.next and fast.next.next: #fasr pointer moves twice as fast as slow pointer
            slow = slow.next
            fast = fast.next.next
        middle = slow.next
        return middle
    
    def split(self): #splits linked list into two halves, for uneven lists, first list is bigger by 1
        middle = self.find_middle()
        left = SinglyLinkedList()
        right = SinglyLinkedList()
        current = self.head
        while current != middle:
            left.append(current.data)
            current = current.next
        while current:
            right.append(current.data)
            current = current.next
        return left, right
    
    def merge(self, other):
        merged = SinglyLinkedList()
        left = self.head
        right = other.head
        while left and right:
            if left.data < right.data:
                merged.append(left.data)
                left = left.next
            else:
                merged.append(right.data)
                right = right.next
        while left:
            merged.append(left.data)
            left = left.next
        while right:
            merged.append(right.data)
            right = right.next
        return merged
    
    def merge_sort(self):
        if self.head.next is None:
            return self
        left, right = self.split()
        left = left.merge_sort()
        right = right.merge_sort()
        return left.merge(right)

linked_list = SinglyLinkedList()
nodes = [13, 11, 9, 14, 12, 8, 6]
for node in nodes:
    linked_list.append(node)

linked_list.print_list()
print("Middle Node:", linked_list.find_middle().data)

l,r = linked_list.split()
l.print_list()
r.print_list()

merged = l.merge(r)
merged.print_list()


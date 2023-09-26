'''
Question 5) Create a Circular Linked List with the following nodes:

'Howard University', 'University of Maryland',

'Johns Hopkins', 'George Mason University',

'Georgetown University', 'Catholic University'

Write functions to:

a) Insert a node at the end of the list

b) Delete a node from the list based on the value

c) Display the elements of the list from a given node.

d) Print out all the elements in the circular linked list
'''

class Node:
    def __init__(self,value=None,next=None):
        self.next = next
        self.value = value

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __str__(self):
        cur = self.head
        out = ''
        while cur:
            out += str(cur.value) + ' -> '
            cur = cur.next
            if cur == self.head:
                break
        return out[:-4]
    
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.head.next = self.head
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head
        self.size += 1

    def delete(self, value):
        cur = self.head
        prev = None
        while cur and cur.value != value:
            prev = cur
            cur = cur.next
            if cur == self.head:
                print("Value not found")
                return
        if prev == None:
            self.head = cur.next
        else:
            prev.next = cur.next
        self.size -= 1

    def display(self, value):
        cur = self.head
        string = ''
        while cur and cur.value != value:
            cur = cur.next
            if cur == self.head:
                return "Value not found"
        while cur:
            string += str(cur.value) + ' -> '
            cur = cur.next
            if cur == self.head:
                break
        return string[:-4]


unis = ['Howard University', 'University of Maryland', 'Johns Hopkins', 'George Mason University', 'Georgetown University', 'Catholic University']
universities = CircularLinkedList()

for uni in unis:
    universities.append(uni)

print("\nList of all Universities")
print(universities)
print("\nList of all Univeristies Statring from Johns Hopkins")
print(universities.display('Johns Hopkins'))
print(universities.delete('Howard University'))
print("\nList of all Univeristies after deleting Howard University")
print(universities)
class ListNode: 
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, data):
        if self.head is None:
            self.head = ListNode(data)
            return
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = ListNode(data)

    def insert(self, data, position):
        new_node = ListNode(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        else:
            current = self.head
            for i in range(position - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def delete(self, position):
        if position == 0:
            self.head = self.head.next
            return
        else:
            current = self.head
            for _ in range(position - 1):
                current = current.next
            current.next = current.next.next


    def print_list(self):
        current = self.head
        output = ""
        while current.next:
            output += current.val + " --> "
            current = current.next
        output += current.val
        print(output)


DC_metro = SinglyLinkedList()
DC_metro.append("Union Station")
DC_metro.append("Judiciary Square")
DC_metro.append("Gallery Place")
DC_metro.append("Farragut North")
DC_metro.append("Penn Station")

print("\nQuestion 1:")
DC_metro.print_list()

print("\nQuestion 2:")
DC_metro.insert("Metro Center", 3)
DC_metro.print_list()

print("\nQuestion 3:")
DC_metro.delete(5)
DC_metro.print_list()



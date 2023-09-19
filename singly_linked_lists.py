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

# node1 = ListNode(1)
# node2 = ListNode(2)
# node1.next = node2

# head = node1
# while head:
#     print(head.val)
#     head = head.next

weeks = SinglyLinkedList()
weeks.append("Mon")
weeks.append("Tue")
weeks.append("Wed")
weeks.append("Thu")
weeks.append("Fri")
weeks.append("Sat")
weeks.append("Sunday")

weeks.insert("RAHUALS DAY", 4)

weeks.print_list()

weeks.delete(4)

weeks.print_list()
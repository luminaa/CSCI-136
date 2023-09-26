# Question 1) write a python function that converts the strings above to their corresponding numbers

multiplier = {
    "hundred": 100,
    "thousand": 1000,
}
number_dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "ten": "10",
    "twenty": "20",
    "thirty": "30",
    "forty": "40",
    "fifty": "50",
    "sixty": "60",
    "seventy": "70",
    "eighty": "80",
    "ninety": "90",
}

def convert_string_to_number(number):
    numbers = number.lower().split(" ")
    n = 0
    for i in numbers:
        if i in number_dict:
            n += int(number_dict[i])
        elif i in multiplier:
            n *= multiplier[i]
    return n

string = ["One thousand", "fifty thousand", "three", "twenty thousand", "forty", "ten", "ten thousand"]
numbers = []
for i in string:
    number = convert_string_to_number(i)
    print(number)
    numbers.append(number)



# Question 2) Implement a stack using a linked list. The stack should have methods for push, pop, peek, is_empty, maximum, and minimum

class Node:
    def __init__(self,value=None,next=None):
        self.next = next
        self.value = value

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
        self.maxi = float("-inf")
        self.mini = float("inf")

    def __str__(self):
        cur = self.head
        out = ''
        while cur:
            out += str(cur.value) + ' -> '
            cur = cur.next
        return out[:-4]

    def push(self, value):
        if value > self.maxi:
            self.maxi = value
        if value < self.mini:
            self.mini = value
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def pop(self):
        if self.head.value == None:
            return None
        else:
            self.head = self.head.next
            self.size -= 1
    
    def peek(self):
        return self.head.value
    
    def maximum(self):
        return self.maxi
    
    def minimum(self):
        return self.mini

    def get_size(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0



# Question 3a) Insert the numbers from question 1 above to the stack

stack = Stack()

for i in numbers:
    stack.push(i)

print('\nInitial Stack')
print(stack)



# Question 3b) Print out the maximum and minimum values in the stack

print('\nMaximum value in stack')
print(stack.maximum())

print('\nMinimum value in stack')
print(stack.minimum())



# Question 4) What is the time complexity for the following methods: push, pop, peek, is_empty, maximum, and minimum

# push: O(1)
# pop: O(1)
# peek: O(1)
# is_empty: O(1)
# maximum: O(1)
# minimum: O(1)
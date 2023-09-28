'''
Question 1: Write a Python function named is_balanced that takes a string consisting of parentheses and determines whether the string contains a balanced set of parentheses. A string is balanced if the following conditions are satisfied:

Every open parenthesis has a corresponding closing parenthesis.The pairs of parentheses are properly nested.
The function should return True if the string is balanced, and False otherwise.

Here is an example of a balanced string: (()(())()) Here is an example of an unbalanced string: (()())(

Requirements:You are only allowed to use the list data structure to create the stack. Do not use any other Python libraries or data structures.
'''

def is_balanced(string):
    stack = [] # empty list as a stack
    for i in string:
        if i == "(": # if open parenthesis, push to stack
            stack.append(i)
        elif i == ")": # if close parenthesis, pop from stack
            if len(stack) == 0: # empty stack means unbalanced
                return False
            stack.pop()
    if len(stack) == 0: # empty stack means balanced
        return True
    else: # left over open parenthesis means unbalanced
        return False
    
print(is_balanced("(()()())"))
print(is_balanced("(()())("))



'''
Question 2) Implement a stack using a singly linked list in Python and use it to determine whether a given string of different types of brackets is balanced or not. The types of brackets you should check for are (), [], and {}.

Requirements:
Your implementation must use a singly linked list as the stack. Do not use Python's list or any other data structure or library.

Implement the following methods:

push(item): To add an item to the stack.pop(): To remove the item from the stack.is_empty(): To check if the stack is empty.
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self): 
        self.head = None

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.head is None:
            return None
        else:
            popped = self.head.data
            self.head = self.head.next
            return popped

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False
        
def is_balanced(string):
    stack = Stack() # Stack object initialized
    for i in string:
        if i == "(" or i == "[" or i == "{": # open parenthesis, push to stack
            stack.push(i)
        elif i == ")": # close parenthesis, pop from stack
            if stack.is_empty() or stack.pop() != "(": # if popped value is not open parenthesis or stack is empty, unbalanced
                return False
        elif i == "]": # close square bracket, pop from stack
            if stack.is_empty() or stack.pop() != "[": # if popped value is not open square bracket or stack is empty, unbalanced
                return False
        elif i == "}": # close curly bracket, pop from stack
            if stack.is_empty() or stack.pop() != "{": # if popped value is not open curly bracket or stack is empty, unbalanced
                return False
    if stack.is_empty(): # empty stack means balanced
        return True
    else: # left over open parenthesis means unbalanced
        return False
    
print(is_balanced("(()()())"))
print(is_balanced("(()())("))
print(is_balanced("(()[]{)"))
print(is_balanced("(()[]{})"))
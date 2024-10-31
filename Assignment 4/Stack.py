class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def isEmpty(self):
        return self.size == 0
    
    def push(self, value):
        if self.size == 0:
            n = Node(value, None)
            self.head = self.tail =  n
        else:
            n = Node(value, self.head)
            self.head = n
        self.size += 1
    
    def pull(self):
        if not self.head:
            return
        val = self.head.value
        self.head = self.head.next
        self.size -= 1
        return val

    def printLL(self):
        temp=self.head
        while temp!=None:
            print(" -> ",temp.value,end=" ")
            temp=temp.next
        print() 

text = input("Enter Text: ")
message = ""
s = Stack()
for i in text:
    if i.isalpha() or i == " ":
        s.push(i)
    elif i == "*":
        if not s.isEmpty():
            message += s.pull()
while not s.isEmpty():
    message += s.pull()
print(message)
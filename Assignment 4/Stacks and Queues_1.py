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

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def queue(self, value):
        n = Node(value, None)
        if self.size == 0:
            self.head = self.tail =  n
        else:
            n = Node(value, None)
            self.tail.next = n
            self.tail = n
        self.size += 1
    
    def dequeue(self):
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

s = Stack()
q = Queue()

text = input("Enter the text to check if it is palindrome: ")

odd = False

mid = len(text)//2
if len(text) % 2 == 1:
    odd = True
    m = text[mid]

for i in range(len(text)):
    if i < mid:
        q.queue(text[i])
    elif i == mid and odd:
        continue
    else:
        s.push(text[i])
# s.printLL()
# q.printLL()
temp1 = s.head
temp = q.head
isPalindromes = True
while temp1 and temp:
    a = s.pull().upper()
    b = q.dequeue().upper()
    # print(a,b)
    if a!=b:
        print("Not Palindromes")
        isPalindromes = False
        break
    temp1 = temp1.next
    temp = temp.next

print(isPalindromes)
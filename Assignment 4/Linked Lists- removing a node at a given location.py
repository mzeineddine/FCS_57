class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def addHead(self, value):
        if self.size == 0:
            n = Node(value, None)
            self.head = self.tail =  n
        else:
            n = Node(value, self.head)
            self.head = n
        self.size += 1
    
    def addTail(self, value):
        n = Node(value, None)
        if self.size == 0:
            self.head = self.tail =  n
        else:
            n = Node(value, None)
            self.tail.next = n
            self.tail = n
        self.size += 1
    
    def delHead(self):
        if not self.head:
            return
        self.head = self.head.next
        self.size -= 1

    def delTail(self):
        if not self.head:
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None
        self.tail = temp
        self.size -= 1
    
    def delValue(self, val):
        if not self.head:
            return
        
        elif not self.head.next:
            if self.head.value == val:
                self.delHead()
            else:
                return
            
        elif self.tail.value == val:
            self.delTail()

        elif self.head.value == val:
                self.delHead()

        else:
            temp = self.head
            temp1 = self.head.next
            while temp and temp1:
                if temp1.value == val:
                    temp.next = temp1.next
                    temp1 = None
                    break
                temp = temp.next
                temp1 = temp1.next

    def printLL(self):
        temp=self.head
        while temp!=None:
            print(" -> ",temp.value,end=" ")
            temp=temp.next
        print() 

ll = LinkedList()

ll.addHead(1)
ll.addHead(2)
ll.addHead(3)
ll.addHead(4)
ll.addHead(5)
ll.addHead(6)
ll.addHead(7)
ll.addHead(4)

ll.printLL()

ll.delValue(4)
ll.printLL()

# ll.delTail()
# ll.printLL()
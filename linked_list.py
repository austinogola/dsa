class Node(object):

    def __init__(self,data):
        self.data=data
        self.next=None

class SinglyLinkedList(object):

    def __init__(self):
        self.head=None
        self.size=0

    def addNode(self,data):
        newNode=Node(data)
        if self.head:
            newNode.next=self.head
            self.head=newNode
            self.size+=1
        else:
            self.head=newNode
            self.size+=1

    def removeFirst(self):
        self.head=self.head.next
        self.size-=1

    def showAll(self):
        curr=self.head
        while curr:
            print(curr.data)
            curr=curr.next

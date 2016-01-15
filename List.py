'''
Simple Implementation of a Single Linked List
'''


class Node:
    def __init__(self,data,next=None):
        self.next = next
        self.data = data

    def getValue(self):
        return self.data

    def setValue(self,value):
        self.data = value

    def getNext(self):
        return self.next

    def setNext(self,next):
        self.next = next

class List:

    def __init__(self):
        self.head = None
        self.size = 0

    def add(self,value):
        '''
        Insert Value at Head
        :param value:
        :return:
        '''
        node = Node(value,self.head)
        self.head = node
        self.size += 1

    def remove(self,value):

        # No item to remove
        if self.head == None:
            return

        # Value is the first item, remove from list
        if self.head.getValue() == value:
            self.head = self.head.getNext()
            self.size -= 1
            return

        currentNode = self.head.getNext()
        previousNode = self.head

        while currentNode != None and currentNode.getValue() != value:
            previousNode = currentNode
            currentNode = currentNode.getNext()

        if currentNode and currentNode.getValue() == value:
            previousNode.setNext(currentNode.getNext())
            self.size -= 1

    def reverse(self):
        '''
        Reverse the Linked List
        :return:
        '''

        if self.size == 0 or self.size == 1:
            return

        previous = None
        next = self.head

        while next:
            temp = next.getNext()
            next.setNext(previous)
            previous = next
            next = temp

        self.head = previous

    def __str__(self):
        values = []
        node = self.head
        while node:
            values.append(node.getValue())
            node = node.getNext()

        return str(values)

if __name__ == '__main__':
    l = List()
    print l
    l.add(1)
    l.add(2)
    l.add(3)

    print l

    l.reverse()

    print l

    l.remove(3)

    print l

    l.remove(3)

    print l

    l.remove(2)

    print l
'''
Simple Queue Class
'''

from collections import deque
class Queue:
    def __init__(self):
        '''
        Create Empty Queue
        '''

        # Empty List
        self.data = deque()

    def __len__(self):
        '''
        Returns the number of items on the queue
        :return: Int
        '''
        return len(self.data)

    def __str__(self):
        '''
        Get string representation of queue
        :return: String
        '''
        return str(self.data)

    def push(self,item):
        '''
        Put Item on top of stack
        :param item:
        '''
        self.data.append(item)

    def pop(self):
        '''
        Get First item from queue
        :return: Item
        '''
        return self.data.popleft()

    def peek(self):
        '''
        Preview oldest item in queue
        :return:
        '''
        return self.data[0]

    def clear(self):
        '''
        Clear entire stack
        :return:
        '''
        self.data = deque()

    def empty(self):
        '''
        Returns true if stack is empty
        :return: Boolean
        '''
        return len(self.data) == 0
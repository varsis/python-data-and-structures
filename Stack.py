'''
    A simple Stack Implementation for Python
'''

class Stack:
    def __init__(self):
        '''
        Create Empty stack
        '''

        # Empty List
        self.data = []

    def __len__(self):
        '''
        Returns the number of items on the stack
        :return: Int
        '''
        return len(self.data)

    def __str__(self):
        '''
        Get string representation of stack
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
        Get top item on stack and remove
        :return: Item
        '''

        return self.data.pop()

    def peek(self):
        '''
        Preview top item on stack
        :return:
        '''
        return self.data[-1]

    def clear(self):
        '''
        Clear entire stack
        :return:
        '''
        self.data = []

    def empty(self):
        '''
        Returns true if stack is empty
        :return: Boolean
        '''
        return len(self.data) == 0






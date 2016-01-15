
import unittest
from Stack import Stack



class StackTestCase(unittest.TestCase):
    def test_init(self):
        '''
        Test Init
        :return:
        '''
        s = Stack()
        self.assertNotEqual(None, s)

    def test_push_pop(self):
        '''
        Test Push Pop
        :return:
        '''
        s = Stack()
        s.push("One")

        self.assertEquals(False,s.empty())

        s.pop()

        self.assertEquals(True,s.empty())


    def test_len(self):
        '''
        Test Len
        :return:
        '''
        s = Stack()
        s.push("One")

        self.assertEquals(1,len(s))

    def test_str(self):
        '''
        Test Str
        :return:
        '''
        s = Stack()
        s.push("One")

        self.assertEquals("['One']",str(s))

        s.push("Two")
        self.assertEquals("['One', 'Two']",str(s))

    def test_peek(self):
        '''
        Test peek
        :return:
        '''
        s = Stack()
        s.push("One")

        self.assertEquals('One',s.peek())

        s.push("Two")
        self.assertEquals('Two',s.peek())


    def test_clear(self):
        '''
        Test peek
        :return:
        '''
        s = Stack()
        s.push("One")
        s.push("Two")
        self.assertEquals(False,s.empty())
        s.clear()
        self.assertEquals(True,s.empty())


if __name__ == '__main__':
    unittest.main()

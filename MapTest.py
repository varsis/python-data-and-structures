
import unittest
from Map import Map


class MyTestCase(unittest.TestCase):
    def test_init(self):
        m = Map()
        self.assertNotEqual(None,m)

    def test_addKey(self):
        m = Map()
        m['one'] = 1
        m['two'] = 2

        self.assertEquals(1,m['one'])
        self.assertEquals(2,m['two'])

        m['one'] = 2
        self.assertEquals(2,m['one'])

    def test_collision(self):
        m = Map(10)
        m[10] = 1
        m[0] = 2

        self.assertEquals(1,m[10])
        self.assertEquals(2,m[0])

if __name__ == '__main__':
    unittest.main()

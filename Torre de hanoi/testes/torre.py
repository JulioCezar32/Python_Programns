import unittest
from stack import *

class TestHanoiTower(unittest.TestCase):


    def setUp(self):
        self.stack_void = Stack(0)
        self.stack_one = Stack(1)
        self.stack_two = Stack(2)

    def test_receive_stone_void(self):
        stack = Stack(0)
        stack_structure = []
        self.assertEqual(stack.stone, stack_structure)

    def test_receive_stone_2(self):
        stack = Stack(2)
        stack_structure = [1,2]
        self.assertEqual(stack.stone, stack_structure)

    def test_receive_stone_3(self):
        stack = Stack(3)
        stack_structure = [1,2,3]
        self.assertEqual(stack.stone, stack_structure)

    def test_remove_stone_void(self):
            stack_structure = []
            self.assertEqual(self.stack_void.remove_stone(), 3)
            self.assertEqual(self.stack_void.stone, stack_structure)
            self.assertEqual(self.stack_void.remove_stone(),1)


    def test_receive_stone(self):
        self.assertEqual(self.stack_two.receive_stone(1),1)
        self.assertEqual(self.stack_void.receive_stone(1), 0)

if __name__ == '__main__':
    unittest.main()

"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Node, Stack


class TestNode(unittest.TestCase):

    def test_init(self):
        n1 = Node(5, 2)
        self.assertEqual(n1.data, 5)
        self.assertEqual(n1.next_node, 2)


class TestStack(unittest.TestCase):

    def test_pop(self):
        stack = Stack()
        stack.push("data1")
        self.assertEqual(stack.pop(), "data1")

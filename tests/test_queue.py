"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest
from src.queue import Node, Queue


class TestNode(unittest.TestCase):

    def test_init(self):
        n1 = Node(7)
        self.assertEqual(n1.data, 7)
        self.assertEqual(n1.next_node, None)


class TestQueue(unittest.TestCase):

    def test_enqueue(self):
        queue = Queue()
        queue.enqueue("data1")
        queue.enqueue("data2")
        self.assertEqual(queue.head.data, "data1")
        self.assertEqual(queue.tail.data, "data2")

    def test_str(self):
        queue = Queue()
        queue.enqueue("data1")
        queue.enqueue("data2")
        self.assertEqual(str(queue), "data1\ndata2")

    def test_dequeue(self):
        queue = Queue()
        queue.enqueue("data1")
        queue.enqueue("data2")
        self.assertEqual(queue.dequeue(), "data1")
        self.assertEqual(queue.dequeue(), "data2")
        self.assertEqual(queue.dequeue(), None)

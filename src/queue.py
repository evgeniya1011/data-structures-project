class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node

    def __repr__(self):
        return f"{self.__class__.__name__}({self.data}, {self.next_node})"


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        if self.head is None:
            return ""
        else:
            start = self.head
            result = ""
            while start is not None:
                result += start.data + "\n"
                start = start.next_node
            return result[:-1]

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        node = Node(data, None)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next_node = node
            self.tail = node

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        if self.head is not None:
            pop_item = self.head.data
            self.head = self.head.next_node
            return pop_item
        return None

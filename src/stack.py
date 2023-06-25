class Node:
    """Класс для узла стека"""

    def __init__(self, data: object, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node

    def __repr__(self):
        return f"{self.__class__.__name__}({self.data}, {self.next_node})"


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        self.top = None

    def __str__(self):
        return f"{self.top}"

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        if self.top is None:
            self.top = Node(data, None)
        else:
            self.top = Node(data, self.top)

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        if self.top is not None:
            pop_top = self.top.data
            self.top = self.top.next_node
            return pop_top
        else:
            return None

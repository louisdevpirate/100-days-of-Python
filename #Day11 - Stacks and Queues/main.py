from collections import deque


class Stack:
    """Une implémentation simple d'une pile (stack) utilisant une liste."""

    def __init__(self):
        """Initialise une nouvelle pile vide."""
        self.items = []

    def push(self, item):
        """Ajoute un élément au sommet de la pile."""
        self.items.append(item)

    def pop(self):
        """
        Retire et renvoie l'élément au sommet de la pile.
        Lève une IndexError si la pile est vide.
        """
        if self.is_empty():
            raise IndexError("La pile est vide")
        return self.items.pop()

    def peek(self):
        """
        Renvoie l'élément au sommet de la pile sans le retirer.
        Lève une IndexError si la pile est vide.
        """
        if self.is_empty():
            raise IndexError("La pile est vide")
        return self.items[-1]

    def is_empty(self):
        """Renvoie True si la pile est vide, False sinon."""
        return len(self.items) == 0

    def size(self):
        """Renvoie le nombre d'éléments dans la pile."""
        return len(self.items)


class Queue:
    """Une implémentation efficace d'une file (queue) utilisant collections.deque."""

    def __init__(self):
        """Initialise une nouvelle file vide."""
        self.items = deque()

    def enqueue(self, item):
        """Ajoute un élément à la fin de la file."""
        self.items.append(item)

    def dequeue(self):
        """
        Retire et renvoie l'élément au début de la file.
        Lève une IndexError si la file est vide.
        """
        if self.is_empty():
            raise IndexError("La file est vide")
        return self.items.popleft()

    def front(self):
        """
        Renvoie l'élément au début de la file sans le retirer.
        Lève une IndexError si la file est vide.
        """
        if self.is_empty():
            raise IndexError("La file est vide")
        return self.items[0]

    def is_empty(self):
        """Renvoie True si la file est vide, False sinon."""
        return len(self.items) == 0

    def size(self):
        """Renvoie le nombre d'éléments dans la file."""
        return len(self.items)


# Tests unitaires
import unittest


class TestStack(unittest.TestCase):
    def test_stack_operations(self):
        s = Stack()
        self.assertTrue(s.is_empty())
        s.push(1)
        s.push(2)
        self.assertEqual(s.size(), 2)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.peek(), 1)
        self.assertEqual(s.pop(), 1)
        self.assertTrue(s.is_empty())
        with self.assertRaises(IndexError):
            s.pop()


class TestQueue(unittest.TestCase):
    def test_queue_operations(self):
        q = Queue()
        self.assertTrue(q.is_empty())
        q.enqueue(1)
        q.enqueue(2)
        self.assertEqual(q.size(), 2)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.front(), 2)
        self.assertEqual(q.dequeue(), 2)
        self.assertTrue(q.is_empty())
        with self.assertRaises(IndexError):
            q.dequeue()


if __name__ == "__main__":
    unittest.main()
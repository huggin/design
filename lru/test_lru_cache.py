import unittest
from lru_cache import Cache


class TestHashTable(unittest.TestCase):
    def test1(self):
        table = Cache(2)
        table.set(1, "haha")
        self.assertEqual(table.get(1), "haha")

    def test2(self):
        table = Cache(2)
        table.set(1, 2)
        table.set(2, 3)
        table.set(1, 5)
        table.set(4, 5)
        table.set(6, 7)
        self.assertEqual(table.get(4), 5)
        table.set(1, 2)
        self.assertIsNone(table.get(3))

    def test3(self):
        pass

if __name__ == '__main__':
    unittest.main()

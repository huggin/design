import unittest
from hash_table import HashTable

class TestHashTable(unittest.TestCase):
    def test_get(self):
        self.table = HashTable(100)
        self.table.set(1, 100)
        self.assertEqual(self.table.get(1), 100)
        with self.assertRaises(KeyError):
            self.table.get(2)

    def test_set(self):
        self.table = HashTable(100)
        self.table.set(2, 200)
        self.table.set(2, 300)
        self.assertEqual(self.table.get(2), 300)

    def test_remove(self):
        self.table = HashTable(100)
        self.table.set(3, 500)
        self.table.set(103, 400)
        with self.assertRaises(KeyError):
            self.table.get(4)
        self.table.remove(3)
        with self.assertRaises(KeyError):
            self.table.get(3)
        self.table.get(103)

if __name__ == '__main__':
    unittest.main()

class Item(object):
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value

class HashTable(object):
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def _hash_function(self, key):
        return key % self.size

    def set(self, key, value):
        idx = self._hash_function(key)
        for item in self.table[idx]:
            if item.key == key:
                item.value = value
                return
        self.table[idx].append(Item(key, value))

    def get(self, key):
        idx = self._hash_function(key)
        for item in self.table[idx]:
            if item.key == key:
                return item.value
        raise KeyError('Key not found')

    def remove(self, key):
        idx = self._hash_function(key)
        for i, item in enumerate(self.table[idx]):
            if item.key == key:
                del self.table[idx][i]
                return
        raise KeyError('Key not found')

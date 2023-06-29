class Node(object):
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class LinkedList(object):
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def move_to_front(self, node):
        if node.next:
            node.next.prev = node.prev
        if node.prev:
            node.prev.next = node.next
        self.append_to_front(node)

    def append_to_front(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def remove_from_tail(self):
        if self.tail is None:
            return
        self.tail = self.tail.prev
        self.tail.next = None

class Cache(object):
    def __init__(self, max_sz) -> None:
        self.max_size = max_sz
        self.size = 0
        self.lookup = {}
        self.list = LinkedList()

    def set(self, key, val):
        node = self.lookup.get(key)
        if node:
            node.val = val
            self.list.append_to_front(node)
        else:
            if self.size == self.max_size:
                self.lookup.pop(key, None)
                self.list.remove_from_tail()
            else:
                self.size += 1

            new_node = Node(val)
            self.list.append_to_front(new_node)
            self.lookup[key] = new_node

    def get(self, key):
        node = self.lookup.get(key)
        if node is None:
            return None
        self.list.move_to_front(node)
        return node.val
        


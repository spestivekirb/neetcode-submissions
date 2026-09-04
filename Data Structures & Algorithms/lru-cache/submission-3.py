class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keyHash = {}
        self.ldummy = Node(0, 0)
        self.rdummy = Node(0, 0)

        self.ldummy.next = self.rdummy
        self.rdummy.prev = self.ldummy




    def get(self, key: int) -> int:

        if key in self.keyHash:
            node = self.keyHash[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            
            self.rdummy.prev.next = node
            node.prev = self.rdummy.prev
            node.next = self.rdummy
            self.rdummy.prev = node
            return node.val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        node = None
        if key in self.keyHash:
            # Remove from dll
            node = self.keyHash[key]
            node.prev.next = node.next
            node.next.prev = node.prev

            node.val = value
        else:
            if len(self.keyHash) >= self.capacity:
                node = self.ldummy.next
                node.prev.next = node.next
                node.next.prev = node.prev
                self.keyHash.pop(node.key)
            else:
                node = Node(0, 0)

            node.key = key
            node.val = value
        
        node.prev = self.rdummy.prev
        self.rdummy.prev.next = node
        node.next = self.rdummy
        self.rdummy.prev = node
        self.keyHash[key] = node

    





class LRUCache:

    class Node:

        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    # @param capacity, an integer
    def __init__(self, capacity):
        # write your code here
        self.capacity = capacity
        self.dict = {}
        self.head, self.tail = self.Node('head','head'), self.Node('tail','tail')
        self.head.next = self.tail
        self.tail.prev = self.head



    # @return an integer
    def get(self, key):
        # write your code here
        if key not in self.dict:
            return -1
        else:
            self.insertNodeAtFirst(self.unlinkNode(self.dict[key]))
            return self.dict[key].value
    def set(self, key, value):
        if key in self.dict:
            self.insertNodeAtFirst(self.unlinkNode(self.dict[key]))
            self.dict[key].value = value
        else:
            if len(self.dict) >= self.capacity:
                del self.dict[self.unlinkNode(self.tail.prev).key]
            self.dict[key] = self.Node(key,value)
            self.insertNodeAtFirst(self.dict[key])
        
    # @param key, an integer
    # @param value, an integer
    # @return nothing


    def insertNodeAtFirst(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def unlinkNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None
        return node



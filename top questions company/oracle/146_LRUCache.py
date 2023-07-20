class Node(): 
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
            
class LRUCache():

    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {}
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
    
    def insert(self,node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt,prev
    
    def remove(self,node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt,prev
        
    def get(self, key):
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1
    
    def put(self,key,value):
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
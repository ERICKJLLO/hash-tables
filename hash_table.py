class HashTable:
    def __init__(self, size = 10 ):
        self.size = size
        self.value = [] * self.size
        self.key = [] * self.size

    def _hash(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
       pass 
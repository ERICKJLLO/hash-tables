class HashTable:
    def __init__(self, size = 10 ):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash_knuth(self, key):
        constante_aurea = 0.6180339887
        return int(self.size * ((hash(key) * constante_aurea) % 1))
    
    def _hash_xor(self, key):
        hash_value = 0
        for char in str(key):
            hash_value ^= (hash_value << 5) + (hash_value >>2) + ord(char)
        return hash_value % self.size
    
    def _hash_personalizada(self, key):
        hash_value = sum(ord(char) for char in str(key))
        return (hash_value * 31) % self.size
    
    def _hash(self, key, metodo):
        if metodo == "knuth":
            return self._hash_knuth(key)
        elif metodo == "xor":
            return self._hash_xor(key)
        elif metodo == "personalizada":
            return self._hash_personalizada(key)


    def insert(self, key, value):
       pass
    def search(self, key):
        pass
    def delete(key):
        pass
    def __str__():
        pass

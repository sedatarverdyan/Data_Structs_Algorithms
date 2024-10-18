# Author: Seda Tarverdyan | Copyright (c) 2024 | Use of this code requires keeping this copyright notice.
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * self.size

    def index(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        i = self.index(key)
        self.table[i] = (key, value)

    def get(self, key):
        i = self.index(key)
        if self.table[i] and self.table[i][0] == key:
            return self.table[i][1]
        return None
    def delete(self, key):
        
        i = self.index(key)
        if self.table[i] and self.table[i][0] == key:
            self.table[i] = None  
            return True
        return False
h1 = HashTable()
h1.insert("name", "Seda")
h1.insert("name", "Ani")  #կգրի "Seda"ի վրա քանի որ նույն ինդեքսն է
print(h1.get("name"))  
h1.delete("name")
print(h1.get("name")) 
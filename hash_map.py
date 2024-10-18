# Author: Seda Tarverdyan | Copyright (c) 2024 | Use of this code requires keeping this copyright notice.
class HashMap:
    def __init__(self, size=10):
        self.size = size
        self.map = [[] for _ in range(size)]  

    def index(self, key):
        return hash(key) % self.size  

    def insert(self, key, value):
        i = self.index(key)
        for pair in self.map[i]:  
            if pair[0] == key:
                pair[1] = value  
                return
        self.map[i].append([key, value])  

    def get(self, key):
        i = self.index(key)
        for pair in self.map[i]:
            if pair[0] == key:
                return pair[1]
        return None  

    def delete(self, key):
        i = self.index(key)
        for pair in self.map[i]:
            if pair[0] == key:
                self.map[i].remove(pair)  
                return True
        return False  


hm = HashMap()
hm.insert("age", "20")
hm.insert("age", "21") #կփոխարինի արժեքը նույն ինդեքսի համար
print(hm.get("age"))  
hm.delete("age")
print(hm.get("age"))  

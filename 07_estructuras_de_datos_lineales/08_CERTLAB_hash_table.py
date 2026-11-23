class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, string):
        total = 0
        for char in string:
            total += ord(char)
        return total

    def add(self, key, value):
        code_key = self.hash(key)
        if code_key not in self.collection:
            self.collection[code_key] = {}
        self.collection[code_key][key] = value
        
    def remove(self, key):
        code_key = self.hash(key)
        if code_key in self.collection and key in self.collection[code_key]:
            del self.collection[code_key][key]
            if not self.collection[code_key]:
                del self.collection[code_key]

    def lookup(self, key):
        code_key = self.hash(key)
        if code_key in self.collection and key in self.collection[code_key]:
            return self.collection[code_key][key]
        return None

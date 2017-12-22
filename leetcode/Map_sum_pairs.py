class MapSum:
    def __init__(self):
        self.data = {}

    def insert(self, key, val):
        self.data[key] = val

    def sum(self, prefix):
        sum = 0
        for each in self.data:
            if each[0:len(prefix)] == prefix:
                sum += self.data[each]
        return sum

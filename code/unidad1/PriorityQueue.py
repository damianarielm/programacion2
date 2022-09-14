class PriorityQueue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def insert(self, item):
        self.items.append(item)
    def remove(self):
        item = max(self.items)
        self.items.remove(item)
        return item

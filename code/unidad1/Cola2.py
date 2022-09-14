class ImprovedQueue:
    def __init__(self): self.length, self.head, self.last = 0, None, None
    def isEmpty(self): return self.length == 0
    def insert(self, cargo):
        node = Node(cargo)
        if self.length == 0: # if list is empty
            self.head = self.last = node # the new node is head and last
        else:
            last = self.last # find the last node
            last.next = self.last = node # append the new node
        self.length = self.length + 1
    def remove(self):
        cargo = self.head.cargo
        self.head, self.length = self.head.next, self.length - 1
        if self.length == 0: self.last = None
        return cargo

class Queue:
    def __init__(self): self.length, self.head = 0, None
    def isEmpty(self): return self.length == 0
    def insert(self, cargo):
        node = Node(cargo)
        if self.head == None: # if list is empty the new node goes first
            self.head = node
        else: # find the last node in the list
            last = self.head
            while last.next: last = last.next
            last.next = node # append the new node
        self.length = self.length + 1
    def remove(self):
        cargo = self.head.cargo
        self.head = self.head.next
        self.length = self.length - 1
        return cargo

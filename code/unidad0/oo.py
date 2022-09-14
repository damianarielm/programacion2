class MyList():
    def __init__(self, any_list):
        self.any_list = any_list

    def square(self):
        return [ x * x for x in self.any_list ]

    def doble(self):
        return [ 2 * x for x in self.square() ]

    def sum(self):
        return sum(self.doble())

    my_list = MyList([1, 2, 3, 4, 5])

print(my_list.sum())

class ExtendedStack(list):
    def __init__(self, list_numbers):
        self.list = list_numbers

    def sum(self):
            self.list.append(self.list.pop() + self.list.pop())  # операция сложения

    def sub(self):
            self.list.append(self.list.pop() - self.list.pop())  # операция вычитания

    def mul(self):
            self.list.append(self.list.pop() * self.list.pop())  # операция умножения

    def div(self):
            self.list.append(self.list.pop() // self.list.pop())  # операция целочисленного деления


extendstack = ExtendedStack([1, 2, 3, 4, 5, 6, 7, 8])

extendstack.sum()
extendstack.sub()



print(extendstack.list)
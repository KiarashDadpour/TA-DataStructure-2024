class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.S = [0] * max_size  
        self.num = 0

    def push(self, item):
        if self.num >= self.max_size:
            raise Exception("OverFlow")  
        self.S[self.num] = item
        self.num += 1

    def pop(self):
        if self.num <= 0:
            raise Exception("Empty")  
        item = self.S[self.num - 1]
        self.num -= 1
        return item

    def is_empty(self):
        if self.num == 0:
            return True
        else:
            return False

    def is_full(self):
        if self.num >= self.max_size:
            return True
        else:
            return False

    def top(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            return self.S[self.num - 1]

    def display(self):
        if self.is_empty():
            return "Stack is empty"
        while not self.is_empty():
            print(self.pop())




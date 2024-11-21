class Stack:
    def __init__(self, max_size):
        self.max_size = max_size  
        self.S = [0] * max_size  
        self.num = 0  
    
    def push(self, item):
        if self.num >= self.max_size:
            raise Exception("Stack overflow")
        self.S[self.num] = item
        self.num += 1
        
    def pop(self):
        if self.num == 0:
            raise Exception("Stack empty")
        self.num -= 1
        return self.S[self.num]
    
    def top(self):
        if self.num == 0:
            raise Exception("Stack empty")
        return self.S[self.num-1]

    
    def size(self):
        return self.num
    
    def is_full(self):
        return self.num >= self.max_size
    
    def is_empty(self):
        return self.num == 0

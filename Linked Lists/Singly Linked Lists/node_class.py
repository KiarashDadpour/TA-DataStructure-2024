class Node:

    def __init__(self, info, next=None):
        self.info = info
        self.next = next

    def get_info(self):
        return self.info

    def set_info(self, value):
        self.info = value

    def get_next(self):
        return self.next

    def set_next(self, ptr):
        self.next = ptr

    def __str__(self):
        return str(self.info)
      

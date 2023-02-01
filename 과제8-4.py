class Stack:
    def __init__(self):
        self.lst = []

    def empty(self):
        if len(self.lst) == 0:
            return True
        else:
            return False

    def top(self):
        if self.lst == []:
            return None
        else:
            return self.lst[-1]

    def pop(self):
        if self.lst == []:
                return None
        else:
            return self.lst.pop()
            
    def push(self, k):
        self.lst.append(k)

    def __repr__(self):
        return self.lst

x = Stack()
print(x.lst)
print(x.empty())
x.lst.append(1)
print(x.lst)
print(x.pop())
print(x.push(2))
print(x.__repr__())

class Stack:
    def __init__(self):
        self.items = []
        
    def push(self,data):
        self.items.append(data)
        
    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            print("Empty stack")
            return -1
        
    def pop(self):
        if not self.isEmpty():
            return self.items.pop(0)
        else:
            print("Empty stack")
            return -1
        
    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def value(self):
        return self.items

    def bomb(self):
        self.temp = []
        for i in self.items:
            if int(i)%2 == 0:
                self.temp.append(int(i)-1)
            else:
                self.temp.append(int(i)+2)
        self.items = self.temp

def stackCheck(stack):
    S = Stack()
    if len(stack) == 0:
        return '0'
    else:
        tamp = int(stack[len(stack)-1]) 
        S.push(tamp)
        for i in range(len(stack)-2,-1,-1):
            if int(stack[i]) > tamp:
                tamp = int(stack[i])
                S.push(tamp)
        return S.size()
            
S = Stack()
inp = input('Enter Input : ').split(',')
for i in inp:
    l = i.split()
    if l[0] == 'A':
        S.push(l[1])
    elif l[0] == 'B':
        print(stackCheck(S.value()))
    elif l[0] == 'S':
        S.bomb()
        
# 65010536 นันทิพัฒน์ มั่งศิริ
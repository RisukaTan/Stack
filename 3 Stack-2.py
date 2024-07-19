class Stack:
  def __init__(self):
    self.stack = []

  def pop(self):
    return self.stack.pop() if not self.is_empty() else None

  def push(self, item):
    return self.stack.append(item)
 
  def peek(self):
    return self.stack[-1] if not self.is_empty() else None

  def is_empty(self):
    return self.stack == []

  def size(self):
    return len(self.stack)

  def __str__(self):
     if not self.is_empty():
            return str(self.stack)
     else:
        None
  
P = Stack()
F = Stack()
n = 0
x = []
y = []
inp = input("Enter Input : ").split(',')
for i in range(len(inp)):
   a,b = inp[i].split(" ")
   x.append(int(a))
   y.append(int(b))

for j in range(len(inp)):
   if n > 0 :
      for k in range(P.size()):
         if int(x[j]) > int(P.peek()):
            P.pop()
            print(F.pop())
         else:
            break
      P.push(x[j])
      F.push(y[j])
      n = n + 1
   else :
      P.push(x[j])
      F.push(y[j])
      n = n + 1

# 65010536 นันทิพัฒน์ มั่งศิริ
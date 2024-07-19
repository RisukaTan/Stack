class Stack():

    def __init__(self, ls = None):
        self.stack = []

    def push(self,i):
        self.stack.append(i)

    def pop(self):
        return self.stack.pop() if not self.isEmpty() else None

    def isEmpty(self):
        return self.stack == []

    def size(self):
        return len(self.stack)

def postFixeval(st):

    s = Stack()
    for i in st:
      try:
          s.push(int(i))
      
      except ValueError:
          val1 = s.pop()
          val2 = s.pop()
          if i == '/':
              s.push(val2 / val1)
          else: 
              switcher = {'+': val2 + val1, '-': val2 - val1, '*': val2 * val1, '^': val2**val1}
              s.push(switcher.get(i))
    return s.pop()

            


print(" ***Postfix expression calcuation***")

token = list(input("Enter Postfix expression : ").split())



print("Answer : ",'{:.2f}'.format(postFixeval(token)))
# 65010536 นันทิพัฒน์ มั่งศิริ
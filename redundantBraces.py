class Solution:
  # @param A : string
  # @return an integer
  def braces(self, A):
    if (self.isRedundant(A) == True):
      return 1
    else:
      return 0
    
  def isRedundant(self, exp):
    st = Stack()
    for ch in exp:
      if(ch == ')'):
        top = st.top()
        st.pop()
        flag = True
        while(top != '(' ):
          if (top == '+' or top == '-' or top == '*' or top == '/'):
            flag = False
          top = st.top()
          st.pop()
        if(flag == True):
          return True
      else:
        st.push(ch) 
    
    return False


class Stack():
  def __init__(self):
    self.items = []

  def push(self,item):
    self.items.append(item)

  def pop(self):
    self.items.pop()
    
  def top(self):
    return self.items[-1]
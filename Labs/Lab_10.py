#Number 1
class LinkedStack:
  def __init__(self):
    self.data = DoublyLinkedList()
  def __len__(self):
    return len(self.data)
  def is_empty(self):
    return len(self)==0
  def push(self, e):
    self.data.add_last(e)
  def pop(self):
    is self.is_empty():
      raise Exception("Stack is empty")
     return self.data.delete_last()
  def top(self):
    if self.is_empty():
      raise Exception("Stack is Empty!")
     return self.data.trailer.prev.data
  
 #Number 2
def __getitem__(self, i):
  if 0 <= ind <= len(self)//2:
    start = self.header.next
    for i in range(ind):
      start = start.next
      
     return start.data
  elif len(self)//2 <ind<len(self):
    start = self.trailer.prev
    for i in range(len(self)-1, ind, -1):
      start = start.prev
      
     return start.data
  else:
    raise IndexError("Index out of range!")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

#version 1
def remove_all(lst, value):
    i = 0
    while i < len(lst):
        if lst[i] == value:
            temp = lst[i]
            lst[i] = lst[len(lst) - 1]
            lst[len(lst)-1] = temp
            lst.pop()            
        else:
            i += 1
    return lst
  
  # version 2
  
  def remove_all(lst,elem):
    elemcounter=0
    for i in range(len(lst)):
        if lst[i]==elem:
            elemcounter+=1
        else:
            lst[i-elemcounter]=lst[i]
    for i in range(elemcounter):
        lst.pop()

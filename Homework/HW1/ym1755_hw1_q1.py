

def shift(lst, k, direction = 'left'):
  #Creating conditional flow, the two conditions being a direction either left or right
  if direction == 'left':
  # I am going to repeat for the amount of times k
    for i in range(k):
      first_one = lst[0]     # My first number in this range will be stored in the variable first_one  
    # im going to use the index at j, j being a number in the range of how big my list is(minus one).
      for j in range(len(lst)-1):
        lst[j] = lst[j+1] #Shift that value by 1.    
      # the last value of this lst will now be the first_value I extracted in the range(k)
      lst[-1] = first_one
    # Else, I have my other condition which is if I have the direction set to 'right'
  else:
  # get a value k number of times, iterate k times
    for i in range(k):
      first_one = lst[-1] # im going to take my last element in my lst k and store it for first one. This will be repeated k number of times.  
  # Im going to take the numbers and move them to the right
      for j in range(len(lst)-1, 0, -1):
        lst[j] = lst[j-1]
      lst[0] = first_one

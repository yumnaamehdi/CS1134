'''Implement a function
def factors(num)
integer num, and returns a generator, that when iterated over, it will have all of

for curr_factor in factors(100):
  print(curr_factor)
  
 The expected output is:
1 2 4 5 10 20 25 50 100
  Implementation requirement: Pay attention to the running time of your
  implementation. The for loop like the above, should run in a total cost of Θ1√𝑛𝑢𝑚4.'''

def factors(num):
    for n in range(1, int(num**0.5)+1):
        if num % n == 0:
            yield n
    for n in range(int(num**0.5)-1, 0, -1):
        if num % n == 0:
            yield num//n

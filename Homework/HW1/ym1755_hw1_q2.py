
n = 10
def sum_of_squares(n):
    sum = 0
    for i in range(1, n):
        sum += i * i
    return sum
    
#part b
sum([i*i for i in range(1,n)])

#part c
def sum_of_odd(n):
    sum = 0
    for i in range(1,n):
        if i%2!=0:
            sum += (i*i)
    return sum

#part d
sum([i*i for i in range(1,n) if i%2!=0])

'''Implement the function def e_approx(n). T
his function is given a positive integer n, 
and returns an approximation of e, calculated by 
the sum of the first (n+1) addends of the infinite sum above.'''


def e_approx(n):
    sum_a = 1
    prev_factorial = 1
    for i in range(1,n+1):
        prev_factorial*=i
        sum_a += ((1)/(prev_factorial))
    return sum_a

def main():
    for n in range(15):
        curr_approx = e_approx(n)
        approx_str = "{:.15f}".format(curr_approx)
        print("n =", n, "Approximation:", curr_approx)

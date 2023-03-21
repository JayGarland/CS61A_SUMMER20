from ucb import trace

@trace
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)

def path(m, n):
    #first above is base cases
    if m == 1 or n == 1:
        return 1
    return path(m -1, n) + path(m, n -1)

def knap(n, k):
    if n == 0:
       return k == 0

    with_last = knap(n//10, k-n % 10)
    without_last = knap(n//10, k)
    return with_last or without_last

def all_nums(k):
    def h(k, prefix):
        if k == 0:
            print(prefix)
            return
        h(k- 1, prefix* 10)
        h(k- 1, prefix* 10+ 1)
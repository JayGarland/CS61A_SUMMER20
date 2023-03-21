this_file = __file__


def make_adder_inc(a):
    """
    >>> adder1 = make_adder_inc(5)
    >>> adder2 = make_adder_inc(6)
    >>> adder1(2)
    7
    >>> adder1(2) # 5 + 2 + 1
    8
    >>> adder1(10) # 5 + 10 + 2
    17
    >>> [adder1(x) for x in [1, 2, 3]]
    [9, 11, 13]
    >>> adder2(5)
    11
    """
    "*** YOUR CODE HERE ***"
    step = 0
    def add_helper(b):
        nonlocal step
        step += 1
        return a + b +step -1
    return add_helper

def make_fib():
    """Returns a function that returns the next Fibonacci number
    every time it is called.

    >>> fib = make_fib()
    >>> fib()
    0
    >>> fib()
    1
    >>> fib()
    1
    >>> fib()
    2
    >>> fib()
    3
    >>> fib2 = make_fib()
    >>> fib() + sum([fib2() for _ in range(5)])
    12
    >>> from construct_check import check
    >>> # Do not use lists in your implementation
    >>> check(this_file, 'make_fib', ['List'])
    True
    """
    "*** YOUR CODE HERE ***"
    flag, a = 0, 1
    def fib_helper():
        nonlocal flag, a
        # flag += 1
        # if flag == 1:
        #     return 0
        # else:
        #     return fib_helper(a-1)+fib_helper(a-2)
        flag, a = a, flag+ a
        return flag
    return fib_helper

def insert_items(lst, entry, elem):
    """
    >>> test_lst = [1, 5, 8, 5, 2, 3]
    >>> new_lst = insert_items(test_lst, 5, 7)
    >>> new_lst
    [1, 5, 7, 8, 5, 7, 2, 3]
    >>> large_lst = [1, 4, 8]
    >>> large_lst2 = insert_items(large_lst, 4, 4)
    >>> large_lst2
    [1, 4, 4, 8]
    >>> large_lst3 = insert_items(large_lst2, 4, 6)
    >>> large_lst3
    [1, 4, 6, 4, 6, 8]
    >>> large_lst3 is large_lst
    True
    """
    "*** YOUR CODE HERE ***"
    # initial_list = lst
    # def inserthelper():
    #     nonlocal initial_list
    #     return [initial_list.insert(n, elem) for n in initial_list if entry ==initial_list[n]]
    # return inserthelper
    n = 0
    while n < len(lst):
        if lst[n] == entry:
            lst.insert(n + 1, elem)
            if elem == entry:
                n += 1
        n += 1
    return lst 
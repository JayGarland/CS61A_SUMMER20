class Link:
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest
    
    def __repr__(self):
        if self.rest:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(repr(self.first), rest_str)

    def __str__(self) -> str:
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest 
        return string + str(self.first) + '>'


#str() is used to describe the object to the end user while repr() is mainly used for debugging and development
#the print() function calls the str() function of the object

def sum_nums(lnk):
    if lnk == Link.empty:
        return 0
    return lnk.first + sum_nums(lnk.rest)
    # sum = 0
    # while lnk.rest is not Link.empty:
    #         sum += lnk.first
    #         lnk = lnk.rest
    # sum += lnk.first
    # return sum

def multiply_lnks(lst_of_lnks):
    product = 1
    for everylnk in lst_of_lnks:
        if everylnk.rest == Link.empty:
            return Link.empty # if so then just keep fixed state info
        product *= everylnk.first
    lst_of_lnks_rests = [everylnk.rest for everylnk in lst_of_lnks] #moving the flags
    return Link(product, multiply_lnks(lst_of_lnks_rests))
    # my problem is it can't make sure every one in lst_of_lnks to move themselfves flag all, but we can create the same type of object to do recursion
    #For our base case, if we detect that any of the lists in the list of Links is empty, we can return the empty linked list as we’re not going to multiply anything.


    # GenagratedLnk = Link(1)
    # first = 1
    # for everylnk in lst_of_lnks:
    #     while everylnk.rest is not Link.empty:
    #         first *= everylnk.first
    #         GenagratedLnk = Link(first, multiply_lnks(GenagratedLnk))
    #         everylnk = everylnk.rest
    # return GenagratedLnk
            
def filter_link(link, f):
    while link != Link.empty:# move the flag to which link not empty, it's one more step further
        if f(link.first) == True:
            yield link.first
        link = link.rest
    
def filter_no_iter(link, f):
    if link != Link.empty:
        return 
    elif f(link.first) == True:
        yield link.first
    return filter_no_iter(link.rest, f)

class Tree:
    def __init__(self, label, branches=[]) -> None:
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label 
        self.branches = branches 

    def is_leaf(self):
        return not self.branches 

# we can mutate a tree using attribute assignment 

def make_even(t):
    """
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
    >>> make_even(t)
    >>> t.label
    2
    >>> t.branches[0].branches[0].label
    4
    """
    if t.label %2 != 0:
        t.label += 1 
    for b in t.branches:
        make_even(b) 
    # if t.is_leaf and t.label %2 != 0:
    #     t.label += 1
    # else:
    #     for branch in t.branches:
    #         if branch.label %2 !=0:
    #             branch.label += 1
    #     make_even(branch)
        
    # if t.label %2 != 0:
    #     t.label += 1

    # while not t.is_leaf:
    #     for branch in t.branches:
    #         if branch.label % 2 != 0:
    #             branch.label += 1
    #     make_even(branch)

def square_tree(t):
    if Tree:
        t.label **= 2
    for b in t.branches:
        square_tree(b)

def find_path(t, entry):
    if t.label == entry:
        return [t.label]
    for b in t.branches:
        path = find_path(b, entry)
        if path:
            return [t.label] + path

def average(t):
    def sum_helper(t):
        total, count = t.label, 1
        for b in t.branches:
            # total += sum_helper(b)
            # count += sum_helper(b) can't sum up the function dude
            b_total, b_count = sum_helper(b)
            total += b_total
            b_count += b_count
            return total, count 
    total, count = sum_helper(t) #assign the return value 
    return total / count 

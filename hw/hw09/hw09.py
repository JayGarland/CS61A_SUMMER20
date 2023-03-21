SOURCE_FILE = __file__



def in_order_traversal(t):
    """
    Generator function that generates an "in-order" traversal, in which we
    yield the value of every node in order from left to right, assuming that each node has either 0 or 2 branches.

    For example, take the following tree t:
            1
        2       3
    4     5
         6  7

    We have the in-order-traversal 4, 2, 6, 5, 7, 1, 3

    >>> t = Tree(1, [Tree(2, [Tree(4), Tree(5, [Tree(6), Tree(7)])]), Tree(3)])
    >>> list(in_order_traversal(t))
    [4, 2, 6, 5, 7, 1, 3]
    """
    "*** YOUR CODE HERE ***"
    ans = []
    if t.is_leaf():
        ans.append(t.label)
        return ans #return the label of leaves    
    ans.extend(in_order_traversal(t.branches[0])) #selector that return left child node
    ans.append(t.label)#parent
    ans.extend(in_order_traversal(t.branches[1]))#sibling
    return ans
    




def summation(n, term):
    """Return the sum of the first n terms of a sequence.

    >>> summation(5, lambda x: pow(x, 3))
    225
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total

def interleaved_sum(n, odd_term, even_term):
    """Compute the sum odd_term(1) + even_term(2) + odd_term(3) + ..., up
    to n.

    >>> # 1 + 2^2 + 3 + 4^2 + 5
    ... interleaved_sum(5, lambda x: x, lambda x: x*x)
    29
    >>> from construct_check import check
    >>> check(SOURCE_FILE, 'interleaved_sum', ['While', 'For', 'Mod']) # ban loops and %
    True
    """
    "*** YOUR CODE HERE ***"
    def helper(k, flag):
        if k > n:
            return 0
        if flag == 1:
            return even_term(k) + helper(k + 1, flag -1)
        else:
            return odd_term(k) + helper(k + 1, flag +1)
    return helper(0, 1)


    #another sulotion for this kind question but been banned for this one since no %
    # result = 0
    # def helper(n, odd_term, even_term):
    #     nonlocal result
    #     if n == 0:
    #         return result
    #     elif n % 2 == 0:
    #         result = result + even_term(n)
    #         return helper(n-1, odd_term, even_term)
    #     else:
    #         result = result + odd_term(n)
    #         return helper(n-1, odd_term, even_term)
    # return helper(n, odd_term, even_term)
    

def mutate_reverse(link):
    """Mutates the Link so that its elements are reversed.

    >>> link = Link(1)
    >>> mutate_reverse(link)
    >>> link
    Link(1)

    >>> link = Link(1, Link(2, Link(3)))
    >>> mutate_reverse(link)
    >>> link
    Link(3, Link(2, Link(1)))
    """
    "*** YOUR CODE HERE ***"
    #notice scheme tail recursion reverse is not the same as in python
    value = [] #use a stack to store, an intermedia
    ptr = link
    while ptr is not Link.empty:
        value.append(ptr.first)
        ptr = ptr.rest 
        #transfer all into value

    while link is not Link.empty:
        link.first = value.pop() #pop means pop the last element in stack
        link = link.rest

class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def map(self, fn):
        """
        Apply a function `fn` to each node in the tree and mutate the tree.

        >>> t1 = Tree(1)
        >>> t1.map(lambda x: x + 2)
        >>> t1.map(lambda x : x * 4)
        >>> t1.label
        12
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> t2.map(lambda x: x * x)
        >>> t2
        Tree(9, [Tree(4, [Tree(25)]), Tree(16)])
        """
        self.label = fn(self.label)
        for b in self.branches:
            b.map(fn)

    def __contains__(self, e):
        """
        Determine whether an element exists in the tree.

        >>> t1 = Tree(1)
        >>> 1 in t1
        True
        >>> 8 in t1
        False
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> 6 in t2
        False
        >>> 5 in t2
        True
        """
        if self.label == e:
            return True
        for b in self.branches:
            if e in b:
                return True
        return False

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()


class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'


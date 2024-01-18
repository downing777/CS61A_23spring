def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches.
    Trees have branches, which are trees themselves: this is why trees are recursive data structures."""
    return [label] + list(branches)


def label(tree):
    """Return the label value of a tree."""
    return tree[0]


def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]


def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)


#t = tree(1, [tree(2), tree(4)])
#print(branches(tree(5, [t, tree(3)]))[0][0])


def height(t):
    """Return the height of a tree.

    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    >>> t = tree(3, [tree(1), tree(2, [tree(5, [tree(6)]), tree(1)])])
    >>> height(t)
    3
    """
    "*** YOUR CODE HERE ***"
    if is_leaf(t):
        return 0
    else:
        return 1 + max([height(i) for i in branches(t)])


t = tree(3, [tree(1), tree(2, [tree(5, [tree(6)]), tree(1)])])
print(t)


def max_path_sum(t):
    """Return the maximum path sum of the tree.

    >>> t = tree(1, [tree(5, [tree(1), tree(3)]), tree(10)])
    >>> max_path_sum(t)
    11
    """
    "*** YOUR CODE HERE ***"
    if is_leaf(t):
        return label(t)
    else:
        return label(t) + max([max_path_sum(i) for i in branches(t)])


def find_path(t, x):
    """
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10)  # returns None
    """
    if label(t) == x:
        return [label(t)]
    for i in branches(t):
        path = find_path(i, x)
        if path:
            return [label(t)] + path


t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
print(find_path(t, 5))

print(find_path(tree(3), 5))
# if the situation we meet is not considered in the progremme, the default value is none

def sum_tree(t):
    """
    Add all elements in a tree.
    >>> t = tree(4, [tree(2, [tree(3)]), tree(6)])
    >>> sum_tree(t)
    15
    """
    "*** YOUR CODE HERE ***"
    if is_leaf(t):
        return label(t)
    else:
        return label(t) + sum([sum_tree(i) for i in branches(t)])


def balanced(t):
    """
    Checks if each branch has same sum of all elements and
    if each branch is balanced.
    >>> t = tree(1, [tree(3), tree(1, [tree(2)]), tree(1, [tree(1), tree(1)])])
    >>> balanced(t)
    True
    >>> t = tree(1, [t, tree(1)])
    >>> balanced(t)
    False
    >>> t = tree(1, [tree(4), tree(1, [tree(2), tree(1)]), tree(1, [tree(3)])])
    >>> balanced(t)
    False
    """
    "*** YOUR CODE HERE ***"
    if is_leaf(t):
        return True
    flag = (len(set([sum_tree(i) for i in branches(t)])) == 1)  # take away: set returns all unique elements in python list
    if not flag:
        return flag
    else:
        for i in branches(t):
            flag = flag & balanced(i)
    return flag


def balanced_new(t):
    for b in branches(t):
        if sum_tree(branches(t)[0]) != sum_tree(b) or not balanced(b): # any of the two True, return false
            return False
    return True

# if is leaf, no iteration will be operated


def sprout_leaves(t, leaves):
    """Sprout new leaves containing the data in leaves at each leaf in
    the original tree t and return the resulting tree.

    >>> t1 = tree(1, [tree(2), tree(3)])
    >>> print_tree(t1)
    1
      2
      3
    >>> new1 = sprout_leaves(t1, [4, 5])
    >>> print_tree(new1)
    1
      2
        4
        5
      3
        4
        5

    >>> t2 = tree(1, [tree(2, [tree(3)])])
    >>> print_tree(t2)
    1
      2
        3
    >>> new2 = sprout_leaves(t2, [6, 1, 2])
    >>> print_tree(new2)
    1
      2
        3
          6
          1
          2
    """
    "*** YOUR CODE HERE ***"
    if is_leaf(t):
        return t + [tree(i) for i in leaves]
    else:
        return tree(label(t), [sprout_leaves(i, leaves) for i in branches(t)])


def print_tree(t):
    def helper(i, t):
        print("    " * i + str(label(t)))
        for b in branches(t):
            helper(i + 1, b)
    helper(0, t)

def hailstone_tree(n, h):
    """Generates a tree of hailstone numbers that will reach N, with height H.
    >>> print_tree(hailstone_tree(1, 0))
    1
    >>> print_tree(hailstone_tree(1, 4))
    1
        2
            4
                8
                    16
    >>> print_tree(hailstone_tree(8, 3))
    8
        16
            32
                64
            5
                10
    """
    if h == 0:
        return tree(n)
    branches = [hailstone_tree(2 * n, h - 1)]
    if (n - 1) % 3 == 0 and n > 4 and (n - 1) % 2 != 0:
        branches += [hailstone_tree((n - 1) // 3, h - 1)]
    return tree(n, branches)


print_tree(hailstone_tree(8, 3))
print_tree(hailstone_tree(1, 4))
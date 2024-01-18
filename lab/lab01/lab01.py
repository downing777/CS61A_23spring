def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    assert k >= 0
    prod = 1
    if k == 0:
        return prod
    else:
        for i in range(k):
            prod = prod * (n-i)
        return prod

def divisible_by_k(n, k):
    """
    >>> a = divisible_by_k(10, 2)  # 2, 4, 6, 8, and 10 are divisible by 2
    2
    4
    6
    8
    10
    >>> a
    5
    >>> b = divisible_by_k(3, 1)  # 1, 2, and 3 are divisible by 1
    1
    2
    3
    >>> b
    3
    >>> c = divisible_by_k(6, 7)  # There are no integers up to 6 divisible by 7
    >>> c
    0
    """
    "*** YOUR CODE HERE ***"
    count= 0
    for i in range(1,n+1):
        if i % k == 0:
            print(i)
            count += 1
    return count


def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    last = y % 10
    all_but_last  = y // 10
    sum = last
    while all_but_last >0:
        last  = all_but_last % 10
        sum += last
        all_but_last = all_but_last // 10
    return sum


def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    flag = False
    dig_first = n % 10
    dig_second = (n // 10) % 10 
    all_last = n // 100

    while not flag :
        if all_last == 0:
            if dig_first == dig_second & dig_first == 8:
                flag = True
            else:
                break
        else:
            if dig_first == dig_second & dig_first == 8: 
                flag = True
        dig_first = dig_second
        dig_second = all_last % 10
        all_last  = all_last // 10
    return flag
print(double_eights(12345))

    

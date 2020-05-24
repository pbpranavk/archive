def inc(x):
  return x + 1

def test_increment():
    assert inc(3) == 4



def factorial(n):
    """
    >>> factorial(5)
    120
    >>> factorial(-23)
    'Wrong input'
    """
    fact = n
    if(n == 0):
        return 1
    else:
        if n>0:
            return fact*factorial(n-1)
        else:
            return "Wrong input"

if __name__ == '__main__':
    import doctest
    doctest.testmod()

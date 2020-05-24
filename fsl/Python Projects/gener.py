# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


a = my_gen()

#>>> # We can iterate through the items using next().
next(a)
#This is printed first
#1
 # Once the function yields, the function is paused and the control is transferred to the caller.

 # Local variables and theirs states are remembered between successive calls.
 next(a)
#This is printed second
#2

 next(a)
#This is printed at last
#3

 # Finally, when the function terminates, StopIteration is raised automatically on further calls.
next(a)
#Traceback (most recent call last):
#...
#StopIteration
 next(a)
#Traceback (most recent call last):
#...
#StopIteration

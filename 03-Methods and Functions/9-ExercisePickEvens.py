'''Define a function called myfunc that takes in an arbitrary number
of arguments, and return the sum of those arguments.'''

def myfunc(*args):
 return [n for n in args if n%2 == 0]

print(myfunc(1,2,3,4,5,6,7,8,9,10))
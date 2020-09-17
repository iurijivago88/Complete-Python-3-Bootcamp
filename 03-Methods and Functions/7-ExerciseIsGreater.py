''' Define a function called is_greater that takes in two arguments, and returns TRUE if the first value is greater
than the second, FALSE if it is less than or equal to the second.'''

def is_greater(a,b):
    if a > b:
        return True
    else:
        return False

print(is_greater(3,6))
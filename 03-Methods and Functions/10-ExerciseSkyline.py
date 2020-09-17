'''' Define a function called 'myfunc' that takes in a string, and returns a matching 
string where every even letter is uppercase, and every odd letter is lowercase.'''

def myfunc(st):
    res = []
    for index, c in enumerate(st):
        if index % 2 == 0:
            res.append(c.upper())
        else:
            res.append(c.lower())
    print(res)
    return ''.join(res)

myfunc('iurijivagoleaodasilva')
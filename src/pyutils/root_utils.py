
def nvl(a,b):
    if a is None:
        return b

    if isinstance(a, str) and a == '':
        return b
    return a

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print ("%s == %s" %(key, value))

def print_args(*argv):
    count = 0
    for arg in argv:
        print("arg[" + str(count) + "]:", arg)

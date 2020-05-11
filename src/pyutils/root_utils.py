
def nvl(a,b):
    if a is None:
        return b

    if isinstance(a, str) and a == '':
        return b
    return a

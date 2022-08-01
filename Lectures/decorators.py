# spread functionality of func without code changing

def logged_func(func):
    def inner(x, y):
        print(f'called with {x}, {y}')
        result = func(x, y)
        print(f'result: {result}')
        return result
    return inner


@logged_func               # --> decorator mark
def complicated(x, y):     # --> coplicated has been decorated by logged_func
    return x / y

print(complicated(6,3))
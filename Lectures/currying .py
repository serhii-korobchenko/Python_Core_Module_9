# Tranclate multiargument func in multitude funcs with one argument
def sum_func(x, y):
    return x + y


def sub_func(x, y):
    return x - y


OPERATIONS = {
    '-': sub_func,
    '+': sum_func
}


def get_handler(operator):       # get operator
    return OPERATIONS[operator]  # call funcs through OPERATIONS dict 


handler = get_handler('-')     #        1st step -- assign func to verb
print(handler(2, 3))           # -1     2nd step -- call verb as func with additional args

print(get_handler('+')(2, 3))  # 5
# Func in ver
def func(x, y):
      return x + y

func_alias = func
result = func_alias(2, 3)
print(result)  # 5

# nested func

def sum_func(x, y):
    return x + y

def subtraction_func(x, y):
    return x - y

def tricky_func(x, y, func):
    return func(x, y)

sum_result = tricky_func(2, 3, sum_func)
min_result = tricky_func(2, 3, subtraction_func)

print(sum_result)  # 5
print(min_result)  # -1

# return func from func
def sum_func(x, y):
      return x + y

def subtraction_func(x, y):
      return x - y

def get_operator(operator):
    if operator == '+':
        return sum_func
    elif operator == '-':
        return subtraction_func
    else:
        print('Unknown operator')

sum_action_function = get_operator("+")
print(sum_action_function(2, 3))    # 5

sub_action_function = get_operator("-")
print(sub_action_function(2, 3))    # -1
SOME_VAR = 3


def func(x):
    SOME_VAR = x
    print(SOME_VAR)


def procedure():
    print(SOME_VAR)


procedure()     # 3
func(5)         # 5
print(SOME_VAR) # 3
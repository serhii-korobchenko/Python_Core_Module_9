def adder(val):
    def inner(x):
        return x + val
    return inner


two_adder = adder(2) #               |     val ---> x (2) - only first time
print(two_adder(3)) # 5          <---^     val = 3, but x = 2  ---> 5
print(two_adder(5)) # 7      <---|         val = 5, but x = 2  ---> 7

three_adder = adder(3) #                   val ---> x (3) - only first time
print(three_adder(5))   # 8                val = 5, but x = 3  ---> 8
print(three_adder(-3))  # 0                val = -3, but x = 3  ---> 0

print(id(two_adder) == id(three_adder))   # False
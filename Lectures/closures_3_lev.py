# closure with 3 levels
def adder(val):
    def inner(x):
        def superinner(y):
            return x + val + y
        return superinner
    return inner


#two_adder = adder(2) #               |     
print(adder(2)(3)(4)) # 9          <---^     val = 2,  x = 3, y = 4  ---> 9
print(adder(2)(5)(3)) # 10      <---|         val = 2, x = 5, y = 3  ---> 10

three_adder = adder(3) #                   
print(three_adder(5))   # 8                
print(three_adder(-3))  # 0                

print(id(two_adder) == id(three_adder))   # False
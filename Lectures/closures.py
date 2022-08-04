# closure with 2 levels
def adder(val):
    def inner(x):
        
        return x + val 
       
    return inner


two_adder = adder(2) #               |     
print(two_adder(3)) # 5         <---^     val = 2,  x = 3  ---> 5
print(two_adder(5)) # 7     <---|         val = 2, x = 5  ---> 7

three_adder = adder(3) #                   
print(three_adder(5))   # 8                
print(three_adder(-3))  # 0                

print(id(two_adder) == id(three_adder))   # False
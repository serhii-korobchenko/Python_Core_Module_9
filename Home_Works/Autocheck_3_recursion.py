cache = {'0': 0,
         '1': 1}
def caching_fibonacci():


    def fibonacci(n):


        if n == 0:
            return 0 # base case
        elif n <= 1:
            return 1 # base case
        else:
            if str(n-1) not in cache:
                result = fibonacci(n-1) + fibonacci(n-2) #recursive case
            else:
                result = cache[str(n-1)] + cache[str(n-2)]
            
            
            
            cache[str(n)] = result

        return result

    return fibonacci 


print(caching_fibonacci()(10))

for i in cache.values():
    print(i, end= " ")





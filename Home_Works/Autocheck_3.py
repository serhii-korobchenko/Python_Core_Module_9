#Task:
# Inputs: dict - cache; 

cache = {'0': 0,
         '1': 1}
def caching_fibonacci():
    
    def fibonacci(n):
        for i in range (2, n):
            cache[str(i)] = cache[str(i-1)]+cache[str(i-2)]

        return cache[str(i)]
        
    return fibonacci 




print(caching_fibonacci()(10))

print(cache.values())




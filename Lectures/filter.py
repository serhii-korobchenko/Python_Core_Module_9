# filter - generator - only for 1 argument - check condition (Truth/False) - output: when Truthy
for i in filter(lambda x: x % 2, range(1, 10+1)):
    print(i)
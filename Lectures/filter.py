# filter - generator - only for 1 argument - check condition (Truth/False) - output: when Truthy
for i in filter(lambda x: x % 2, range(1, 10+1)): # Filter only odd values
    print(i)

some_str = 'aaAbbB C F DDd EEe'
for i in filter(lambda x: x.islower(), some_str): # Filter only small letter values
    print(i)
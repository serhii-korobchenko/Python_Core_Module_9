lambda_res = lambda a, b: a+b#  option #1
print(lambda_res(2,3))

print((lambda a, b: a+b)(2,6))# option #2

for i in range (1,10):        # option #3
    print((lambda a, b: a/b)(i,2))
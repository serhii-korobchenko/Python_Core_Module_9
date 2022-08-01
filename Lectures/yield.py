#  class 'generator'
# stop and continue of func proccesing from certain places (enterance points) --- yield using instead return
def interval_generator(x, y):
    while x <= y:
        yield x
        x += 1


five_to_ten_generator = interval_generator(5, 10) # 1st call

print(type(five_to_ten_generator))

for i in five_to_ten_generator:
    print(i)
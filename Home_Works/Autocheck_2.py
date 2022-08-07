
from datetime import datetime

start = datetime.now().microsecond
DEFAULT_DISCOUNT = 0.05
Dima = {"name": "Dima"}
Boris = {"name": "Boris", "discount": 0.15}
Serhii = {"name": "Serhii", "discount": 0.20}

def get_discount_price_customer(price, customer):
    
    if 'discount' in customer:
        discount = customer['discount']
    else:
        discount = DEFAULT_DISCOUNT

    price = price * (1 - discount)

    return price

print(get_discount_price_customer(1000, Serhii))
print(datetime.now().microsecond - start)


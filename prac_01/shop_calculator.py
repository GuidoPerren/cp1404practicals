number_of_items = int(input('Number of Items: '))
while number_of_items <= 0:
    print("Invalid number of items!")
    number_of_items = int(input('Number of Items: '))


total_price = 0
for i in range(0, number_of_items):
    item_price = float(input('Price of item: '))
    if item_price > 0:
        total_price += item_price

if total_price > 100:
    total_price = total_price * 0.90

print(f"Total price for {number_of_items} items is ${total_price:.2f}")


"""
CP1404/CP5632 - Practical
shop calculator
"""
total_price = 0
number_of_items = int(input("Number of items: "))
while number_of_items <= 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
for i in range(number_of_items):
    item_price = float(input("Price of item: "))
    total_price += item_price
if total_price > 100:
    discount_price = total_price * 0.1
    total_price = total_price - discount_price
print(f"Total price for {number_of_items} items is ${total_price:.2f}")

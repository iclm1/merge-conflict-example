gift_value = int(input("Value of gift: "))

if gift_value <= 5000:
    print("No tax!")
else:
    if 5000 < gift_value <= 25000:
        amount_of_tax = 100 + (gift_value - 5000) * 0.08
    elif 25000 < gift_value <= 55000:
        amount_of_tax = 1700 + (gift_value - 25000) * 0.1
    elif 55000 < gift_value <= 200000:
        amount_of_tax = 4700 + (gift_value - 55000) * 0.12
    elif 200000 < gift_value < 1000000:
        amount_of_tax = 22100 + (gift_value - 200000) * 0.15
    elif gift_value >= 1000000:
        amount_of_tax = 142100 + (gift_value - 1000000) * 0.17
    
if amount_of_tax > 0:
    print(f"Amount of tax: {amount_of_tax}")
else:
    print("No tax!")
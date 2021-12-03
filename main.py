# Part 1

# 1 Setting variables & arrays

b5: int = 5
b10: int = 10
b20: int = 20
b50: int = 50
b100: int = 100
b200: int = 200
b500: int = 500

total_price = 0

next_command = True

menu = []
dish_price = []
command = []

note_amount = ""

# Data filling
for i in range(3):
    dish = input("Enter a dish in the menu: ")
    price = int(input("Please, enter the price for " + dish + ": "))

    menu.append(dish)
    dish_price.append(price)

# Show menu to user

dict_menu = dict(zip(menu, dish_price))
print(dict_menu)

# Command
while next_command:
    order = input("What do you want to eat?: ")
    if order in menu:
        command.append(order)
    else:
        print("We don't have that dish!")

    print(command)

    end = input("Finished ordering? (1= Y / 0= N): ")

    if end == "1":
        next_command = False
    else:
        next_command = True

# Payment
for dishes in command:
    i = 0
    for item in menu:
        if dishes == item:
            total_price += dish_price[i]
        i += 1

print(f'Bill: {total_price}€')

while total_price > 0:
    if total_price >= b500:
        num = int(total_price // b500)
        total_price = round(total_price % b500, 2)
        note_amount += f'{num} 500 euro banknotes. '
    if total_price >= b200:
        num = int(total_price // b200)
        total_price = round(total_price % b200, 2)
        note_amount += f'{num} 200 euro banknotes. '
    if total_price >= b100:
        num = int(total_price // b100)
        total_price = round(total_price % b100, 2)
        note_amount += f'{num} 100 euro banknotes. '
    if total_price >= b50:
        num = int(total_price // b50)
        total_price = round(total_price % b50, 2)
        note_amount += f'{num} 50 euro banknotes. '
    if total_price >= b20:
        num = int(total_price // b20)
        total_price = round(total_price % b20, 2)
        note_amount += f'{num} 20 euro banknotes. '
    if total_price >= b10:
        num = int(total_price // b10)
        total_price = round(total_price % b10, 2)
        note_amount += f'{num} 10 euro banknotes. '
    if total_price >= b5:
        num = int(total_price // b5)
        total_price = round(total_price % b5, 2)
        note_amount += f'{num} 5 euro banknotes. '

print(note_amount)

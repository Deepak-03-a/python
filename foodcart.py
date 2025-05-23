# foodcart program

menu = {"pizza": 300,
        "nachos": 450,
        "popcorn": 600,
        "fries": 250,
        "chips": 100,
        "sandwich": 350,
        "soda": 300,
        "softdrinks": 425}
cart = []
total = 0

print("--------- MENU ---------")
for key, value in menu.items():
    print(f"{key:10}: Rs.{value:.2f}")
print("------------------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("------ YOUR ORDER ------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Total is: Rs.{total:.2f}")


weight = float(input("Enter your weight: "))
units = input("Enter Kilograms or pounds? (K or L): ")

if units == "K":
    weight = weight * 2.54
    units = "lbs."
    print(f"Your weight is: {round(weight, 2)} {units}")
elif units == "L":
    weight = weight / 2.54
    units = "kg's."
    print(f"Your weight is: {round(weight, 2)} {units}")
else:
    print(f"{units} is not valid.")



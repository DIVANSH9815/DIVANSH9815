# weight = float(input("enter your weight"))
# unit = input("kelogram / pounds (K / L)")

# if weight == "k":
#     weight = weight * 2.205
#     unit = "KLG"
#     print(f"your weight is {weight} {unit}")
# elif weight == "L":
#     weight == weight / 2.205
#     unit = "klg"
#     print(f"your weight is {weight} {unit}")
# else:
#     print(f"{unit} was not valid ")
    
weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds (K/L): ").strip().upper()

if unit == "K":
    weight = weight * 2.205
    unit = "lbs"
    print(f"Your weight is {weight:.2f} {unit}")
elif unit == "L":
    weight = weight / 2.205
    unit = "kg"
    print(f"Your weight is {weight:.2f} {unit}")
else:
    print(f"{unit} is not a valid unit.")

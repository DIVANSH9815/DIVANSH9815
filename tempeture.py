unit = input("is this tempeture in celcuis or fareahnite (F/C): ")
temp = float(input("enter your temp: "))

if unit == "f":
    temp = round((9 * temp) / 5 + 32 , 1)
    print(f"this is a tempreture in faranhnite {temp}")
elif unit == "c":
    temp = round((temp - 32) * 5 / 9,1)
    print(f"this is a tempreture in celcuis {temp}")
else:
    print(f"this a invalid value {temp}!")
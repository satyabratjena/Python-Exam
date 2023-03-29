

print("Main menu")
print("1. Covert Celcius to Fahrenheit(C)")
print("2. Convert Fahrenheit to Celcius")

coversion = int(input("Enter the choice: "))
temp = float(input("Enter the temperature: "))

if coversion == 1:
    convert_temp_c = (temp * 1.8) + 32
    print(f"{temp} in degree Celcius is {convert_temp_c} in degree Fahrenheit")
elif coversion == 2:
    convert_temp_f = (temp - 32) * 0.55
    print(f"{temp} in degree Fahrenheit is {convert_temp_f} in degree celcius")

else:
    ("Invalid input")


# farenhit_to_celcius = (temp*1.8)+32
# print("Temperature in farenheit is:", farenhit_to_celcius)




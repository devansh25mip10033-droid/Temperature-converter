print("Temperature Convereter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")
print("4. Kelvin to Celsius")
print("5. Fahrenheit to Kelvin")
print("6. Kelvin to Fahrenheit")

choice = input ("Enter your choice (1-6):")

temp = float(input("Enter the temperature value:"))

if choice == '1':
    result = (temp * 9/5) + 32
    print("Temperature in fahrenheit:", result)
elif choice == '2':
    result = (temp - 32) * 5/9
    print("Temperature in celsius:",result)   
elif choice == '3':
    result = temp + 273.15
    print("Temperature in Kelvin:", result) 
elif choice == '5':
    result = (temp - 32) * 5/9 + 273.15
    print("Temperature in kelvin:", result)     
elif choice == '6':
    result = (temp - 273.15) * 9/5 + 32
    print("Temperature in fahrenheit:", result)
else:
    print("Invalid choice! Please select between 1 and 6.") 

temp1 = float(input("Enter the first temperature in Celsius: "))

if temp1 >= 30:
    print("The temperature is hot. Wear light clothing.")
elif temp1 >= 20:
    print("The temperature is warm. A light jacket or shirt is recommended.")
else:
    print("The temperature is cool. A sweater is recommended.")
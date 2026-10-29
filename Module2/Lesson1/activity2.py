unit = float(input ("Enter the number of electricity units consumed: "))

if unit > 50:
    amount = unit * 2.6
    surcharge = 25
elif unit >= 100:
    unit = unit - 50
    amount = (50 * 2.6) + (unit * 3.25)
    surcharge = 35
elif unit >= 200:
    unit = unit - 100
    amount = (50 * 2.6) + (50 * 3.25) + (unit * 5.26)
    surcharge = 45
else:
    unit = unit -200
    amount = (50 * 2.6) + (50 * 3.25) + (100 * 5.26) + (unit * 8.45)
    surcharge = 75

total = amount + surcharge
print("\nThe total electricity bill is: %.2f " % total)
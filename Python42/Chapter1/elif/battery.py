battery = int(input("Enter battery percentage: "))

if battery <= 10:
    print("Battery very low")
elif battery <= 30:
    print("Battery low")
elif battery <= 70:
    print("Battery normal")
elif battery <= 100:
    print("Battery Full")
payment = input("Enter payment method: ")

if payment == "cash":
    print("Pay by cash")
elif payment == "upi":
    print("Scan QR code")
elif payment == "card":
    print("Swipe your card")
elif payment == "online":
    print("Pay online")
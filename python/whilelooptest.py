pin = int(input("Enter PIN: "))
while pin != 5431:
    pin = input("Wrong PIN. Enter your PIN: ")
if pin == 5431:
    print("Access granted!")

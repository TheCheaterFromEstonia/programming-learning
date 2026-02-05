#the first line triggers at the start
pin = int(input("Enter PIN: "))
#If the correct PIN is entered, the loop will stop, exiting the program. Though if the wrong PIN is entered, the loop will trigger line 5, prompting me to input again.
while pin != 5431:
    pin = int(input("Wrong PIN. Enter your PIN: "))
    


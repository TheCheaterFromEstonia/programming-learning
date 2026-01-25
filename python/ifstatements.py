#if statements allow for basic decision-making
age = int(input("How old are you?: "))
if age >= 18:
    print("You are an adult.")
    
elif age <= 0: 
    print("You arent born yet.")

else:
    print("You are underage.")
guess = 0
tries = 0

while guess != 6 and tries < 5:
    guess = int(input("Guess the number: "))
    tries += 1

if guess == 6:
    print("You got it!")
elif tries >= 5:
    print("You've reached the maximum number of tries. Game over!")

guessed = False
while not guessed:
    guess = input("Pick a number between 1-10")
    if int(guess) == 9:
        guessed = True

print("You win!")

times_to_repeat = (5)
for x in range(0,times_to_repeat):
        print(x)



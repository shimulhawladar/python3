import random

ActualNumber = random.randint(0,100)
gameStatus = False

turn = 5

for x in range(1,turn+1):
    guess = int(input("Guess a number between 0-100 : "))
    if guess < ActualNumber :
        print("Your guess is less than the actual number.")
        print(f"Remaining { turn - x } out of 5 \n")
    elif guess > ActualNumber :
        print("Your guess is greater than the actual number.")
        print(f"Remaining {turn - x} out of 5 \n")
    else:
        print(f"You Won!!! \nTotal tries {x}")
        gameStatus = True
        break

if gameStatus == False:
    print(f"You loses the game. Actual Number is {ActualNumber}")

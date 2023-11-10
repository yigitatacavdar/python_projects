import random

num = random.randint(1,10)
guess = None

while guess != num:
    guess = input("\nguess the number between 1 and 10 broo: ")
    guess = int(guess)

    if guess == num:
        print("\ncongrats you are a fucking idiot")
        input("press enter to go out")
        break
    else:
        print("nope you couldnt try again")
        

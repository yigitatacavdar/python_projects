import random

def roller():
  n = random.randint(1,12)
  if n >= 6:
    print("You rolled", [str(n)], "you win!!")
    print("wanna play again yes or no")
    answer = input(">")
    if answer == "yes":
      roller()
    elif answer == "no":
      input("press enter to exit")
      
  elif n < 6:
    print("Your rolled", [str(n)], "Better luck next time")
    print("wanna play again yes or no")
    answer = input(">")
    if answer == "yes":
      roller()
    elif answer == "no":
      input("press enter to exit")
    

def start():
 print("This is a dice rolling game, to win you need to roll more than '6', type 'a' to roll")

 answer = input(">")

 if answer == "a":
   roller()
 else:
   print("please press 'a' to roll")
   start()
  

start()





 





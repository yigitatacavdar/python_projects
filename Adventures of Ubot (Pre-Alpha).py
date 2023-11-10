#use time.delay() for waiting in dialog
#use slowprint() for writing slowly


import sys
import time
import random
import keyboard
import collections

    


def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.04)
        if keyboard.is_pressed("s"):
            break
    
    

def start():

    print('{:^110s}'.format("ADVENTURES OF UBOT"))
    print('{:^110s}'.format("Created by Nathan Rye"))
    print("Which chapter would you like like to start from?")
    print("0-Info")
    print("1-Start")
    print("2-Chest Room")
       
    answer = input(">")

    if answer == "1":
        startgame()

    elif answer == "2":
        chest_room()

    elif answer == "0":
        info()

    else:
        start()

       

def info():

    print("Only type in lowercase. if you dont, the game will reset, so consantrate")
    print("press 's' to skip")
    input("press enter to return to main menu")
    start()

def play_again():
    print("\nDo you wanna give it another try? ( 'Yes' or 'No' )")

    answer = input(">")

    if answer == "yes":
        start()

    elif answer == "no":

        print("\nWell see you then!")
        input("press enter to exit")
        exit()

    else:
        game_over("Write it properly")

def game_over(reason):

    print("\n" + reason)
    print("Game Over!")

    play_again()


def startgame():
    
    slowprint("\nOnce upon a time in a very distant land there was a robot adventurer called Ubot. He was created by his masters before they wiped themselves from the planet.")
    slowprint("One day when he was venturing in the dungeons of uzurim, he faced a goblin that pulled a knife to rob him.")
    print("\nwhat do you do? ( 'Run away' or 'Fight' )")

    answer = input(">")

    if answer == "run away":

        slowprint("\nYou managed to run away from the goblin you are quickly heading for the chest room.")
        chest_room()

    elif answer == "fight":

        slowprint("\nWhen you pulled your sword to end him he quickly ran away.")
        chest_room()
        
    else:
        game_over("write it properly")

def chest_room():

    slowprint("\nAfter picking the lock you went in the chest room to see dozens of chests. some of them were open and some of them werent. You collected some gold and left.")
    slowprint("When you were about to leave the dungeon you saw a man standing in the door way. HE WANTS ALL YOUR GOLD and has a knife.")
    print("\nWhat do you do? ( 'Talk him out of the situation' or 'FIGHT')")

    answer = input(">")

    if answer == "talk him out of the situation":

        slowprint("\nHe killed you before you could say a word and got all you money")
        game_over("Unlucky today?")

    elif answer == "fight":

        slowprint("\nAfter his attack you managed to doge it. After a long sword duel you were the winner.")
        slowprint("You headed for home")
    

    else:
        game_over("write it properly")


    
    
start()
        

        


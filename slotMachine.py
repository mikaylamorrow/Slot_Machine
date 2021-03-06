import random
print(60 * '\033[1;34;48m=')
print('''\t\t Welcome to the Slot Machine Simulator
You'll start with $50. You'll be asked if you want to play.
''')
print(60 * '=')

#Constants:
INIT_money = 50
ITEMS = ["CHERRY", "ORANGE", "PLUM", "LEMON", "BELL", "BAR"]

firstWheel = None
secondWheel = None
thirdWheel = None
money = INIT_money


def play():
    global money, firstWheel, secondWheel, thirdWheel
    playQuestion = askPlayer()
    while(money != 0 and playQuestion == True):
        firstWheel = spinWheel()
        secondWheel = spinWheel()
        thirdWheel = spinWheel()
        printScore()
        playQuestion = askPlayer()


def askPlayer():
    global money
    while(True):
        answer = input("\033[1;35;48m Would you like to play? " + "You have $" + str(money) + ". " )
        answer = answer.lower()
        print(60 * '-')
        if(answer == "yes" or answer == "y"):
            return True
        elif(answer == "no" or answer == "n"):
            print("\t\t\033[1;34;48m You ended the game with $" + str(money) + " in your hand. ")
            return False
        else:
            print("wrong input!")


def spinWheel():
    # returns a random item from the wheel

   randomNumber = random.randint(0, 5)
   return ITEMS[randomNumber]


def printScore():
   # prints the current score

   global money, firstWheel, secondWheel, thirdWheel
   if((firstWheel == "CHERRY") and (secondWheel != "CHERRY")):
       win = 2
   elif((firstWheel == "CHERRY") and (secondWheel == "CHERRY") and (thirdWheel != "CHERRY")):
       win = 5
   elif((firstWheel == "CHERRY") and (secondWheel == "CHERRY") and (thirdWheel == "CHERRY")):
       win = 7
   elif((firstWheel == "ORANGE") and (secondWheel == "ORANGE") and ((thirdWheel == "ORANGE") or (thirdWheel == "BAR"))):
       win = 10
   elif((firstWheel == "PLUM") and (secondWheel == "PLUM") and ((thirdWheel == "PLUM") or (thirdWheel == "BAR"))):
       win = 14
   elif((firstWheel == "BELL") and (secondWheel == "BELL") and ((thirdWheel == "BELL") or (thirdWheel == "BAR"))):
       win = 20
   elif((firstWheel == "BAR") and (secondWheel == "BAR") and (thirdWheel == "BAR")):
       win = 250
   else:
       win = -1

   money += win

   if(win > 0):
       print('\033[1;32;48m {:<10}{:^10}{:^10}{:>28}'.format(firstWheel, secondWheel, thirdWheel, ("You Win $")) + str(win))
   else:
       print('\033[1;31;48m {:<10}{:^10}{:^10}{:>28}'.format(firstWheel, secondWheel, thirdWheel, ("You Lose")))
play()

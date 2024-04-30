
#necessary imports
import random #adds the ability to use random numbers
import time, os, sys

def terminalPrint(text):
  for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.005)
    
def typingPrint(text):
  for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.019)
    
def terminalPrint(text):
  for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.05)
  value = input()
  return value

def clearScreen():
  os.system("clear")
    
weapon = False

def strangeCreature():
  actions = ["fight","flee"]
  global weapon
  print("A strange goul-like creature has appeared. You can either run or fight it. What would you like to do?")
  userInput = ""
  while userInput not in actions:
    print("Options: flee/fight")
    userInput = input()
    if userInput == "fight":
      if weapon:
        print("You kill the goul with the knife you found earlier. After moving forward, you find one of the exits. Congats!")
      else:
        print("The goul-like creature has killed you.")
      quit()
    elif userInput == "flee":
      showSkeletons()
    else:
      print("Please enter a valid option.")
      
def showSkeletons():
  directions = ["backward","forward"]
  global weapon
  print("You see a wall of skeletons as you walk into the room. Someone is watching you. Where would you like to go?")
  userInput = ""
  while userInput not in directions:
    print("Options: left/backward/forward")
    userInput = input()
    if userInput == "left":
      print("You find that this door opens into a wall. You open some of the drywall to discover a knife.")
      weapon = True
    elif userInput == "backward":
      introScene()
    elif userInput == "forward":
      strangeCreature()
    else:
      print("Please enter a valid option.")
      

def hauntedRoom():
  directions = ["right","left","backward"]
  print("You hear strange voices. You think you have awoken some of the dead. Where would you like to go?")
  userInput = ""
  while userInput not in directions:
    print("Options: right/left/backward")
    userInput = input()
    if userInput == "right":
      print("Multiple goul-like creatures start emerging as you enter the room. You are killed.")
      quit()
    elif userInput == "left":
      print("You made it! You've found an exit.")
      quit()
    elif userInput == "backward":
      introScene()
    else:
      print("Please enter a valid option.")

def cameraScene():
  directions = ["forward","backward"]
  print("You see a camera that has been dropped on the ground. Someone has been here recently. Where would you like to go?")
  userInput = ""
  while userInput not in directions:
    print("Options: forward/backward")
    userInput = input()
    if userInput == "forward":
      print("You made it! You've found an exit.")
      quit()
    elif userInput == "backward":
      showShadowFigure()
    else:
      print("Please enter a valid option.")
      
def showShadowFigure():
  directions = ["right","backward"]
  print("You see a dark shadowy figure appear in the distance. You are creeped out. Where would you like to go?")
  userInput = ""
  while userInput not in directions:
    print("Options: right/left/backward")
    userInput = input()
    if userInput == "right":
      cameraScene()
    elif userInput == "left":
      print("You find that this door opens into a wall.")
    elif userInput == "backward":
      introScene()
    else:
      print("Please enter a valid option.")


def introScene():
    clearScreen()
    typingPrint("\"Today's the day! I finally landed a tech internship after three years.\n")
    typingPrint("It's my time to shine!\" You leap out of your car once your\n")
    typingPrint("Kia Soul putts to a stop. \"Is my GPS broken? This can't be\n")
    typingPrint("the correct place.\" A dilapidated urban building stands before you.\n")
    clearScreen()
    typingPrint("The door hangs off its hinges almost as if it's inviting you in.\n")
    typingPrint("As you hesitantly approach the building, a tall jolly man with\n")
    typingPrint("glasses peeks his head around the corner akin to a Mystery Gang member.\n")
    typingPrint("???: \"What's your name again?\"\n")
    name = input("Enter name: ")
    typingPrint("Ohh, right. Nice to meet you in person " + name + ".\n")
    typingPrint(name + ": " + "\"Nate, is that you?\"")
    typingPrint("Nate: \"Yup, I would probably recognize you too if you had your\n")
    typingPrint("camera on in the online meeting. Let's continue this conversation inside.\n")





introScene()


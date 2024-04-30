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
  os.system('cls')
    

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
    typingPrint("Nate: \"Ohh, right. Nice to meet you in person " + name + ".\"\n")
    typingPrint(name + ": " + "\"Nate, is that you?\"\n")
    typingPrint("Nate: \"Yup, I would probably recognize you too if you had your\n")
    typingPrint("camera on in the online meeting. Let's continue this conversation inside.\n")
    
introScene()
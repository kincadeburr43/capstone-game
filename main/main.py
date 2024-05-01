#necessary imports
import random #adds the ability to use random numbers
import time, os, sys

name = ""
keycard = False

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

#function to initiate the intro scene of the game
def introScene():
  global name
  actions = ["leave","follow"]
  userInput = ""
  while userInput not in actions:
    typingPrint("Options: leave/follow\n")
    userInput = input()
    if userInput == "leave":
      unemployedEnd()
    elif userInput == "follow":
      enterBuilding()
    else:
      typingPrint("Please enter a valid option.\n")

def unemployedEnd():
  global name
  clearScreen()
  typingPrint("You simply return to your car and drive off.\n")
  typingPrint("As you're driving away, you can see Nate chasing after you in the rearview mirror to no avail.\n")
  typingPrint("You are still unemployed, therefore you lose.\n(Unemployed Ending)\n")

def enterBuilding():
  global name
  clearScreen()
  typingPrint("*The inside of the building looks surprisingly normal.*\n")
  typingPrint("Nate: \"Welcome to Ole' Smitty's Tech & Stuff! We're so glad to have you on the team. You are going to be an in... *ahem* essential asset to our organization.\"\n")
  typingPrint("*Did he accidentally say I was inessential?*\n")
  typingPrint("\"Behold!... The lobby. This is where all the real ones hang out. We chit-chat and chill down here when we're notworking. On the left, we have a few couches and some snacks.\"\n")
  typingPrint("*Woah, I can't wait to chill and eat my hot Cheetos.*\n")
  typingPrint("Nate: \"To the right, we have a few chairs for visitors and the bathroom is down that way too.\"\n")
  typingPrint("*That's handy to know.*\n")
  typingPrint("Nate: \"Right in front of us, we have the lobby desk with our lovely secretary. Say hi to Cleetus!\"\n")
  typingPrint("Nate: \"To the right, we have a few chairs for visitors and the bathroom is down that way too.\"\n")
  typingPrint(name + ": " + "\"Hi... Cleetus\"\n")
  typingPrint("Cleetus: \"Howdy, newbie! You must be the new intern. What's your name again?\"\n")
  typingPrint(name + ": " + name + ".\n")
  typingPrint("Cleetus: \"Alright then! Let's see... (user's name), right here. You'll be on floor 1 with network management. Here's your keycard.\"\n")
  keycard = True
  typingPrint("Nate: \"Thanks a lot Cleetus! Isn't he the sweetest?\"\n")
  typingPrint(name + ": " + "\"Yup.\"\n")
  typingPrint(name + ": " + "*He was very kind. This job doesn't seem too bad.*\n")
  typingPrint("Nate: \"You can look around before going upstairs if you would like.\"\n")
  actions = ["lounge","bathroom", "cleetus", "elevator"]
  userInput = ""
  while userInput not in actions:
    typingPrint("Options: lounge/bathroom/cleetus/elevator\n")
    userInput = input()
    if userInput == "lounge":
      lounge()
    elif userInput == "bathroom":
      bathroom()
    elif userInput == "cleetus":
      talkToCleetus()
    elif userInput == "elevator":
      lobbyElevator()
    else:
      typingPrint("Please enter a valid option.\n")


def lounge():
  pass

def bathroom():
  pass

def talkToCleetus():
  pass

def lobbyElevator():
  pass

if __name__ == "__main__":
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
  typingPrint("???: \"Ohh, right. Nice to meet you in person " + name + ".\"\n")
  typingPrint(name + ": " + "\"Nate, is that you?\"\n")
  typingPrint("Nate: \"Yup, I would probably recognize you too if you had your\n")
  typingPrint("camera on in the online meeting. Let's continue this conversation inside.\n")
  introScene()
    

#necessary imports
import random #adds the ability to use random numbers
import time, os, sys
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

name = ""
keycard = False
weight = 0
explore = False
cleetusTalk = False
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def terminalPrint(text):
  for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.005)
    
def typingPrint(text):
  for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.03)
    
def terminalPrint(text):
  for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.05)
  value = input()
  return value

def clearScreen():
  os.system('cls')
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

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
      
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def unemployedEnd():
  global name
  clearScreen()
  typingPrint("You simply return to your car and drive off.\n")
  typingPrint("As you're driving away, you can see Nate chasing after you in the rearview mirror to no avail.\n")
  typingPrint("You are still unemployed, therefore you lose.\n(Unemployed Ending)\n")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def enterBuilding():
  global name
  if explore == False:
    clearScreen()
    typingPrint("*The inside of the building looks surprisingly normal.*\n")
    typingPrint("Nate: \"Welcome to Ole' Smitty's Tech & Stuff! We're so glad to have you on the team. You are going to be an in... *ahem* essential asset to our organization.\"\n")
    typingPrint("*Did he accidentally say I was inessential?*\n")
    typingPrint("\"Behold!... The lobby. This is where all the real ones hang out. We chit-chat and chill down here when we're not working. On the left, we have a few couches and some snacks.\"\n")
    typingPrint("*Woah, I can't wait to chill and eat my hot Cheetos.*\n")
    typingPrint("Nate: \"To the right, we have a few chairs for visitors and the bathroom is down that way too.\"\n")
    typingPrint("*That's handy to know.*\n")
    typingPrint("Nate: \"Right in front of us, we have the lobby desk with our lovely secretary. Say hi to Cleetus!\"\n")
    typingPrint("Nate: \"To the right, we have a few chairs for visitors and the bathroom is down that way too.\"\n")
    typingPrint(name + ": " + "\"Hi... Cleetus\"\n")
    typingPrint("Cleetus: \"Howdy, newbie! You must be the new intern. What's your name again?\"\n")
    typingPrint(name + ": " + name + ".\n")
    typingPrint("Cleetus: \"Alright then! Let's see... " + name + ", right here. You'll be on floor 1 with network management. Here's your keycard.\"\n")
    keycard = True
    typingPrint("Nate: \"Thanks a lot Cleetus! Isn't he the sweetest?\"\n")
    typingPrint(name + ": " + "\"Yup.\"\n")
    typingPrint(name + ": " + "*He was very kind. This job doesn't seem too bad.*\n")
    typingPrint("Nate: \"You can look around before going upstairs if you would like.\"\n")
  else:
    typingPrint("What would you like to do next?\n")
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
      
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      
def caseOhEnding():
  typingPrint("Nate: \"You broke the couch?! You're out of control and now banned from the snacks.")
  typingPrint("Go back to the lobby.")
  
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def lounge():
  global weight
  global explore
  explore = True
  clearScreen()
  typingPrint("*This area seems pretty chill.\n")
  typingPrint("\"The couch is quite comfy, and they already have a fridge stocked with snacks.\"\n")
  typingPrint("\"Aw, bell yeah. Time to eat some hot Cheetos.\"\n")
  typingPrint("*Your stomach enlarges slightly more.*\n")
  clearScreen()
  weight += 60
  typingPrint("Weight" + ": " + str(weight) +"\n")
  if (weight >= 300):
    caseOhEnding()
  else:
    actions = ["leave"]
    userInput = ""
    while userInput not in actions:
      typingPrint("Options: leave\n")
      userInput = input()
      if userInput == "leave":
        enterBuilding()
      else:
        typingPrint("Please enter a valid option.\n")
        
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  

def bathroom():
  global explore
  explore = True
  clearScreen()
  typingPrint("*Hmm, the bathroom has a code. That's unfortunate. I kind of needed to use the loo.*\n")
  actions = ["leave"]
  userInput = ""
  while userInput not in actions:
    typingPrint("Options: leave\n")
    userInput = input()
    if userInput == "leave":
      enterBuilding()
    else:
      typingPrint("Please enter a valid option.\n")
      
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def cleetus1():
  global name
  global cleetusTalk
  cleetusTalk = True
  typingPrint("Cleetus: \"Why of course. You don't need to pay anyone else for desk service when you have Cleetus.\"\n")
  typingPrint(name + ": " + "*tight budget I guess*\n")
  talkToCleetus()
  
def cleetus2():
  global name
  global cleetusTalk
  cleetusTalk = True
  typingPrint("Cleetus: \"Paid? You're the unpaid intern. It says so right here on your name tag.\"\n")
  typingPrint(name + ": " + "*At least I'll get experience.*\n")
  talkToCleetus()
  
def cleetus3():
  global name
  global cleetusTalk
  cleetusTalk = True
  typingPrint("Cleetus: \"No.\"\n")
  typingPrint(name + ": " + "\"Why not?\"\n")
  typingPrint("Cleetus: \"No one meets the boss.\"\n")
  talkToCleetus()

def talkToCleetus():
  global explore
  global name
  explore = True
  clearScreen()
  if cleetusTalk == False:
    typingPrint("Cleetus: \"What's up " + name + " ? Got any questions for Cleetus?\n")
    typingPrint("1: Are you the only secretary?\n")
    typingPrint("2: How much am I getting paid?\n")
    typingPrint("3: Can I meet the boss?\n")
  else:
    typingPrint("Cleetus: \"Any other questions?\"\n")
    typingPrint("1: Are you the only secretary?\n")
    typingPrint("2: How much am I getting paid?\n")
    typingPrint("3: Can I meet the boss?\n")
  actions = ["1", "2", "3"]
  userInput = ""
  while userInput not in actions:
    typingPrint("Options: 1/2/3/leave\n")
    userInput = input()
    if userInput == "1":
      cleetus1()
    elif userInput == "2":
      cleetus2()
    elif userInput == "3":
      cleetus3()
    elif userInput == "leave":
      enterBuilding()   
    else:
      typingPrint("Please enter a valid option.\n")
      
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def lobbyElevator():
  global explore
  global name
  explore = True
  clearScreen()
  
  typingPrint("Cleetus: \"Enjoy your first day!\"\n")
  typingPrint(name + ": \"Sorry for taking so long, Nate.\"\n")
  typingPrint("Nate: \"K, let's get going.\"\n")
  typingPrint(name + ": *He seems a little angry.*\n")
  typingPrint("You move past him and swipe your keycard across the scanner next to the door and enter. Nate follows.\n")
  typingPrint("Nate: \"You know that was an RFID reader you used. It wirelessly reads the RFID tag your card emits and compares your data against our employee database.\"\n")
  typingPrint(name + ": \"I didn't, thank you for this valuable information.\"\n")
  typingPrint("*ding*\nAs the elevator doors open, you let out a sigh of relief.\n" + name + ": *Man, Nate is odd.* \n")
  typingPrint("Nate: \"Here's the 1st floor. This is our customer service floor where our lovely employees help customers through their problems when Cleetus is not available.\n")
  typingPrint("Your first task is to build Janet's new computer. She's our top employee on this level, so she needs the best equipment at all times. Come say hi!\"\n")
  typingPrint("Nate: \"Janet, this is our new intern, " + name + ". They're here to build your PC.\"\n")
  typingPrint("Janet: \"Nice to meet you! I have all the parts right here. I'm so excited to have a 4090!\"\n")
  typingPrint(name + ": \"Wow, that's awesome! I can't wait to build it for you.\"\n")
  typingPrint("Nate: \"Okay, let's get started. I'll give you about two hours to build it.\"\n")
  typingPrint(name + ": \"Sounds like a deal.\"\n")



  actions = ["leave"]
  userInput = ""
  while userInput not in actions:
    typingPrint("Options: leave\n")
    userInput = input()
    if userInput == "leave":
      enterBuilding()
    else:
      typingPrint("Please enter a valid option.\n")
  

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

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
    

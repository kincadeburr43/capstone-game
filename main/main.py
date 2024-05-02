#necessary imports
import random #adds the ability to use random numbers
import time, os, sys
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

name = ""
keycard = False
weight = 0
explore = False
cleetusTalk = False
lives = 5
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
  buildPC()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def troubleshoot2():
  pass

def explainOSI():
  typingPrint("Nate: *sigh* \"You're pretty incompetent, you know that? Anyway, the OSI model or the Open Systems Interconnection is a more organized way to understand how network protocols and communication between devices works.\n")
  typingPrint("There are seven layers (starting from the bottom): Physical, Data Link, Network, Transport, Session, Presentation, Application. The data link layer packages the 1s and 0s from the physical layer into a nice frame. The network layer takes care of addressing messages to the right place.\n")
  typingPrint("This is where IP lies. The transport layer is responsible for making sure the IP packet arrives at its destination properly. The session layer establishes a session to send the messages over. The presentation layer formats data so it can be used by the application layer.\n")
  typingPrint("The application layer deals with the user interface of the software. Hopefully, you can use this knowledge to help troubleshoot the other computers. Let's get back to work now.\"\n")
  troubleshoot2()

def t1Right():
  typingPrint("Nate: \"Stellar! Let's move on to the next problem.\"\n")
  troubleshoot2()

def t1Wrong():
  typingPrint("Nate: \"No, it should be bottom-up since we're dealing with a potentially physical layer issue.\nThe physical layer is the bottom layer of the OSI model and encapsulates all functionality of physical parts such as cabling, electronics, and Network Interface Cards.\nPlease don't tell me you need me to explain the OSI model.\"\n")
  explainOSI()

def troubleshoot1():
  typingPrint("Nate: \"This is Demarco. I'll let him explain what's been happening.\"\n")
  typingPrint("Demarco: \"Hello, Nate told me you're here to fix my computer. I've been having problems with accessing the internet.\n")
  typingPrint("No matter what ethernet cable I use, I cannot connect to the internet.\"\n")
  typingPrint("Nate: \"What troubleshooting method should be used in this situation?\"\n")
  typingPrint("1: Top-Down\n")
  typingPrint("2: Bottom-Up\n")
  typingPrint("3: Divide-and-conquer\n")
  actions = ["1", "2", "3"]
  userInput = ""
  while userInput not in actions:
    userInput = input("Enter Answer: ")
    if userInput == "2":
      t1Right()
    elif userInput == "1":
      t1Wrong()
    elif userInput == "3":
      t1Wrong()
    else:
      typingPrint("Please enter a valid option.\n")

def level1Elevator():
  global name
  typingPrint("Nate: \"That's all I have for you on this floor. Let's get back to the elevator.\"\n")
  typingPrint("As the elevator doors open, the feeling of impending doom consumes your mind. A purple haze seems to leak from the interior, yet Nate is unphased.\n")
  typingPrint("Nate: \"Is something wrong " + name + "?\"\n")
  typingPrint(name + ": \"Do you not see that?\"\n")
  typingPrint("Nate: \"See what?\"\n")
  typingPrint(name + ": \"Nevermind then...\"\n")
  typingPrint("Nate: \"Okay, maybe you're just nervous on the first day.\"\n")
  typingPrint(name + ": \"Yeah, that's probably it... sorry about that.\"\n")
  typingPrint("*ding*\nThe elevator doors open to reveal an identical layout of the first floor.\n")
  typingPrint("Nate: \"This is our finance department. Some of our employees are having some problems with their PCs, so I would like you to troubleshoot them.\"\n")
  troubleshoot1()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def wrongHypervisor():
  global lives
  lives -= 1
  typingPrint("Nate: \"No, it's definitely a type 2 hypervisor. The difference is that a type 1 hypervisor is installed directly onto the hardware of a server/computer.\"\n")
  typingPrint("However, a type 2 hypervisor is installed on the operating system. We are just trying to download a hypervisor on to her built computer in this case.\"\n")
  
def rightHypervisor():
  typingPrint("Nate: \"Awesome job! I award you a gold star for that.\"\n")
  level1Elevator()

def hypervisorQuestion():
  typingPrint("Should we use a type 1 or type 2 hypervisor?\"\n")
  actions = ["1", "2"]
  userInput = ""
  while userInput not in actions:
    typingPrint("Options: 1/2\n")
    userInput = input()
    if userInput == "1":
      wrongHypervisor()
    elif userInput == "2":
      rightHypervisor()
    else:
      typingPrint("Please enter a valid option.\n")


def finishedPC():
  typingPrint(name + ": \"It's all finished!\"\n")
  typingPrint("Janet: \"Thank you so much!\"\n")
  typingPrint("Nate: \"What a star. Now... let's see if you can install the right hypervisor on her computer.\"\n")
  typingPrint("Our company operates on Linux, but she chose to have a Windows PC.\"\n")
  typingPrint("It is essentially a manager for virtual machines. A virtual machine is like a fake operating system.\"\n")
  typingPrint("It allows a user to use their PC on an operating system other than the natively installed one.\"\n")
  typingPrint("You can have multiple opened at a time, and ahypervisor is what manages these virtual machine instances.\"\n")
  hypervisorQuestion()


def brokenPC():
  global lives
  lives -= 1
  typingPrint("Janet: \"NOOOO, MY BEAUTIFUL PC. YOU ARE UNQUALIFIED. NATE, GET THEM OUT OF HERE!!!\"")

def buildPC():
  pcFails = 0
  pcWins = 0
  steps = [1, 4, 5, 3, 6, 7, 2, 8]
  words = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eigth"]
  for i in range(len(steps)):
      typingPrint("What's the " + words[i] + " step to building a PC?\n")
      typingPrint("1: Ground the PC to prevent Electrostatic Discharge\n")
      typingPrint("2: Install GPU\n")
      typingPrint("3: Install Power Supply\n")
      typingPrint("4: Install CPU & Cooler\n")
      typingPrint("5: Install RAM\n")
      typingPrint("6: Install Motherboard\n")
      typingPrint("7: Install SSD/HDD\n")
      typingPrint("8: Plug in PC and power on\n")  
      userInput = int(input("Enter Answer: "))
      if userInput == steps[i]:
          pcWins += 1
          typingPrint("Correct.\n")
      else:
          pcFails += 1
          typingPrint("Wrong.\n")
      typingPrint("You have " + str(pcFails) + " incorrect and " + str(pcWins) + " correct.\n")
      clearScreen()
      if pcFails >= 3:
          brokenPC()
      if pcWins >= 8:
          finishedPC()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#if __name__ == "__main__":
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
    
buildPC()
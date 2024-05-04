#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
THE INTERNSHIP
Joshua Butler and Kincade Burroughs
Cisco Senior Capstone Project
'''
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

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
    print(char, end='', flush = True)
    time.sleep(0.04)
    
def terminalInput(text):
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
  clearScreen()
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
  clearScreen()
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
  clearScreen()
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
  clearScreen()
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

def subnet3Right():
  clearScreen()
  typingPrint("Ole Smitty: \"This is not possible. No. No no no no no. NO!\n")
  typingPrint("There's no chance you just bested me, the subnetting wizard, Ole Smitty.\n")
  typingPrint("I cannot live after such a devastating embarrassment.\n")
  typingPrint("Here is your recommendation letter and company of interest.\n")
  typingPrint("\n")
  typingPrint("He hands you a tobacco-stained piece of paper with\n")
  typingPrint('the words, "Google, hire dis guy. He very smart.\n')
  typingPrint("-Ole Smitty.\"\n")
  typingPrint("\n")
  typingPrint("You celebrate your victory with a Fortnite dance and return to the\n")
  typingPrint("outside world just to realize you are still jobless lol.")

def subnet3Wrong():
  global lives
  lives -= 1
  clearScreen()
  typingPrint("Ole Smitty: \"Muahahah. That was the wrong answer, and that means your soul is mine.\n")
  typingPrint("He eats sucks the soul out of you as he cackles.\n")
  typingPrint("You die and lose.\"")

def subnet3():
  clearScreen()
  typingPrint("Ole Smitty: \"How many subnets does a network address of 192.168.0.0 /28 create?\"")
  userInput = input()
  if userInput == "16":
    subnet3Right()
  else:
    subnet3Wrong()

def subnet2Right():
  clearScreen()
  typingPrint("Ole Smitty: \"Okay, clearly I've been going too easy. This next one is a doozy.\"")
  subnet3()
  
def subnet2Wrong():
  global lives
  lives -= 1
  clearScreen()
  typingPrint("Ole Smitty: \"Muahahah. That was the wrong answer, and that means your soul is mine.\n")
  typingPrint("He eats sucks the soul out of you as he cackles.\n")
  typingPrint("You die and lose.\"")
  
def subnet2():
  clearScreen()
  typingPrint('Ole Smitty: "What is the IP address range for Class C addresses?\n')
  typingPrint("1: 0.0.0.0 to 127.255.255.255\n")
  typingPrint("2: 128.0.0.0 to 191.255.255.255\n")
  typingPrint("3: 192.0.0.0 to 223.255.255.255\n")
  typingPrint("4: 224.0.0.0 to 239.255.255.255\"\n")
  actions = ["1", "2", "3", "4"]
  userInput = ""
  while userInput not in actions:
    typingPrint("Options: 1/2/3/4\n")
    userInput = input()
    if userInput == "3":
      subnet2Right()
    elif userInput == "2" or "1" or "4":
      subnet2Wrong()
    else:
      typingPrint("Please enter a valid option.\n")

def subnet1Wrong():
  global lives
  lives -= 1
  clearScreen()
  typingPrint('Ole Smitty: "Muahahah. That was the wrong answer, and that means your soul is mine.\n')
  typingPrint("He eats sucks the soul out of you as he cackles.\n")
  typingPrint("You die and lose.\"")
  
def subnet1Right():
  clearScreen()
  typingPrint("\"Hmm, so you got the first one correct. You're one step closer to a new life. Time for the next question.\"\n")
  subnet2()

def subnet1():
  clearScreen()
  typingPrint("Ole Smitty: \"On a Class A subnet, how many hosts would there be in a single subnet with a slash notation of /25?\"")
  userInput = input()
  if userInput == "256":
    subnet1Right()
  else:
    subnet1Wrong()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def floor4ElevatorRight():
  global name
  clearScreen()
  typingPrint(name + ": \"That's all I needed... you're cooked brother.\" You feel a shove in your back which propels you into the grimy elevator. Your consciousness fades in and out... then suddenly the elevator falls from beneath you, and you pass out.\n")
  typingPrint("???: \"It's so nice to meet you. I enjoy watching my prey struggle.\"\n")
  typingPrint(name + ": \"huh, what's going on?\"\n")
  typingPrint("???: \"You were finished the moment you applied to this job. I've been feeding off your brain power ever since you stepped into this building. Every problem you solve only increases my power. It's so yummy!\"\n")
  typingPrint(name + ": \"WHAT?! WHO EVEN ARE YOU?\"\n")
  typingPrint("???: \"Ho, ho. You know me. I'm your boss, Ole Smitty, otherwise known as the subnetting wizard.\"\n")
  typingPrint(name + ": \"Why would you do this to me?\"\n")
  typingPrint("Ole Smitty: \"This is how I keep this company running. All of my brain power has given me psychic powers. With these great powers, I can telekinetically spread mind propaganda promoting the company.\"\n")
  typingPrint(name + ": \"That's horrible! Have you been mind-controlling me too?\"\n")
  typingPrint("Ole Smitty: \"You learn quickly, youngin. I've been manipulating your every movement since you joined us.\"\n")
  typingPrint(name + ": \"NO. IT'S NOT POSSIBLE.\"\n")
  typingPrint("Ole Smitty: \"Believe it, Sonny. There's no point in denying the truth. It may very well just cost you your life. Now, because I am so gracious and love all my employees, I will give you a chance to escape with a good reference letter and a job opportunity elsewhere.\"\n")
  typingPrint(name + ": \"Please... what do I have to do.\"\n")
  typingPrint("Ole Smitty: \"You must solve 3 subnetting problems. If you even miss one... it's joever.\"\n")
  typingPrint(name + ": \"Zounds! I need to get out of here. Give me the first problem.\"\n")
  typingPrint("Ole Smitty: \"As you wish. Here's the first problem.\"")
  subnet1()
  
def floor4Elevator():
  global name
  i = 0
  randNum4 = random.randint(0,65536)
  binNum4 = bin(randNum4)[2:].zfill(16) # [2:] takes the first two characters off the binary string (0b) and zfill pads the front with 0's until it is 4-digits long
  clearScreen()
  typingPrint(name + ": \"Let's go to the 5th floor so you can meet the boss. I'm sure he'd love to see his new intern.\"\n")
  typingPrint(name + ": \"That sounds like a plan.\"\n")
  typingPrint("*He talks about this so casually, but I'm pretty nervous. My mind feels like it's rotting, and my stomach is turning. I think I'm going to be sick.*\n")
  typingPrint("Nate: \"Of course, this is the top floor, so it's the most secure with a 16 digit binary lock. The number is " + str(randNum4) +", now convert it into binary.\"\n")
  
  userInput = input("Enter code: ")
  while userInput != binNum4:
    typingPrint("You try swiping your card, but no money. Let's try another code.\n")
    userInput = input("Enter code: ")
    i += 1
    if i >= 2:
        typingPrint("Nate: \"Wrong again. Now we're locked out! And you got so close to meeting the boss too... I'll have to deal with you myself.\"\n*Nate's head enlarges 5 fold, and you feel your brain start to shrink. You dead.\n(Bad Binary Ending #3)")
        break
  if userInput == binNum4:
    floor4ElevatorRight()
    
  
def staticRouteWrong():
  global lives
  lives -= 1
  clearScreen()
  typingPrint("Nate: *incorrect buzzer sound effect*\"Go again.\"n")
  staticRoute()
  
def staticRouteRight():
  global name
  clearScreen()
  typingPrint("Nate: \"All done with the routers, fantastic job!\"n")
  typingPrint(name + ": \"Thanks again, Nate. It's really nothing. I'm just doing my job.\"\n")
  floor4Elevator()

def staticRoute():
  clearScreen()
  typingPrint("What is the command to configure a basic static route?\n")
  typingPrint("1: ip route outside-address subnet-mask inside-address\n")
  typingPrint("2: ip route inside-address subnet-mask outside-address\n")
  typingPrint("3: ip route mapping inside-address subnet-mask outside-address\n")
  actions = ["1", "2", "3"]
  userInput = ""
  while userInput not in actions:
    typingPrint("Options: 1/2/3\n")
    userInput = input()
    if userInput == "2":
      staticRouteRight()
    elif userInput == "3" or "1":
      staticRouteWrong()
    else:
      typingPrint("Please enter a valid option.\n")
def natRight():
  clearScreen()
  typingPrint("Nate: \"Shweet! On to the final problem of the floor.\"\n")
  staticRoute()
  
def natWrong():
  global lives
  lives -= 1
  clearScreen()
  typingPrint("Nate: \"Nah, fam. Try again.\"\n")


def nat():
  global name
  clearScreen()
  typingPrint(name + "\"Got it, Nate. Thanks.\"\n")
  typingPrint("You are already logged into the router, so you enter the exit command to return to global configuration mode.\n")
  typingPrint(name + "*It looks like I need to create a static NAT configuration.*\n")
  typingPrint("What is the command used to create a static inside NAT configuration?\n")
  typingPrint("1: ip nat translation inside address\n")
  typingPrint("2: ip nat inside\n")
  typingPrint("3: ip nat inside source static address\n")
  
  actions = ["1", "2", "3"]
  userInput = ""
  while userInput not in actions:
    typingPrint("Options: 1/2/3\n")
    userInput = input()
    if userInput == "3":
      natRight()
    elif userInput == "2" or "1":
      natWrong()
    else:
      typingPrint("Please enter a valid option.\n")

def dhcpRight():
  clearScreen()
  typingPrint("Nate: \"Oh my glob, that was fantastical! let's move on to the next task: configuring NAT.\"\n")
  nat()

def dhcpWrong():
  global lives
  lives -= 1
  clearScreen()
  typingPrint("Nate: \"Try that again... you can do better.\"\n")
  dhcp()


def dhcp():
  clearScreen()
  typingPrint(name + ": *okay, first up. DHCP*\n")
  typingPrint("You log into the router and enter the necessary passwords. It turns out this router has received an IP address via DHCP, however none of the clients connected have access to DHCP. What command would allow this router to pass on DHCP services to the rest of the network?\n")
  typingPrint("1: ip dhcp relay-address address\n")
  typingPrint("2: ip dhcp helper-address address\n")
  typingPrint("3: ip helper-address address\n")
  actions = ["1", "2", "3"]
  userInput = ""
  while userInput not in actions:
    typingPrint("Options: 1/2/3\n")
    userInput = input()
    if userInput == "3":
      dhcpRight()
    elif userInput == "2" or "1":
      dhcpWrong()
    else:
      typingPrint("Please enter a valid option.\n")

def floor3ElevatorRight():
  clearScreen()
  typingPrint("Nate: \"Okay, nice. Let's continue.\"\n")
  typingPrint("Your legs become heavier as the elevator doors open. It feels as if gravity increased two fold. Once your second foot enters the elevator, it shoots up to the next floor, doors still open.\n\n")
  typingPrint(name + ": \"AHH, WHAT THE BISCUITS!\"\n")
  typingPrint("*ding*\n")
  typingPrint("Nate: \"Sorry about that. The elevator guy is coming in tomorrow.\"\n")
  typingPrint(name + ": *What kind of elevator is this?*\n")
  typingPrint(name +": \"Yeah, alright.\"\n")
  typingPrint("Nate: \"Let's just get off. It's not the most safe to be on there. I just want to make sure you get the whole experience.\"\n")
  typingPrint("Unease fills your body as you exit the elevator. The desecrated routers are barely screwed in, and the racks are disheveled as ever. There also seems to be an ominous red stain upon the wall in front of you.\n\n")
  typingPrint(name + "*Maybe someone spilled their lunch.*\n")
  typingPrint("Nate: \"Don't worry about that stain, it's really nothing. You should be more worried about your next tasks. First, I need you to fix our DHCP server, then you will configure NAT, and finally, configure a new static route.\"")
  dhcp()
def floor3Elevator():
  global name
  i = 0
  randNum3 = random.randint(0,255)
  binNum3 = bin(randNum3)[2:].zfill(8) # [2:] takes the first two characters off the binary string (0b) and zfill pads the front with 0's until it is 4-digits long
  clearScreen()
  typingPrint("Nate: \"Fire, onward to the third floor. You didn\'t see anything in that closet, right?\"\n")
  typingPrint(name + "\": No, no. no. Don\'t get it twisted. I didn\'t see anything. Just the switch cable.\"\n")
  typingPrint("Nate: \"Okay, just checking. I lost something recently and haven't been able to find it. Anyway, let's go to the elevator.\"\n")
  typingPrint(name + "*The elevator seems to have another binary code. This time it is 8 bits long, otherwise known as one byte. The given number is " + str(randNum3) + ". What would this be in binary?*\n")
 
  userInput = input("Enter code: ")
  while userInput != binNum3:
    typingPrint("Nate: \"It's not that hard bro. Keep trying.\"\n")
    userInput = input("Enter code: ")
    i += 1
    if i >= 2:
        typingPrint("Nate: \"Ngl. You kinda suck at this. You're fired.\"\n(Bad Binary Ending #2)")
        break
  if userInput == binNum3:
    floor3ElevatorRight()





def stpRight():
  typingPrint("Nate: \"Swagalicious, my croney! On to the final task... etherchannel.\"\n")
  typingPrint("*I'm pretty sure that's the technique used for link aggregation. It allows multiple connections to act as one.*\n")
  typingPrint("You enter the show etherchannel command in privileged exec mode to check the status of the links.\n")
  typingPrint("*Zounds, this is a problem. G0/1 and G0/2 are on VLAN 1, instead of 99. Let's change them to VLAN 99.\n")
  typingPrint("You enter the first two commands:\ninterface range g0/1-2\nswitchport mode access\n")
  typingPrint("YWhat's the last command to enter?\n")
  typingPrint("1: switchport access vlan 99\n")
  typingPrint("2: switchport access default-vlan 99\n")
  typingPrint("3: switchport trunk vlan 99\n")
  actions = ["1", "2", "3"]
  userInput = ""
  while userInput not in actions:
    typingPrint("Options: 1/2/3\n")
    userInput = input()
    if userInput == "1":
      floor3Elevator()
    elif userInput == "2" or "3":
      maxPortsRight()
    else:
      typingPrint("Please enter a valid option.\n")

def stpWrong():
  global lives
  lives -= 1
  clearScreen()
  typingPrint("Nate: \"No, try it again.\"\n")
  maxPortsRight()


def maxPortsRight():
  global name
  clearScreen()
  typingPrint("Nate: \"Step one is done. Now on to STP.\"\n")
  typingPrint(name + ": *It seems to be running normal, but something's not right. Why is one link down when four ports are occupied.*\n")
  typingPrint("What command could be used to make the link operational?\n")
  typingPrint("1: shutdown\n")
  typingPrint("2: no shutdown\n")
  typingPrint("3: port-status up\n")
  actions = ["1", "2", "3"]
  userInput = ""
  while userInput not in actions:
    typingPrint("Options: 1/2/3\n")
    userInput = input()
    if userInput == "2":
      stpRight()
    elif userInput == "1" or "3":
      stpWrong()
    else:
      typingPrint("Please enter a valid option.\n")



def maxPortsWrong():
  global lives
  lives -= 1
  clearScreen()
  typingPrint("Nate: \"Even I know that one. Try again.\"\n")


def switch1Right():
  global name
  clearScreen()
  typingPrint("Nate: \"Correctamungo! Now just swap out that power cable for a spare in the closet.\"\n")
  typingPrint(name + "\"Of course!\"\n")
  typingPrint("As you approach the closet, stench which was originally claimed as a fart becomes more prominent. You open the door and a skeleton falls next to your feet.\"\n")
  typingPrint(name + ": \"HOLY CRACKERS AND CHEESE!\"\n")
  typingPrint("Nate: \"What's wrong " + name + "?")
  typingPrint(name + ": *just try to act normal, I need this position*\nOh nothing, I just thought I saw a spider. I have arachnophobia.*\n")
  typingPrint("*I really hope they just forgot to take down Halloween decorations.*\n")
  typingPrint("You swiftly grab the power cord, return to Nate, and swap the cables. \n")
  typingPrint("Nate: \"Now I also know we also need to update the max number of allowed ports and ensure STP and Etherchannel are operational.\nLuckily, we have a subscription to Cisco DNA center so we can manage multiple switches from one computer.")
  typingPrint("You boot up DNA center on the computer beside the massive rack of switches and open the terminal.\n")
  typingPrint(name + "\"Okay, first I have to change the max number of ports.\"\n")
  clearScreen()
  
  typingPrint("\"What command can accomplish this?\"\n")
  typingPrint("1: switchport port-security\n")
  typingPrint("2: switchport port-security violation\n")
  typingPrint("3: switchport port-security maximum (#)\n")
  actions = ["1", "2", "3"]
  userInput = ""
  while userInput not in actions:
    typingPrint("Options: 1/2/3\n")
    userInput = input()
    if userInput == "3":
      maxPortsRight()
    elif userInput == "2" or "1":
      maxPortsWrong()
    else:
      typingPrint("Please enter a valid option.\n")



def switch1Wrong():
  global lives
  lives -= 1
  clearScreen()
  typingPrint("Nate: \"Erm. Try again.\"\n")


def switch():
  clearScreen()
  typingPrint("Nate: \"First off, this switch has a blinking amber power light. Doesn't seem pretty normal, I want you to find the problem. What does this light indicate?\"\n")
  typingPrint("1: Indicates the switch is working, but not receiving power properly.\n")
  typingPrint("2: The switch is not receiving enough power.\n")
  typingPrint("3: Power over Ethernet is working properly.\n")
  actions = ["1", "2", "3"]
  userInput = ""
  while userInput not in actions:
    typingPrint("Options: 1/2/3\n")
    userInput = input()
    if userInput == "1":
      switch1Right()
    elif userInput == "2" or "3":
      switch1Wrong()
    else:
      typingPrint("Please enter a valid option.\n")

def floor2ElevatorRight():
  global name
  clearScreen()
  typingPrint("As you step into the elevator, you can feel an ominous force lurking. It almost feels as if someone is inside your brain.\"\n")
  typingPrint(name + ": \"I think I'm starting to develop a headache. Is it okay if I go home for the day. I don't want to risk getting anyone sick.\"\n")
  typingPrint("Nate: \"No, worries! You're the only one who's working on the next two floors.\"\n")
  typingPrint(name +": \"What?\"\n")
  typingPrint("Nate: \"Well, besides me. But most of the time I'm helping out the boss with his tech issues.\"\n")
  typingPrint(name +": \"Interesting.\"\n*ding* The elevator doors open and a rancid scent pervades your nostrils.")
  typingPrint("Nate: \"Died? No one died in here.\"\n")
  typingPrint(name +": \"What's that smell then?\"\n")
  typingPrint("Nate: \"Sorry, I farted. Let's go somewhere else.\"\n")
  typingPrint(name +": \"Good idea.\"\n")
  typingPrint("Nate: \"Anyway, this is the switching room. We keep all of our switches here alongside a few test computers. Let's go over to switch 1.\"\n")
  switch()
  
def floor2Elevator():
  i = 0
  randNum2 = random.randint(0,15)
  binNum2 = bin(randNum2)[2:].zfill(4) # [2:] takes the first two characters off the binary string (0b) and zfill pads the front with 0's until it is 4-digits long
  clearScreen()
  typingPrint("Nate: \"Now that we're reaching the higher floors, there are greater security measures. You see next to the door, there is a 4-digit code. The code only consists of 1's and 0's.\n")
  typingPrint("All you have to do is convert the given decimal number into binary. Give it a try. The number for you is " + str(randNum2) + ".\"\n")
  userInput = input("Enter code: ")
  while userInput != binNum2:
    typingPrint("You try swiping your card, but no money. Let's try another code.\n")
    userInput = input("Enter code: ")
    i += 1
    if i >= 2:
        typingPrint("Nate: \"Clearly you don't know your stuff. Now we're locked out. I guess we just have to leave.\"\n(Bad Binary Ending)")
        break
  if userInput == binNum2:
    floor2ElevatorRight()
      
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def t3Right():
  global name
  clearScreen()
  typingPrint("Nate: \"Fantástico! Whoops, accidentally switched to Spanish. I've been watching too much Dora lately.\"\n")
  typingPrint(name +": \"Muy bien, Nate.\"\n")
  typingPrint("Nate: \"Gracias, vamos arriba!\"\n")
  typingPrint(name +": \"Sí.\"\n")
  floor2Elevator()


def t3Wrong():
  global lives
  lives -= 1
  clearScreen()
  typingPrint("Nate: \"This is crazy man. How do you still not know the OSI model? It's so important to your job. Let's just move on to the next floor.\"\n")
  floor2Elevator()


def troubleshoot3():
  global name
  clearScreen()
  typingPrint("Nate: \"This is Jeff. Say hi to " + name + ", Jeff\"\n")
  typingPrint("Jeff: \"Hi, " + name + ".\"\n")
  typingPrint("Nate: \"Jeff, what problem did you have with your computer again.\"\n")
  typingPrint("Jeff: \"When I try to search for anything on my browser, the entire webpage looks like it was put through a washing machine.\"\n")
  typingPrint("Nate: \"What layer of the OSI model would this problem fall upon?\"\n")
  typingPrint("Jeff: \"I don't know, I just do the taxes.\"\n")
  typingPrint("Nate: \"That's enough from you Jeff.\"\n")
  actions = ["1", "2", "3", "4", "5", "6", "7"]
  userInput = ""
  while userInput not in actions:
    userInput = input("Enter Answer: ")
    if userInput == "7":
      t3Right()
    elif userInput == "1" or "2" or "4" or "5" or "6" or "3":
      t3Wrong()
    else:
      typingPrint("Please enter a valid option.\n")


def noExplainOSI():
  clearScreen()
  typingPrint("Nate: \"Okay then. Let's get to the last person.\"\n")
  troubleshoot3()


def t2Right():
  global name
  clearScreen()
  typingPrint("Nate: \"Woah, nice job!\"\n")
  typingPrint("Clarisse: \"Cheers, luv!\"\n")
  typingPrint("\"Let's keep it moving " + name + ".\"\n")
  troubleshoot3()


def t2Wrong():
  clearScreen()
  global lives
  lives -= 1
  typingPrint("Nate: No, the problem was at the network layer since it deals with DHCP and IP addresses which are layer three protocols.\nDo you really need me to explain the OSI layers?\"\n")
  actions = ["yes", "no"]
  userInput = ""
  while userInput not in actions:
    typingPrint("Options: yes/no")
    userInput = input("Enter Answer: ")
    if userInput == "yes":
      explainOSI()
    elif userInput == "no":
      noExplainOSI()
    else:
      typingPrint("Please enter a valid option.\n")

def troubleshoot2():
  clearScreen()
  typingPrint("Nate: \"Next up, we have Clarisse. (She's British by the way)\"\n")
  typingPrint("Clarisse: \"Ello luv, I've got a slight problem with my desktop. I cannot seem to receive an address from the DHCP server. All I get is an APIPA address, y'know, one of those \"169.254...\" ones.\"\n")
  typingPrint("Nate: \"What layer of the OSI model does this issue fall under?\"\n1: Physical\n2: Data Link\n3: Network\n4: Transport\n5: Session\n6: Presentation\n7: Application\n")
  actions = ["1", "2", "3", "4", "5", "6", "7"]
  userInput = ""
  while userInput not in actions:
    userInput = input("Enter Answer: ")
    if userInput == "3":
      t2Right()
    elif userInput == "1" or "2" or "4" or "5" or "6" or "7":
      t2Wrong()
    else:
      typingPrint("Please enter a valid option.\n")

def explainOSI():
  clearScreen()
  typingPrint("Nate: *sigh* \"You're pretty incompetent, you know that? Anyway, the OSI model or the Open Systems Interconnection is a more organized way to understand how network protocols and communication between devices works.\n")
  typingPrint("There are seven layers (starting from the bottom): Physical, Data Link, Network, Transport, Session, Presentation, Application. The data link layer packages the 1s and 0s from the physical layer into a nice frame. The network layer takes care of addressing messages to the right place.\n")
  typingPrint("This is where IP lies. The transport layer is responsible for making sure the IP packet arrives at its destination properly. The session layer establishes a session to send the messages over. The presentation layer formats data so it can be used by the application layer.\n")
  typingPrint("The application layer deals with the user interface of the software. Hopefully, you can use this knowledge to help troubleshoot the other computers. Let's get back to work now.\"\n")
  troubleshoot2()

def t1Right():
  clearScreen()
  typingPrint("Nate: \"Stellar! Let's move on to the next problem.\"\n")
  troubleshoot2()

def t1Wrong():
  clearScreen()
  global lives
  lives -= 1
  typingPrint("Nate: \"No, it should be bottom-up since we're dealing with a potentially physical layer issue.\nThe physical layer is the bottom layer of the OSI model and encapsulates all functionality of physical parts such as cabling, electronics, and Network Interface Cards.\nPlease don't tell me you need me to explain the OSI model.\"\n")
  explainOSI()

def troubleshoot1():
  clearScreen()
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
    elif userInput == "1" or "3":
      t1Wrong()
    else:
      typingPrint("Please enter a valid option.\n")

def level1Elevator():
  clearScreen()
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
  clearScreen()
  global lives
  lives -= 1
  typingPrint("Nate: \"No, it's definitely a type 2 hypervisor. The difference is that a type 1 hypervisor is installed directly onto the hardware of a server/computer.\"\n")
  typingPrint("However, a type 2 hypervisor is installed on the operating system. We are just trying to download a hypervisor on to her built computer in this case.\"\n")
  
def rightHypervisor():
  clearScreen()
  typingPrint("Nate: \"Awesome job! I award you a gold star for that.\"\n")
  level1Elevator()

def hypervisorQuestion():
  clearScreen()
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
  global name
  clearScreen()
  typingPrint(name + ": \"It's all finished!\"\n")
  typingPrint("Janet: \"Thank you so much!\"\n")
  typingPrint("Nate: \"What a star. Now... let's see if you can install the right hypervisor on her computer.\"\n")
  typingPrint("Our company operates on Linux, but she chose to have a Windows PC.\"\n")
  typingPrint("It is essentially a manager for virtual machines. A virtual machine is like a fake operating system.\"\n")
  typingPrint("It allows a user to use their PC on an operating system other than the natively installed one.\"\n")
  typingPrint("You can have multiple opened at a time, and ahypervisor is what manages these virtual machine instances.\"\n")
  hypervisorQuestion()


def brokenPC():
  clearScreen()
  global name
  global lives
  lives -= 1
  typingPrint("Janet: \"NOOOO, MY BEAUTIFUL PC. YOU ARE UNQUALIFIED. NATE, GET THEM OUT OF HERE!!!\"")
  typingPrint("Nate: \"Don't worry, Janet. We'll buy you a new one from " + name + "'s non-existent paycheck.\"\n")


def buildPC():
  clearScreen()
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
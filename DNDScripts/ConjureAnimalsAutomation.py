
import BeastAttacks

while True:
    # Prompt the user to enter the first number
    userInput = str(input("Enter [beast] [attack] [count] [adv/disadv/none]: "))

    if userInput.lower() == "":
        continue

    if userInput.lower() == 'list':
        print("Elk: ram, hooves")
        print("GiantVulture: multiattack")
        print("Rothe: gore")
        print("Snake: bite, constrict")
        print("Wolf: bite")
        continue
    if userInput.lower() == 'end':
        break

    # Input seperation
    inputArray = userInput.split()
    count = ""
    adv = ""
    
    beast = inputArray[0].lower()
    attack = inputArray[1].lower()
    if len(inputArray) > 2: count = inputArray[2].lower()
    if len(inputArray) > 3: adv = inputArray[3].lower()

    
    print(f"Input: {userInput}")
    if (beast == "wolf"):
        BeastAttacks.getWolfBiteAttack(count, adv)
    elif (beast == "snake"):
        BeastAttacks.getSnakeAttack(attack)
    elif (beast == "rothe"):
        BeastAttacks.getRotheGoreAttack(count, adv)
    elif (beast == "elk"):
        BeastAttacks.getElkAttack(attack)
    elif (beast == "giantvulture"):
        BeastAttacks.getGiantVultureMultiAttack(count, adv)
    else:
        print(f"Beast: {beast} not recognised")
    
print("Program ended")
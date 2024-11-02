
from Beasts import ConstrictorSnake, Elk, GiantPoisonousSnake, Wolf, Rothe, GiantVulture, Velociraptor, Rhino
import Colors


# Contants
AUTOMATION_COLOUR = Colors.GREEN
CRITICAL_HIT_TEXT = f"{Colors.RED}NAT 20!!{AUTOMATION_COLOUR}"
BUFFER_TEXT = f"Press ENTER or Input [adv/disadv] to generate next:"
SEQUENCE_END_TEXT = f"{Colors.YELLOW}End of Sequence{Colors.RESET}"


# Define maps for controlled inputs
ATTACK_MAP = {

    "elk": {
        "ram": lambda isAdv, count: Elk.getRamAttack(isAdv, count, CRITICAL_HIT_TEXT, AUTOMATION_COLOUR),
        "hooves": lambda isAdv, count: Elk.getHoovesAttack(isAdv, count, CRITICAL_HIT_TEXT, AUTOMATION_COLOUR),
    },
    "csnake": {
        "constrict": lambda isAdv, count: ConstrictorSnake.getConstrictAttack(isAdv, count, CRITICAL_HIT_TEXT, AUTOMATION_COLOUR),
        "bite": lambda isAdv, count: ConstrictorSnake.getBiteAttack(isAdv, count, CRITICAL_HIT_TEXT, AUTOMATION_COLOUR),
    },
    "wolf": {
        "bite": lambda isAdv, count: Wolf.getBiteAttack(isAdv, count, CRITICAL_HIT_TEXT, AUTOMATION_COLOUR)
    },
    "rothe": {
        "gore": lambda isAdv, count: Rothe.getGoreAttack(isAdv, count, CRITICAL_HIT_TEXT, AUTOMATION_COLOUR)
    },
    "giantvulture": {
        "multiattack": lambda isAdv, count: GiantVulture.getMultiAttack(isAdv, count, CRITICAL_HIT_TEXT, AUTOMATION_COLOUR)
    },
    "velociraptor": {
        "multiattack": lambda isAdv, count: Velociraptor.getMultiAttack(isAdv, count, CRITICAL_HIT_TEXT, AUTOMATION_COLOUR)
    },
    "rhino": {
        "gore": lambda isAdv, count: Rhino.getGoreAttack(isAdv, count, CRITICAL_HIT_TEXT, AUTOMATION_COLOUR)
    },
    "gpsnake": {
        "bite": lambda isAdv, count: GiantPoisonousSnake.getBiteAttack(isAdv, count, CRITICAL_HIT_TEXT, AUTOMATION_COLOUR)
    }



}

VALID_ADV_INPUTS = {"adv", "disadv", ""}


# Main Automation Sequence
while True:
    # Prompt the user to enter the first number
    userInput = str(input("Enter [beast] [attack]: "))

    if userInput.lower() == "":
        continue

    if userInput.lower() == 'list':
        for beast, attacks in ATTACK_MAP.items():
            # Join the attack options into a string separated by commas
            attack_list = ', '.join(attacks.keys())
            # Print the beast name and its attack options
            print(f"{beast.capitalize()}: {attack_list}")
        continue
    if userInput.lower() == 'exit':
        break

    # Input seperation
    inputArray = userInput.split()
    if len(inputArray) < 2:
        print ("You entered less than 2 words dumbass")
        continue
    
    beast = inputArray[0].lower()
    attack = inputArray[1].lower()

    def invokeBeastAttackFunction(beast, attack, isAdv, count):
        # retrieves the mapping of beast attacks 
        beastAttackMap = ATTACK_MAP.get(beast)
        # retrieves the specific function for the attack
        attackFunction = beastAttackMap.get(attack)
        # invokes the function by passing the other parameters into it
        attackFunction(isAdv, count)

    # Activating individual Beast Attacks
    if (beast not in ATTACK_MAP): # error handling
        print(f"{Colors.RED}Beast: {beast} not recognised{Colors.RESET}")
        continue
    beast_attack_map = ATTACK_MAP.get(beast)
    if (attack not in beast_attack_map): # error handling
        print(f"{Colors.RED}{beast} does not have an attack called: {attack}{Colors.RESET}")
        continue

    print(f"{Colors.BRIGHT_BLUE}Generating {Colors.RED}{beast} {attack}{Colors.BRIGHT_BLUE} Attacks{Colors.RESET}")
    count = 1
    while (True):
        isAdv = str(input(BUFFER_TEXT))
        isAdv = isAdv.lower()
        if (isAdv == "exit"):
            break
        if (isAdv not in VALID_ADV_INPUTS):
            print(f"isAdv value: {isAdv} not recognised, please try again!")
            continue
        invokeBeastAttackFunction(beast, attack, isAdv, count)
        count += 1
    print(SEQUENCE_END_TEXT)
        
    
print("Program ended")
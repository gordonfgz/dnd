
import DiceRolls

while True:
    # Prompt the user to enter the first number
    userInput = str(input("Enter [reps] [xdy] [adv/disadv/none]: "))

    if userInput.lower() == 'end':
        break

    # Input seperation
    inputArray = userInput.split()
    repsString = inputArray[0].lower()
    dices = inputArray[1].lower()
    adv = inputArray[2].lower()

    # important variables
    reps = 0
    numberOfDices = 0
    diceMaxValue = 0
    variablesCalibrated = False

    # analysing xdy
    if 'd' not in dices:
        print(f"[xdy] input of: {dices} is invalid")
        continue
    else:
        beforeD, d, afterD = dices.partition('d')
        if adv not in ("adv", "none", "disadv"):
            print("adv is not 'adv', 'none', or 'disadv'.")
            continue
        try:
            # Attempt to convert the input to an integer
            reps = int(repsString)
            numberOfDices = int(beforeD)
            diceMaxValue = int(afterD)
            variablesCalibrated = True
        except ValueError:
            print("Failed to convert input to an integer, either reps or xdy is incorrect.")
            continue

    if (variablesCalibrated):
        for i in range(reps): 
            currentRep = i+1
            finalValue = 0
            for i in range(numberOfDices):
                rollValue = DiceRolls.roll(diceMaxValue, adv)
                finalValue += rollValue
            print(f"[{currentRep}] Rolled {dices} for {finalValue}")

        print("<<< Roll sequence ended >>>")
    
        

    

    
print("Program ended")
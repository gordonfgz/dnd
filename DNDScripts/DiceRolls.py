import random
import Colors

def rollDamage(reps, diceRollFunction, diceValue):
    damage = 0
    for _ in range(reps):
        damage += diceRollFunction(diceValue)
    return damage

def roll(dice, adv):
    if (adv == ""):
        return rollD(dice)
    elif (adv == "adv"):
        return rollWithAdvD(dice)
    elif (adv == "disadv"):
        return rollWithDisadvD(dice)
    else:
        print(f"Roll mode {adv} not recognised")


def rollD(n):
    return random.randint(1, n)

def rollWithAdvD(n):
    firstRoll = rollD(n)
    secondRoll = rollD(n)

    if (firstRoll > secondRoll):
        print(f"rolled with Adv: [{Colors.YELLOW}{firstRoll}{Colors.RESET}, {secondRoll}]")
    elif (secondRoll > firstRoll):
        print(f"rolled with Adv: [{firstRoll}, {Colors.YELLOW}{secondRoll}{Colors.RESET}]")
    else:
        print(f"rolled with Adv: [{Colors.YELLOW}{firstRoll}{Colors.RESET}, {Colors.YELLOW}{secondRoll}{Colors.RESET}]")

    return  max(firstRoll, secondRoll)

def rollWithDisadvD(n):
    firstRoll = rollD(n)
    secondRoll = rollD(n)

    if (firstRoll < secondRoll):
        print(f"rolled with Disadv: [{Colors.YELLOW}{firstRoll} {Colors.RESET}, {secondRoll}]")
    elif (secondRoll < firstRoll):
        print(f"rolled with Adv: [{firstRoll}, {Colors.YELLOW}{secondRoll}{Colors.RESET}]")
    else:
        print(f"rolled with Adv: [{Colors.YELLOW}{firstRoll}{Colors.RESET}, {Colors.YELLOW}{secondRoll}{Colors.RESET}]")
        
    return  min(firstRoll, secondRoll)
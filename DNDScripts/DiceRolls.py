import random

def roll(dice, adv):
    if (adv == "none"):
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
    return  max(firstRoll, secondRoll)

def rollWithDisadvD(n):
    firstRoll = rollD(n)
    secondRoll = rollD(n)
    return  min(firstRoll, secondRoll)
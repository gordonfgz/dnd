import DiceRolls


def calculateCritDamage(reps, diceRollFunction, diceValue):
    damage = 0
    for _ in range(reps):
        damage += diceRollFunction(diceValue)
    return damage

def getWolfBiteAttack(count, adv):
    print(f"*Generating Wolf Bite Attacks*")
    count = int(count)
    damageType = "piercing"
    toHit = 4
    for i in range(count):
        hitDice = DiceRolls.roll(20, adv)
        damageDice = DiceRolls.rollD(4) + DiceRolls.rollD(4) + 2
        critDamage = DiceRolls.rollD(4) + DiceRolls.rollD(4)
        if (hitDice == 20):
            damageDice = damageDice + calculateCritDamage(2, DiceRolls.rollD, 4)
            hitDice = "A CRITICAL!!"
        else:
            hitDice = hitDice + toHit
        print(f"Wolf {i+1} rolled {hitDice} for {damageDice} {damageType} damage")
    print("*Sequence Ended*")
            

def getSnakeAttack(attack, count, adv):
    print(f"*Generating Snake {attack} Attacks*")
    count = int(count)
    damageType = ""
    toHit = 4
    for i in range(count):
        hitDice = DiceRolls.roll(20, adv)
        damageDice = 0
        critDamage = 0
        if (attack == "constrict"):
            damageDice = DiceRolls.rollD(8) + 2
            critDamage = calculateCritDamage(1, DiceRolls.rollD, 8)
            damageType = "bludgeoning"
        elif (attack == "bite"):
            damageDice = DiceRolls.rollD(6) + 2
            critDamage = calculateCritDamage(1, DiceRolls.rollD, 6)
            damageType = "piercing"
        else:
            print(f"Snake attack type: [{attack}] not recognized")
            return
        if (hitDice == 20):
            damageDice += critDamage
            hitDice = "A CRITICAL!!"
        else:
            hitDice = hitDice + toHit
        print(f"Snake {i+1} rolled {hitDice} for {damageDice} {damageType} damage")
    print("*Sequence Ended*")

def getRotheGoreAttack(count, adv):
    print(f"*Generating Rothe Gore Attacks*")
    count = int(count)
    damageType = "piercing"
    toHit = 6
    for i in range(count):
        hitDice = DiceRolls.roll(20, adv)
        damageDice = DiceRolls.rollD(6) + 4
        chargeDamage = DiceRolls.rollD(6) + DiceRolls.rollD(6)
        critDamage = calculateCritDamage(1, DiceRolls.rollD, 6)
        chargeCritDamage = calculateCritDamage(2, DiceRolls.rollD, 6)
        if (hitDice == 20):
            damageDice += critDamage
            chargeDamage += chargeCritDamage
            hitDice = "A CRITICAL!!"
        else:
            hitDice = hitDice + toHit
        print(f"Rothe {i+1} rolled {hitDice} for {damageDice} ({damageDice + chargeDamage} if charge) {damageType} damage")
    print("*Sequence Ended*")

def getElkAttack(attack, count, adv):
    print(f"*Generating Elk {attack} Attacks*")
    count = int(count)
    damageType = ""
    toHit = 5
    for i in range(count):
        hitDice = DiceRolls.roll(20, adv)
        damageDice = 0
        critDamage = 0
        chargeDamage = DiceRolls.rollD(6) + DiceRolls.rollD(6)
        chargeCritDamage = calculateCritDamage(2, DiceRolls.rollD, 6) 
        # checking attack type
        if (attack == "ram"):
            damageDice = DiceRolls.rollD(6) + 3
            critDamage = DiceRolls.rollD(6)
            damageType = "bludgeoning"
        elif (attack == "hooves"):
            damageDice = DiceRolls.rollD(4) + DiceRolls.rollD(4) + 3
            critDamage = calculateCritDamage(2, DiceRolls.rollD, 4)
            damageType = "bludgeoning"
        else:
            print(f"Elk attack type: [{attack}] not recognized")
            return
        # checking crit
        if (hitDice == 20):
            damageDice += critDamage
            chargeDamage += chargeCritDamage
            hitDice = "A CRITICAL!!"
        else:
            hitDice = hitDice + toHit
        # print differs for each attack type
        if (attack == "ram"):
            print(f"Elk {i+1} rolled {hitDice} for {damageDice} ({damageDice+chargeDamage}) {damageType} damage.")
        else:
            print(f"Elk {i+1} rolled {hitDice} for {damageDice} {damageType} damage.")
    print("*Sequence Ended*")

def getGiantVultureMultiAttack(count, adv):
    print(f"*Generating Giant Vulture MultiAttacks*")
    count = int(count)
    damageType1 = "piercing"
    damageType2 = "slashing"
    toHit = 4
    for i in range(count):
        hitDice1 = DiceRolls.roll(20, adv)
        hitDice2 = DiceRolls.roll(20, adv)
        damageDice1 = DiceRolls.rollD(4) + DiceRolls.rollD(4) + 2
        critDamage1 = calculateCritDamage(2, DiceRolls.rollD, 4)
        damageDice2 = DiceRolls.rollD(6) + DiceRolls.rollD(6) + 2
        critDamage2 = calculateCritDamage(2, DiceRolls.rollD, 6)
        # first attack
        if (hitDice1 == 20):
            damageDice1 += critDamage1
            hitDice1 = "A CRITICAL!!"
        else:
            hitDice1 = hitDice1 + toHit
        # second attack
        if (hitDice2 == 20):
            damageDice2 += critDamage2
            hitDice2 = "A CRITICAL!!"
        else:
            hitDice2 = hitDice2 + toHit



        print(f"G.Vulture {i+1} rolled {hitDice1} for {damageDice1} {damageType1} damage and {hitDice2} for {damageDice2} {damageType2} damage")
    print("*Sequence Ended*")
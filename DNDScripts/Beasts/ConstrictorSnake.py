import DiceRolls
import CritDamageCalculator
import Colors

def getConstrictAttack(isAdv, count, CRITICAL_HIT_TEXT, AUTOMATION_COLOUR):
    # standard stuff
    hitDice = DiceRolls.roll(20, isAdv)
    toHit = 4
    damageDice = DiceRolls.rollD(8) + 2
    critDamage = CritDamageCalculator.calculateCritDamage(1, DiceRolls.rollD, 8)
    damageType = "bludgeoning"
    if (hitDice == 20):
        damageDice += critDamage
        hitDice = CRITICAL_HIT_TEXT
    else:
        hitDice = hitDice + toHit
    print(f"{AUTOMATION_COLOUR}Snake {count} rolled {Colors.YELLOW}{hitDice}{AUTOMATION_COLOUR} for {Colors.RED}{damageDice}{AUTOMATION_COLOUR} {damageType} damage{Colors.YELLOW} [on hit auto grapple + restrain (DC14 to escape)]{Colors.RESET}")


def getBiteAttack(isAdv, count, CRITICAL_HIT_TEXT, AUTOMATION_COLOUR):
    # standard stuff
    hitDice = DiceRolls.roll(20, isAdv)
    toHit = 4
    damageDice = DiceRolls.rollD(6) + 2
    critDamage = CritDamageCalculator.calculateCritDamage(1, DiceRolls.rollD, 6)
    damageType = "piercing"
    if (hitDice == 20):
        damageDice += critDamage
        hitDice = CRITICAL_HIT_TEXT
    else:
        hitDice = hitDice + toHit
    print(f"{AUTOMATION_COLOUR}Snake {i} rolled {hitDice} for {damageDice} {damageType} damage{Colors.RESET}")
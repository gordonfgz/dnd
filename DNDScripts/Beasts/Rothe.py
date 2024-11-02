import DiceRolls
import CritDamageCalculator
import Colors

def getGoreAttack(isAdv, count, CRITICAL_HIT_TEXT, AUTOMATION_COLOUR):
    # standard
    damageType = "piercing"
    toHit = 6
    hitDice = DiceRolls.roll(20, isAdv)
    damageDice = DiceRolls.rollD(6) + 4
    critDamage = CritDamageCalculator.calculateCritDamage(1, DiceRolls.rollD, 6)
    # special
    chargeDamage = DiceRolls.rollD(6) + DiceRolls.rollD(6)
    chargeCritDamage = CritDamageCalculator.calculateCritDamage(2, DiceRolls.rollD, 6)
    # checking crit
    if (hitDice == 20):
        damageDice += critDamage
        chargeDamage += chargeCritDamage
        hitDice = CRITICAL_HIT_TEXT
    else:
        hitDice = hitDice + toHit
    print(f"{AUTOMATION_COLOUR}Rothe {count} rolled {hitDice} for {damageDice} ({damageDice + chargeDamage} if charge) {damageType} damage{Colors.RESET}")
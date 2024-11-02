import DiceRolls
import CritDamageCalculator
import Colors

def getGoreAttack(isAdv, count, CRITICAL_HIT_TEXT, AUTOMATION_COLOUR):
    # standard
    damageType = "bludgeoning"
    toHit = 7
    hitDice = DiceRolls.roll(20, isAdv)
    damageDice = DiceRolls.rollDamage(2, DiceRolls.rollD, 8) + 5
    critDamage = DiceRolls.rollDamage(2, DiceRolls.rollD, 8)
    # special
    chargeDamage = DiceRolls.rollDamage(2, DiceRolls.rollD, 8)
    chargeCritDamage = DiceRolls.rollDamage(2, DiceRolls.rollD, 8)
    # checking crit
    if (hitDice == 20):
        damageDice += critDamage
        chargeDamage += chargeCritDamage
        hitDice = CRITICAL_HIT_TEXT
    else:
        hitDice = hitDice + toHit
    print(f"{AUTOMATION_COLOUR}Rhino {count} rolled {Colors.YELLOW}{hitDice}{AUTOMATION_COLOUR} for {Colors.LIGHT_RED}{damageDice} ({damageDice + chargeDamage} if charge){AUTOMATION_COLOUR} {damageType} damage. {Colors.YELLOW} [on hit chance to prone (DC15 STR save)]{Colors.RESET}")
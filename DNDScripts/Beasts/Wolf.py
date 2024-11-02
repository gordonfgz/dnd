import DiceRolls
import CritDamageCalculator
import Colors

def getBiteAttack(isAdv, count, CRITICAL_HIT_TEXT, AUTOMATION_COLOUR):
    damageType = "piercing"
    toHit = 4
    hitDice = DiceRolls.roll(20, isAdv)
    damageDice = DiceRolls.rollD(4) + DiceRolls.rollD(4) + 2
    critDamage = DiceRolls.rollD(4) + DiceRolls.rollD(4)
    if (hitDice == 20):
        damageDice = damageDice + critDamage
        hitDice = CRITICAL_HIT_TEXT
    else:
        hitDice = hitDice + toHit
    print(f"{AUTOMATION_COLOUR}Wolf {count} rolled {hitDice} for {damageDice} {damageType} damage{Colors.YELLOW} [on hit chance to prone (DC11 STR save)]{Colors.RESET}")
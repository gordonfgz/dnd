import DiceRolls
import CritDamageCalculator
import Colors


def getBiteAttack(isAdv, count, CRITICAL_HIT_TEXT, AUTOMATION_COLOUR):
    # standard
    damageType = "piercing"
    toHit = 6
    hitDice = DiceRolls.roll(20, isAdv)
    damageDice = DiceRolls.rollDamage(1, DiceRolls.rollD, 4) + 4
    critDamage = DiceRolls.rollDamage(1, DiceRolls.rollD, 4)
    # special
    poisonDamage = DiceRolls.rollDamage(3, DiceRolls.rollD, 6)
    # checking crit
    if (hitDice == 20):
        damageDice += critDamage
        hitDice = CRITICAL_HIT_TEXT
    else:
        hitDice = hitDice + toHit
    print(f"{AUTOMATION_COLOUR}GiantPoisonousSnake {count} rolled {Colors.YELLOW}{hitDice}{AUTOMATION_COLOUR} for {Colors.LIGHT_RED}{damageDice}{AUTOMATION_COLOUR} {damageType} damage.{Colors.YELLOW} [DC11 Con save or take {Colors.LIGHT_RED}{poisonDamage}{Colors.YELLOW} or half on success]{Colors.RESET}")
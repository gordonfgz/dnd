import DiceRolls
import CritDamageCalculator
import Colors

def getRamAttack(isAdv, count, CRITICAL_HIT_TEXT, AUTOMATION_COLOUR):
    # standard stuff
    damageType = "bludgeoning"
    toHit = 5
    hitDice = DiceRolls.roll(20, isAdv)
    damageDice = DiceRolls.rollD(6) + 3
    ifCritBonusDamage = DiceRolls.rollD(6)
    # special charge bonus damage
    chargeDamage = DiceRolls.rollD(6) + DiceRolls.rollD(6)
    ifCritChargeBonusDamage = CritDamageCalculator.calculateCritDamage(2, DiceRolls.rollD, 6) 
    damageDice = DiceRolls.rollD(6) + 3
    # checking crit
    if (hitDice == 20):
        damageDice += ifCritBonusDamage
        chargeDamage += ifCritChargeBonusDamage
        hitDice = CRITICAL_HIT_TEXT
    else:
        hitDice = hitDice + toHit
    print(f"{AUTOMATION_COLOUR}Elk {count} rolled {hitDice} for {damageDice} ({damageDice+chargeDamage}) {damageType} damage.{Colors.YELLOW} [on hit chance to prone (DC13 STR save)]{Colors.RESET}")

def geHoovesAttack(isAdv, count, CRITICAL_HIT_TEXT, AUTOMATION_COLOUR):
    # standard stuff
    damageType = "bludgeoning"
    toHit = 5
    hitDice = DiceRolls.roll(20, isAdv)
    damageDice = DiceRolls.rollD(4) + DiceRolls.rollD(4) + 3
    ifCritBonusDamage = CritDamageCalculator.calculateCritDamage(2, DiceRolls.rollD, 4)
    # checking crit
    if (hitDice == 20):
        damageDice += ifCritBonusDamage
        hitDice = CRITICAL_HIT_TEXT
    else:
        hitDice = hitDice + toHit
    print(f"{AUTOMATION_COLOUR}Elk {count} rolled {hitDice} for {damageDice} {damageType} damage.{Colors.RESET}")
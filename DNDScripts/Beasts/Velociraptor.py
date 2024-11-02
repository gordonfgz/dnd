import DiceRolls
import CritDamageCalculator
import Colors

def getMultiAttack(isAdv, count, CRITICAL_HIT_TEXT, AUTOMATION_COLOUR):
    print(f"*Generating Giant Vulture MultiAttacks*")
    count = int(count)
    damageType1 = "piercing"
    damageType2 = "slashing"
    toHit = 4
    hitDice1 = DiceRolls.roll(20, isAdv)
    hitDice2 = DiceRolls.roll(20, isAdv)
    damageDice1 = DiceRolls.rollD(6) + 2
    critDamage1 = CritDamageCalculator.calculateCritDamage(1, DiceRolls.rollD, 6)
    damageDice2 = DiceRolls.rollD(4) + 2
    critDamage2 = CritDamageCalculator.calculateCritDamage(1, DiceRolls.rollD, 4)
    # first attack
    if (hitDice1 == 20):
        damageDice1 += critDamage1
        hitDice1 = CRITICAL_HIT_TEXT
    else:
        hitDice1 = hitDice1 + toHit
    # second attack
    if (hitDice2 == 20):
        damageDice2 += critDamage2
        hitDice2 = CRITICAL_HIT_TEXT
    else:
        hitDice2 = hitDice2 + toHit

    print(f"{AUTOMATION_COLOUR}Velociraptor {count} rolled {Colors.YELLOW}{hitDice1}{AUTOMATION_COLOUR} for {Colors.LIGHT_RED}{damageDice1} {damageType1} damage{AUTOMATION_COLOUR} and {Colors.YELLOW}{hitDice2}{AUTOMATION_COLOUR} for {Colors.LIGHT_RED}{damageDice2} {damageType2} damage{Colors.RESET}")
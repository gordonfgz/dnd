import DiceRolls
import CritDamageCalculator

# ANSI escape codes for text colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"  # Reset color back to default

# Constants
AUTOMATION_COLOUR = GREEN
CRITICAL_HIT_TEXT = f"{RED}NAT 20!!{AUTOMATION_COLOUR}"
BUFFER_TEXT = f"Press Enter to generate next:"
SEQUENCE_END_TEXT = f"{YELLOW}End of Sequence{RESET}"



def getWolfBiteAttack(adv):
    damageType = "piercing"
    toHit = 4
    hitDice = DiceRolls.roll(20, adv)
    damageDice = DiceRolls.rollD(4) + DiceRolls.rollD(4) + 2
    critDamage = DiceRolls.rollD(4) + DiceRolls.rollD(4)
    if (hitDice == 20):
        damageDice = damageDice + CritDamageCalculator.calculateCritDamage(2, DiceRolls.rollD, 4)
        hitDice = CRITICAL_HIT_TEXT
    else:
        hitDice = hitDice + toHit
    print(f"{AUTOMATION_COLOUR}Wolf {i+1} rolled {hitDice} for {damageDice} {damageType} damage{RESET}")

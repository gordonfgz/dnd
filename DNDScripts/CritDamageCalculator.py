def calculateCritDamage(reps, diceRollFunction, diceValue):
    damage = 0
    for _ in range(reps):
        damage += diceRollFunction(diceValue)
    return damage
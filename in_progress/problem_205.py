from itertools import product

def calculate_probability():
    peter_dice = [1, 2, 3, 4] * 9
    colin_dice = [1, 2, 3, 4, 5, 6] * 6

    peter_wins = 0
    total_outcomes = 0

    for outcome_peter in product(peter_dice, repeat=9):
        for outcome_colin in product(colin_dice, repeat=6):
            total_outcomes += 1
            if sum(outcome_peter) > sum(outcome_colin):
                peter_wins += 1

    probability = peter_wins / total_outcomes
    return probability

result = calculate_probability()
print(f"The probability that Pyramidal Peter beats Cubic Colin is approximately {result:.7f}")

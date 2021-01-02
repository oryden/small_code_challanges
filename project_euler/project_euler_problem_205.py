"""
https://projecteuler.net/problem=205

Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3, 4.
Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5, 6.

Peter and Colin roll their dice and compare totals: the highest total wins. The result is a draw if the totals are equal.

What is the probability that Pyramidal Pete beats Cubic Colin? Give your answer rounded to seven decimal places in the form 0.abcdefg
"""
import numpy as np


def calculate_pdf_dice(nr_side_of_dice, nr_dice):
    """"
    Help function that calculates the PDF of one dice player
    """
    max_score = nr_dice*nr_side_of_dice
    nr_possible_combinations = nr_side_of_dice**nr_dice

    outcome_frequency = np.zeros(max_score)
    dice_outcome_vector = np.ones(nr_dice)

    # Loop over all possible combination of dice to calculate the outcome frequency
    for i in range(0, nr_possible_combinations):
        outcome_result = dice_outcome_vector.sum()
        outcome_frequency[int(outcome_result - 1)] = outcome_frequency[int(outcome_result - 1)] + 1
        # Used to have a flexible way to have nested for-loops [decided by number of dice and side of dice]
        for dice_nr in range(0, nr_dice):
            updated_other_dice = False

            # Criteria to see if wone of the dice to the right shall have an updated value
            criteria_1 = dice_outcome_vector[0:dice_nr+1].sum() == nr_side_of_dice*(dice_nr+1)
            if dice_nr+1 < nr_dice:
                criteria_2 = dice_outcome_vector[dice_nr+1] != nr_side_of_dice
            else:
                criteria_2 = True

            # update dice to the right if all the dice to the left have maximum value (see criteria above)
            if criteria_1 and criteria_2 and i < nr_possible_combinations-1:
                dice_outcome_vector[0:dice_nr + 1] = 1
                dice_outcome_vector[dice_nr + 1] = dice_outcome_vector[dice_nr + 1] + 1
                updated_other_dice = True
                break
        # if not update dice to the right - update dice to the left
        if not updated_other_dice:
            dice_outcome_vector[0] = dice_outcome_vector[0] + 1

    # calculate the PDF funciton by taking the frequency/number of possible outcomes
    pdf_vector = outcome_frequency/outcome_frequency.sum()

    return pdf_vector

if __name__ == '__main__':
    peter_pdf = calculate_pdf_dice(nr_side_of_dice=4, nr_dice=9)
    colin_pdf = calculate_pdf_dice(nr_side_of_dice=6, nr_dice=6)

    # calculate probability that peter wins using conditional probabilities
    culumtative_win_peter = 0
    for i in range(0, len(peter_pdf)):
        culumtative_win_peter += colin_pdf[0:i].sum() * peter_pdf[i]

    print("probability win peter: {}".format(culumtative_win_peter))
import random


def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3
    balls of the same color were drawn in the first 3 draws.
    '''

    sameColor = 0
    for i in range(numTrials):
        balls = [0, 0, 0, 0, 1, 1, 1, 1]
        selection = []
        for j in range(3):
            choice = random.randint(0, len(balls)-1)
            selection.append(balls[choice])
            del balls[choice]
        if all(i == 0 for i in selection) or all(i == 1 for i in selection):
            sameColor += 1

    return sameColor/numTrials

print(drawing_without_replacement_sim(10000))

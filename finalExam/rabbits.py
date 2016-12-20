import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30


def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP
    currentRabbitPopCopy = CURRENTRABBITPOP

    for rabbit in range(currentRabbitPopCopy):
        if 10 < CURRENTRABBITPOP < MAXRABBITPOP:
            reproduce = random.random()
            if reproduce <= (1 - CURRENTRABBITPOP/MAXRABBITPOP):
                CURRENTRABBITPOP += 1


def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    currentFoxPopCopy = CURRENTFOXPOP

    for fox in range(currentFoxPopCopy):
        if 10 < CURRENTRABBITPOP:
            eatRabbitPop = random.random()
            if eatRabbitPop <= CURRENTRABBITPOP/MAXRABBITPOP:
                CURRENTRABBITPOP -= 1
                reproducePop = random.random()
                if reproducePop <= 1/3:
                    CURRENTFOXPOP += 1
            foxDiePop = random.random()
            if foxDiePop <= 0.1:
                CURRENTFOXPOP -= 1

            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """
    rabbit_populations = []
    fox_populations = []
    for step in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbit_populations.append(CURRENTRABBITPOP)
        fox_populations.append(CURRENTFOXPOP)

    return rabbit_populations, fox_populations


if __name__ == '__main__':
    rabbitPops, foxPops = runSimulation(200)
    timeSteps = []
    for i in range(200):
        timeSteps.append(i)

    pylab.plot(timeSteps, rabbitPops)
    pylab.plot(timeSteps, foxPops)
    pylab.title('rabbit and fox simulation')
    pylab.xlabel('Time step')
    pylab.ylabel('# of animal')


    rabbitModel = pylab.polyfit(timeSteps, rabbitPops, 2)
    estRabbitPops = pylab.polyval(rabbitModel, timeSteps)
    pylab.plot(timeSteps, estRabbitPops, label='rabbit pops 2nd order poly fit')
    foxModel = pylab.polyfit(timeSteps, foxPops, 2)
    estFoxPops = pylab.polyval(foxModel, timeSteps)
    pylab.plot(timeSteps, estFoxPops, label='fox pops 2nd order poly fit')

    pylab.show()

import random as rd
import matplotlib.pyplot as plt
import Coursework_Funs as fnc


#Task 2
#This will simulate evolving a generated text, D, 10,000 times and monitoring its score the more it 'evolves'.

experiment = fnc.genRANDText()
scores_experiment = []
for i in range(10000):

    scores_experiment.append(fnc.score(experiment))
    if experiment != fnc.DESIRED_SENTENCE:
        experiment = fnc.evolution(experiment, 1) #Am using the second version of evolution here, however using a mutation rate of 1 is equivelent.


plt.plot(scores_experiment)
plt.title("Score of a text over a series of 'evolutions'")
plt.xlabel("Evolutions")
plt.ylabel("Score of the text")
plt.show()

#This creates a very interesting graph. Sort of similar looking to a CDF of an exponential (1-e^-cx). Only our graph spans values above 1.
# --> if this graph was continuous, then it probably has a derivative = pdf of a random variable X~exponential(c) thus
# telling us the rate of the graph we produced.
# We do need to run enough iterations for this to confirm our conjecture of course though...

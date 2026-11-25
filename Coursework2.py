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



#Mean referred to in the report
score_at_number = []
for i in range(4000):
    sentence = fnc.genRANDText()
    lis = []
    for j in range(200):
        lis.append(fnc.score(sentence))
        sentence = fnc.evolution(sentence, 1)
    score_at_number.append(lis[-1])

print(sum(score_at_number) / len(score_at_number))




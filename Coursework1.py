### Coursework-1 ###
import random as rd
import math
import matplotlib.pyplot as plt
import Coursework_Funs as fnc

#---------------------------------------------------------------------------------------------------------------------------------------------------
#TASK 1


#Now we will use this while-loop to see if we can generate the DESIRED_SENTENCE.

attempt_scores = []
i = 0

while i < 10000: #limits trials to 10000
    """
    Adds the score for each trial of 'random_sentence' to a list, attempt_scores
    """
    the_score = fnc.score(fnc.genRANDText())
    attempt_scores.append(the_score)

    if the_score == len(fnc.DESIRED_SENTENCE):
      break  

    i += 1

#Will generate a graph showcasing the pmf of our results from a dictionary 'score_counter' made below from the list 'attempt_scores'
score_counter = {}
for i in range(len(attempt_scores)):
    if attempt_scores[i] in score_counter:
        score_counter[attempt_scores[i]] += 1
    else:
        score_counter[attempt_scores[i]] = 1

#average, best and worst scores
average_score = sum(attempt_scores) / len(attempt_scores)
best_score = max(attempt_scores)
worst_score =  min(attempt_scores)

plt.subplots(figsize=(5, 3))

x_values = score_counter.keys()
y_values = score_counter.values()
plt.bar(x_values, y_values)
# plt.title(f"Iterations = 10000", "Highest Score = ", "Lowest Score")
plt.title(
    f"Histogram of Random Sentences\nMean = {average_score}, Best Score = {best_score}, Worst Score = {worst_score}"
)
plt.xlabel("Score of the random_sentence")
plt.ylabel("Frequency of Score")
plt.show()

# We will plot our values against a binomial distributions, using paramaters n = 62 trials and probability 1/28 as each character can take one of 28 options
n, p = 62, 1/28
pmf = [math.comb(n, k) * p**k * (1-p)**(n-k) for k in range(n+1)]

plt.hist(attempt_scores, bins=range(max(attempt_scores) + 2), align="left", rwidth=0.8, density=True, label="Simulation")
plt.plot(range(n+1), pmf, "ro-", label="Theorised Binomial")
plt.xlim(-1, max(attempt_scores) + 2)
plt.xlabel("Score")
plt.ylabel("Relative Frequency")
plt.title("Relative Frequency Vs Binomial~(62,1/28)")
plt.legend()
plt.show()



        

        
        

            
    





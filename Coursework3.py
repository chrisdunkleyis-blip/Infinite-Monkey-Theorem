import random as rd
import matplotlib.pyplot as plt
import Coursework_Funs as fnc


#Task 3

#take a random_sentence and analyse how the mutation rate effects the runs needed to obtain our DESIRED_SENTENCE

random_sentence = fnc.genRANDText()
for i in range(1, len(random_sentence) + 1):
    scores_random_sentence = []
    evo = random_sentence
    for j in range(9000):
        evo = fnc.evolution(evo, i)
        scores_random_sentence.append(fnc.score(evo))
    plt.bar(i, scores_random_sentence[-1])
plt.title("How mutation_rate effects the score after 9000 loops")
plt.xlabel("Mutation_rate")
plt.ylabel("Score after loops")
plt.show()


#2
#Idea is to reward the variations with another 'score' the closer the i-th letter is to the desired i-th letter. 
#The reason for this is because evolution is driven by natural selection, and not rewarding an animal when they have a close trait
# to the one desired is false.
#So if we were rewarding, we would do it like so:
# example random_sentence:
#              "duqehfg dhquex"
#Target sentence:
#              "two is a prime"
#for our first letter 'd' in random_sentence, we will want to obtain somwthing in theory 'closer' to the desired letter, 't' and 
# then reward the string with a higher score based on how close the mutated characters are to the desired one.


#showcases 50 different random_sentences' closeness_score on a bar chart
ls = []

for i in range(50):
    sentence = fnc.genRANDText()
    ls.append(fnc.closeness(sentence))
    plt.bar(i, ls[-1])
print("Average score: ", sum(ls) / len(ls))
print("Best score: ", max(ls))
print("Worst score: ", min(ls))
plt.title("Closeness of random_sentence")
plt.xlabel("random_sentence")
plt.ylabel("Closeness")
plt.show()


#Now will take into account evolution and how mutation rate changes the closeness_score of a random_sentence

random_sentence = fnc.genRANDText()
for i in range(1, len(random_sentence) + 1):
    new_score_rand = []
    evo = random_sentence
    for j in range(5000):
        evo = fnc.evolution(evo, i)
        new_score_rand.append(fnc.closeness(evo))
    plt.bar(i, new_score_rand[-1])
    
plt.title("Closeness of the string")
plt.xlabel("Mutation rate")
plt.ylabel("Average closeness")
plt.show()

#Now with this we can apply the theory of a selection pressure further. Lets say we have 50 different strings (characters),
# We want to keep the ones that have a closeness_score lower than average (as the others did not have a trait which they needed to survive)
# and then mutate them with a mutation rate of 1 - this is because we have seen that this achieves a higher score (lower closeness_score)
# across iterations. We will then see the score of the overall survivor (of the fittest)
# - limitation: each survivor reproduces asexually and produces one mutated offspring.




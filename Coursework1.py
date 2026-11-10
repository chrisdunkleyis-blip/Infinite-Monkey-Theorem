### Coursework-1 ###
import random as rd
import matplotlib.pyplot as plt


#-----------------------------------------------------------------------------------------------------------------------------------------
#TASK 1

DESIRED_SENTENCE = "he who seeks rest finds boredom. he who seeks work finds rest."

def genRANDText():
    """
    First we created a list of our 28 character alphabet, 'characters'. Using this and the random library, we can
    randomly select a character ('random_character') and add it to our 'random_sentence' - we do this while making sure
    that we are selecting a 'random_character' each time we run the for-loop.
    """
    characters = [" ", ".", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", 
                  "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    
    random_sentence = ""
    
    for i in range(62):
        random_character = rd.choice(characters)
        random_sentence += random_character

    return random_sentence


def score(attempt: str):
    """
    Function which decides how many i-th characters from our 'attempt' sentence is equal to the i-th character
    of the 'DESIRED_SENTENCE' using a for-loop.
    incrememts 'the_score' by 1 when a matching i-th character is found.
    """
    the_score = 0

    for i in range(len(attempt)):
        if DESIRED_SENTENCE[i] == attempt[i]:
            the_score += 1

    return the_score


#------------------------------------------------------------------------------------------------------------------------------------------

#Now we will use this while-loop to see if we can generate the DESIRED_SENTENCE.

attempt_scores = []
i = 0

while i < 10000: #limits trials to 10000
    """
    Adds the score for each trial of 'random_sentence' to a list, attempt_scores
    """
    the_score = score(genRANDText())
    attempt_scores.append(the_score)

    if the_score == len(DESIRED_SENTENCE):
      break  

    i += 1

#Will generate a graph showcasing the pmf of our results from a dictionary 'score_counter' made below from the list 'attempt_scores'
score_counter = {}
for i in range(len(attempt_scores)):
    if attempt_scores[i] in score_counter:
        score_counter[attempt_scores[i]] += 1
    else:
        score_counter[attempt_scores[i]] = 1


x_values = score_counter.keys()
y_values = score_counter.values()
plt.bar(x_values, y_values)
plt.title("Histogram of random_sentences")
plt.xlabel("Score of the random_sentence")
plt.ylabel("Frequency of Score")
plt.show()

#Now printing the average, best and worst scores
print("Average score: ", sum(attempt_scores) / len(attempt_scores))
print("Best score: ", max(attempt_scores))
print("Worst score: ", min(attempt_scores))

#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
#TASK 2

def evolution(S: str):
    """
    This function takes a random character in S, randomises it (and subsequently) makes a copy of S, called new_S. 
    We then compare the score of S and new_S to see if S as a result of the randomisation has 'evolved' 
    """

    #As a remeinder, these are the 28 characters we choose from;
    characters = [" ", ".", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", 
                  "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    
    random_element = rd.randint(0, 61)
    new_S = S[0: random_element] + rd.choice(characters) + S[random_element + 1:]

    if score(new_S) > score(S):
        return new_S
    else:
        return S


#This will simulate evolving a generated text, D, 10,000 times and monitoring its score the more it 'evolves'.

experiment = genRANDText()
scores_experiment = []
for i in range(10000):

    scores_experiment.append(score(experiment))
    if experiment != DESIRED_SENTENCE:
        experiment = evolution(experiment)


plt.plot(scores_experiment)
plt.title("Score of a text over a series of 'evolutions'")
plt.xlabel("Evolutions")
plt.ylabel("Score of the text")
plt.show()

#This creates a very interesting graph. Sort of similar looking to a CDF of an exponential (1-e^-cx). Only our graph spans values above 1.
# --> if this graph was continuous, then it probably has a derivative = pdf of a random variable X~exponential(c) thus
# telling us the rate of the graph we produced.
# We do need to run enough iterations for this to confirm our conjecture of course though...


#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
# TASK 3

#1
def evolution(S: list, mutation_rate: int): 
    """
    We are creating a function which 'evolves' our random_sentence with a 'mutation_rate'. The mutation rate is a trait of
    our 'evolution' function that we 'evolve' x = 'mutation_rate' number of characters inside the random_sentence.
    From this we can also imply that each randomised numbered element we are attempting to 'evolve' is not the same element  
    that we randomise again when the mutation_rate > 1.
    """

    characters = [" ", ".", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", 
                  "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


    randomised_indices = []
    for i in range(mutation_rate):
            while True:
                test = rd.randint(0, 61)
                if test not in randomised_indices:
                    randomised_indices.append(test)
                    break

    new_S = S
    for j in range(len(randomised_indices)):
        new_S = new_S[0: randomised_indices[j]] + rd.choice(characters) + new_S[randomised_indices[j] + 1:]

    if score(new_S) > score(S):
        return new_S
    else:
        return S
    
# Now we take a random_sentence and analyse how the mutation rate effects the runs needed to obtain our DESIRED_SENTENCE

random_sentence = genRANDText()
for i in range(1, len(random_sentence) + 1):
    scores_random_sentence = []
    evo = random_sentence
    for j in range(9000):
        evo = evolution(evo, i)
        scores_random_sentence.append(score(evo))
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
#
#

def closeness_score(attempt: str):
    """
    idea is to reward the closeness to a desired letter from an attempt on a scale of 1-28 (28 being the worst). The lower the score, the better.
    """
    characters = [" ", ".", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", 
                  "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    
    score = 0 
    for i in range(len(attempt)):
        difference = abs( characters.index(DESIRED_SENTENCE[i]) - characters.index(attempt[i]) )
        score += difference

    return score

ls = []

for i in range(50):
    sentence = genRANDText()
    ls.append(closeness_score(sentence))
    plt.bar(i, ls[-1])

plt.show()


        

        
        

            
    





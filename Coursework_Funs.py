import random as rd
import matplotlib.pyplot as plt



DESIRED_SENTENCE = "he who seeks rest finds boredom. he who seeks work finds rest."

CHARACTERS = [" ", ".", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", 
              "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def genRANDText():
    """
    First we created a list of our 28 character alphabet, 'characters'. Using this and the random library, we can
    randomly select a character ('random_character') and add it to our 'random_sentence' - we do this while making sure
    that we are selecting a 'random_character' each time we run the for-loop.
    """
    
    random_sentence = ""
    
    for i in range(62):
        random_character = rd.choice(CHARACTERS)
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


def evolution(S: str):
    """
    This function takes a random character in S, randomises it (and subsequently) makes a copy of S, called new_S. 
    We then compare the score of S and new_S to see if S as a result of the randomisation has 'evolved' 
    """

    
    random_element = rd.randint(0, 61)
    new_S = S[0: random_element] + rd.choice(CHARACTERS) + S[random_element + 1:]

    if score(new_S) > score(S):
        return new_S
    else:
        return S


def evolution(S: list, mutation_rate: int): 
    """
    We are creating a function which 'evolves' our random_sentence with a 'mutation_rate'. The mutation rate is a trait of
    our 'evolution' function that we 'evolve' x = 'mutation_rate' number of characters inside the random_sentence.
    From this we can also imply that each randomised numbered element we are attempting to 'evolve' is not the same element  
    that we randomise again when the mutation_rate > 1.
    """


    randomised_indices = []
    for i in range(mutation_rate):
            while True:
                test = rd.randint(0, 61)
                if test not in randomised_indices:
                    randomised_indices.append(test)
                    break

    new_S = S
    for j in range(len(randomised_indices)):
        new_S = new_S[0: randomised_indices[j]] + rd.choice(CHARACTERS) + new_S[randomised_indices[j] + 1:]

    if score(new_S) > score(S):
        return new_S
    else:
        return S



def closeness(attempt: str):
    """
    idea is to find the mean closeness to a desired letter from a character from attempt on a scale of 1-28 (28 being the worst). The lower the score, the better.
    """
    
    score = 0 
    for i in range(len(attempt)):
        difference = abs( CHARACTERS.index(DESIRED_SENTENCE[i]) - CHARACTERS.index(attempt[i]) ) / len(attempt)
        score += difference

    return score
    
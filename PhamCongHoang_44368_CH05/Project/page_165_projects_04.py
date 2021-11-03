"""
Author: pham cong hoang
Date:09/10/2021
Problem:
Make the following modifications to the original sentence-generator program:
a. The prepositional phrase is optional. (It can appear with a certain
probability.)
b. A conjunction and a second independent clause are optional: The boy took a
drink and the girl played baseball.
c. An adjective is optional: The girl kicked the red ball with a sore foot.
You should add new variables for the sets of adjectives and conjunctions

Solution:
import random

articles = ("A", "THE")
nouns = ("BOY", "GIRL", "BAT", "BALL",)
verbs = ("HIT", "SAW", "LIKED")
prepositions = ("WITH", "BY")

def nounPhrase():
    return random.choice(articles) + " " + random.choice(nouns)
print(nounPhrase())
def prepositionalPhrase():
    return random.choice(prepositions) + " " + nounPhrase()
print(prepositionalPhrase())
def verbPhrase():
    return random.choice(verbs) + " " + nounPhrase() + " " + prepositionalPhrase()
print(verbPhrase())
def sentence():
    return nounPhrase() + " " + verbPhrase()
print(sentence())



"""
import random

articles = ("A", "THE")
nouns = ("BOY", "GIRL", "BAT", "BALL",)
verbs = ("HIT", "SAW", "LIKED")
prepositions = ("WITH", "BY")

def nounPhrase():
    return random.choice(articles) + " " + random.choice(nouns)
print(nounPhrase())
def prepositionalPhrase():
    return random.choice(prepositions) + " " + nounPhrase()
print(prepositionalPhrase())
def verbPhrase():
    return random.choice(verbs) + " " + nounPhrase() + " " + prepositionalPhrase()
print(verbPhrase())
def sentence():
    return nounPhrase() + " " + verbPhrase()
print(sentence())

"""
Author: pham cong hoang
Date:09/10/2021
Problem:Generating Sentences

Solution:
Sentences in any language have a structure defined by a grammar. They also include
a set of words from the vocabulary of the language. The vocabulary of a language
like English consists of many thousands of words, and the grammar rules are quite
complex. For the sake of simplicity our program will generate sentences from a simplified subset of English. The vocabulary will consist of sample words from several
parts of speech, including nouns, verbs, articles, and prepositions. From these words,
you can build noun phrases, prepositional phrases, and verb phrases. From these
constituent phrases, you can build sentences. For example, the sentence “The girl hit
the ball with the bat” contains three noun phrases, one verb phrase, and one prepositional phrase. Table 5-3 summarizes the grammar rules for our subset of English.


"""
import random
# Vocabulary: words in 4 different parts of speech
articles = ("A", "THE")
nouns = ("BOY", "GIRL", "BAT", "BALL")
verbs = ("HIT", "SAW", "LIKED")
prepositions = ("WITH", "BY")
def sentence():
 """Builds and returns a sentence."""
 return nounPhrase() + " " + verbPhrase()
def nounPhrase():
 """Builds and returns a noun phrase."""
 return random.choice(articles) + " " + random.choice(nouns)
def verbPhrase():
 """Builds and returns a verb phrase."""
 return random.choice(verbs) + " " + nounPhrase() + " " + \
 prepositionalPhrase()
def prepositionalPhrase():
 """Builds and returns a prepositional phrase."""
 return random.choice(prepositions) + " " + nounPhrase()
def main():
 """Allows the user to input the number of sentences
 to generate."""
 number = int(input("Enter the number of sentences: "))
 for count in range(number):
  print(sentence())
# The entry point for program execution
if __name__ == "__main__":
 main()
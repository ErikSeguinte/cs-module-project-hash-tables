import random
import re

# Read in all the words in one go
with open("applications/markov/input.txt") as f:
    words = f.read().split()

# TODO: analyze which words can follow other words
# Your code here
word_dict = {}
prev = words[0]

for word in words[1:]:
    if prev not in word_dict:
        word_dict[prev] = [word]
    else:
        word_dict[prev].append(word)

    prev = word

# TODO: construct 5 random sentences
# Your code here


capitals = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
def is_start_word(word):
    pos = 0
    if word[pos] == '"':
        pos = 1
    return word[pos] in capitals

punctuation = set(".!?")
def is_stop_word(word):
    pos = -1
    if word[pos] == '"':
        pos = -2
    return word[pos] in punctuation

num_sentences = 5

for _ in range(num_sentences):
    word = None
    while True:
        word = random.choice(words)
        if is_start_word(word):
            break

    print(word, end=" ")

    prev = word
    while True:
        word = random.choice(word_dict[prev])
        print(word, end=" ")
        if is_stop_word(word):
            break
        
        prev = word
    print()
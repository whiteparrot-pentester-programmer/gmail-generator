import random
import string
# get user input
num = int(input("\nHow much do you wan to gen Stelko> "))
# read word lists
with open('nouns.txt', encoding="utf8") as infile:
    nouns = infile.read().strip(' \n').split('\n')
with open('adjectives.txt', encoding="utf8") as infile:
    adjectives = infile.read().strip(' \n').split('\n')
#read censor list
with open('blacklist.txt', encoding="utf8") as inline:
    censored = inline.read().strip(' \n').split('\n')
# generate usernames
for i in range(num):

    # construct username
    word1 = random.choice(adjectives)
    word2 = random.choice(nouns)
    #check if word2 is censored
    if word2 in censored:
        i -=1
        continue
    #else make and print the username
    #captilaize first letter
    word1 =word1.title()
    word2 =word2.title()
    username = '{}{}{}'.format(word1, word2, random.randint(1, 999))

    # success
    print(username + "@gmail.com")

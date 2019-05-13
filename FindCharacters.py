# -*- coding: utf-8 -*-
import nltk
from collections import Counter
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def parse_names(names, matrix):
    queries = list()
    for i in range(len(names)):
    




file_content = open("sense1.txt").read()
tokens = nltk.word_tokenize(file_content)
tagged = nltk.pos_tag(tokens)
titles = ("Mr", "Ms", "Miss", "Mrs", "Dr", "Madam", "Sir", "Lady", "Colonel", "Poor")
stops = ("!", ".", "?")

candidates = list()
prevs = dict()

prev_line = (" ", " ")
for line in tagged:
    token = line[0]
    if line[1] == "NNP":
        if not "." in token and not token in titles and not prev_line[0]in stops:
            candidates.append(token)
            if prev_line[1] == "NNP":
                if token in prevs:
                    prevs[token].append(prev_line[0])
                else:
                    prevs[token] = [prev_line[0]]
    prev_line = line

characters = Counter(candidates).most_common(10)
names = [x for x,y in characters]
final = names
for name in names:
    if name in prevs:
        associated = [x for x,y in Counter(prevs[name]).most_common(10) if y > 3 and x in candidates]
        final.extend(associated)
            
matrix = list()
for name in set(final):
    print(name)
    if name in prevs:
        matrix.append([x for x,y in Counter(prevs[name]).most_common(10) if y > 3])
    else:
        matrix.append([])
        
print(matrix)


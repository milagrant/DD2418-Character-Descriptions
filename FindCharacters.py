# -*- coding: utf-8 -*-
import re
import nltk
from collections import Counter
import string
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from Gen import gen_description

titles = ("Mr.", "Ms.", "Miss", "Mrs.", "Dr.", "Madam", "Sir", "Lady")
stops = string.punctuation

candidates = list()
prevs = dict()
prev_names = dict()
prev_titles = dict()
title_pairs = dict()
common_adj = list()

def find_common_adjectives(tagged):
    global common_adj
    adjectives = [t[0] for t in tagged if( t[1] == "JJ")]
    common_adj = [word for word,nr in Counter(adjectives).most_common(130)]
    
def find_names(tagged):
    prev = " "
    for line in tagged:
        token = line[0]
        tag = line[1]
        if token in prevs:
            candidates.append(token)
            if not prev in stops:
                prevs[token].append(prev)
        else:
            if tag == "NNP" and not prev in stops and not token in titles \
             and not "." in token and not "”" in token and not "“" in token \
             and not "’" in token:
                candidates.append(token)
                prevs[token] = [prev]
        prev = token
    return [word for word,nr in Counter(candidates).most_common(2)]
    
def find_prevs(characters):
    for c in characters:
        prev_names[c] = list()
        prev_titles[c] = list()
        for token in set(prevs[c]):
            if token in candidates :
                if nltk.pos_tag(token)[0][1] == "NNP":
                    prev_names[c].append(token)
            if token in titles:
                prev_titles[c].append(token)

def adjectives_search(q, content):
    adjectives = list()
    sentences = re.split(r' (?<![Mrs|Ms|Mr|Dr])\.|[\?!"]', content)
    query = " ".join(q)
    for s in sentences:
        if  query in s:
            tokens = nltk.word_tokenize(s)
            tagged = nltk.pos_tag(tokens)
            adjectives.extend([t[0] for t in tagged if t[1] == "JJ"\
                               and not t[0] in common_adj])
    return adjectives
  
def combine_with_titles(character, character_titles):
    pairs = list()
    for title in character_titles:
        pairs.append([title, character])
    title_pairs[character] = pairs
    
def formulate_queries(finals):
    queries = dict()
    for i in finals:
        string = " ".join(i)
        length = len(i)
        for j in finals:
            if i[length -1] == j[len(j) -1]:
               if length == 3:
                   queries[string] = [[i[0], i[2]], [i[1]]]
               if length == 2:
                   queries[string] = [[i[0], i[1]]]
               break
        if not string in queries:
            if length == 3:
                queries[string] = [[i[1]], [i[2]]]
            if length == 2:
                queries[string] = [[i[1]]]
    return queries

def main():
    content = open("jekyll.txt").read()
    tokens = nltk.word_tokenize(content)
    tagged = nltk.pos_tag(tokens)
    find_common_adjectives(tagged)
    characters = find_names(tagged)
    find_prevs(characters)

    for c in characters:
        for p in prev_names[c]:
            find_prevs([p])
            characters.append(p)

    for c in characters:
        combine_with_titles(c, prev_titles[c])
        
    finals = list()
    done = list()
    for name in title_pairs:
        pair = title_pairs[name]
        for p in pair:
            for c in characters:
                if p[1] in prev_names[c]: 
                    finals.append([p[0], p[1], c])
                    done.append([p[0], p[1]]) #title and given name 
                    done.append([[1], c]) #given name and surname
                    done.append([p[0], c]) #title and surname
    for name in title_pairs:
        pair = title_pairs[name]
        for p in pair:
            if not p in done:
                finals.append(p)
    
    queries = formulate_queries(finals)
    
    for character in queries:
        query_terms = queries[character]
        adjectives = list()
        for term in query_terms:
            adjectives.extend(adjectives_search(term, content))
        most_common = [word for word,nr in Counter(adjectives).most_common(5)]
        print(gen_description(character, most_common))
        print("")
     
if __name__== "__main__":
  main()
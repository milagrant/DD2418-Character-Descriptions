# -*- coding: utf-8 -*-

male_titles = ("Mr.", "Sir")
female_titles = ("Ms.", "Miss", "Mrs.", "Lady", "Madam", "Ma'am")

def get_pronoun(full_name):
    if full_name[0] in male_titles:
        return "him"
    if full_name[0] in female_titles:
        return "her"
    else:
        return "they"

def gen_description(full_name, adjectives):
    pron = get_pronoun(full_name)
    gender = "person"
    if pron == "him":
        gender = "man"
    if pron == "her":
        gender = "woman"
    
    des = list() 
    des.append(" ".join(full_name))
    des.append("is a")
    des.append(adjectives[0])
    des.append(gender)
    des.append(".")
    des.append("Some migth describe")
    des.append(pron)
    des.append("as")
    des.append(adjectives[1])
    des.append(",")
    des.append(adjectives[2])
    des.append("and")
    des.append(adjectives[3])
    des.append(".")
    
    return des
    
full_name = ["Mr.", "John", "Smith"]
adjectives = ["sweet", "quiet", "kind", "loving"]
des = gen_description(full_name , adjectives )
print(" ".join(des)) 

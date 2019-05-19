# -*- coding: utf-8 -*-
import random

male_titles = ("Mr.", "Sir")
female_titles = ("Ms.", "Miss", "Mrs.", "Lady", "Madam")

def get_pronoun(full_name):
    name = "".join(full_name)
    name_list = name.split(" ")
    if list(name_list)[0] in male_titles:
        return "him"
    if list(name_list)[0] in female_titles:
        return "her"
    else:
        return "them"

def gen_description(full_name, adjectives):
    random_number = random.randint(1,4)
    pron = get_pronoun(full_name)
    gender = "person"
    if pron == "him":
        gender = "man"
    if pron == "her":
        gender = "woman"
        
    if random_number == 1:
        des = generate_description1(full_name, adjectives, pron, gender)
    elif random_number == 2:
        des = generate_description2(full_name, adjectives, pron, gender)
    elif random_number == 3:
        des = generate_description3(full_name, adjectives, pron, gender)
    elif random_number == 4:
        des = generate_description4(full_name, adjectives, pron, gender)

    des = "".join(des)
    return des
def generate_description1(full_name, adjectives, pron, gender):

    des = list() 
    des.append("".join(full_name))
    des.append(" is a ")
    des.append(adjectives[0])
    des.append(" " + gender)
    des.append(". ")
    des.append("Some might describe ")
    des.append(pron)
    des.append(" as ")
    des.append(adjectives[1])
    des.append(", ")
    des.append(adjectives[2])
    des.append(" and ")
    des.append(adjectives[3])
    des.append(".")
    
    return des
    
def generate_description2(full_name, adjectives, pron, gender):

    des = list()  
    des.append("The ")
    des.append(adjectives[0])
    des.append(" ")
    des.append("".join(full_name))
    des.append(" is always ")
    des.append(adjectives[1])
    des.append(" and ")
    des.append(adjectives[2])
    des.append(". Some might even call ")
    des.append(pron)
    des.append(" ")
    des.append(adjectives[3])
    des.append(".")
    
    return des

def generate_description3(full_name, adjectives, pron, gender):

    des = list()  
    des.append("The character ")  
    des.append("".join(full_name))
    des.append(" is a ")  
    des.append(adjectives[0])
    des.append(" and ")
    des.append(adjectives[1])
    des.append(" " + gender)
    des.append(".")
    des.append(" You can always find ")
    des.append(pron)
    des.append(" being ")
    des.append(adjectives[2])
    des.append(" and ")
    des.append(adjectives[3])
    des.append(".")
    
    return des

def generate_description4(full_name, adjectives, pron, gender):

    des = list()  
    des.append("One central character is the ") 
    des.append(adjectives[0])
    des.append(" and ")
    des.append(adjectives[1])
    des.append(" ")
    des.append("".join(full_name))
    des.append(". As a person people would describe ")
    des.append(pron)
    des.append(" as ")
    des.append(adjectives[2])
    des.append(" and ")
    des.append(adjectives[3])
    des.append(".")
    return des


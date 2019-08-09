# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 22:09:17 2019

@author: Evan
"""



def compliment_strand(dna):
    rev_comp = ""
    dic = {"A" : "T", "T":"A", "G":"C", "C": "G"}
    for i in range(len(dna) - 1, -1, -1):
        rev_comp += dic[dna[i]]
    return rev_comp

#n = num months, k = num pairs, count = state
def n_rabbits(n, k, count, mature, immature):        
    new_immature = 1 if count == 1 else mature * k
    new_mature = immature + mature
    if(count == n):
        return new_mature + new_immature
    else:
        count += 1
        return n_rabbits(n, k, count, new_mature, new_immature)

n_rabbits(5,3,0,0,1)
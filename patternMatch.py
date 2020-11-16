# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 23:28:56 2019

@author: Kooffreh Emmanuel
"""
#Find a pattern of DNA in Genome.
Genome = "GATATATGCATATACTT"
Pattern = "ATAT"
def PatternMatching(Pattern, Genome):
    positions = [] # output variable
    
    for Codon in range(len(Genome)- len(Pattern) + 1):
        if Genome[Codon:Codon + len(Pattern)] == Pattern:
            
            positions.append(Codon)
    return positions
print (PatternMatching(Pattern, Genome))
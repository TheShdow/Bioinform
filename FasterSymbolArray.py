# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 22:25:47 2019

@author: Kooffreh Emmanuel
"""
file = open("C://Users//Kooffreh Emmanuel//Documents//E Coli.txt", "r")
symbol = "C"
Genome = file.read()
def FasterSymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]

    # look at the first half of Genome to compute first array value
    array[0] = PatternCount(symbol, Genome[0:n//2])

    for i in range(1, n):
        # start by setting the current array value equal to the previous array value
        array[i] = array[i-1]

        # the current array value can differ from the previous array value by at most 1
        if ExtendedGenome[i-1] == symbol:
            array[i] = array[i]-1
        if ExtendedGenome[i+(n//2)-1] == symbol:
            array[i] = array[i]+1
    return array

def PatternCount(Pattern, Text):
    count = 0
    
    for i in range(len(Text) + 1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count + 1
                        
    return count
print(FasterSymbolArray(Genome, symbol))
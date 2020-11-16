# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 15:46:53 2020

@author: Kooffreh Emmanuel
"""

def Profile(Motifs):
    count = {} # initializing the count matrix
    k = len(Motifs[0]) # length of the first kmer (but all are same length)
    for symbol in "ACGT":
        count[symbol] = [] # count matrix now has keys A, C, T, and G all with values of empty list
        for j in range(k):
            count[symbol].append(0) # count matrix now has keys A, C, G, and T all with values of a list of zeroes of length equal to the length of a kmer
    t = len(Motifs) # length of Motifs, a list of kmers (strings)
    for i in range(t): # for each kmer in Motifs
        for j in range(k): # for each element of the kmer
            symbol = Motifs[i][j] # assigns the key (symbol) to a nucleotide (ACGT) in Motifs
            
            #count[symbol] corresponds to the key of the dictionary count
            #count[symbol][j] corresponds to the position in the list assigned to the key
            count[symbol][j] += 1/t # adds 1 to the position in the list assigned to the key
    return count
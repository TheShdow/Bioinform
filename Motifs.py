# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 22:58:32 2020
To Find Regulatory Motifs in DNA responsible for replication and Circadian rhythms in Algae

@author: Kooffreh Emmanuel
"""
Motifs = [
"GCGCCCCGCCCGGACAGCCATGCGCTAACCCTGGCTTCGATGGCGCCGGCTCAGTTAGGGCCGGAAGTCCCCAATGTGGCAGACCTTTCGCCCCTGGCGGACGAATGACCCCAGTGGCCGGGACTTCAGGCCCTATCGGAGGGCTCCGGCGCGGTGGTCGGATTTGTCTGTGGAGGTTACACCCCAATCGCAAGGATGCATTATGACCAGCGAGCTGAGCCTGGTCGCCACTGGAAAGGGGAGCAACATC",
"CCGATCGGCATCACTATCGGTCCTGCGGCCGCCCATAGCGCTATATCCGGCTGGTGAAATCAATTGACAACCTTCGACTTTGAGGTGGCCTACGGCGAGGACAAGCCAGGCAAGCCAGCTGCCTCAACGCGCGCCAGTACGGGTCCATCGACCCGCGGCCCACGGGTCAAACGACCCTAGTGTTCGCTACGACGTGGTCGTACCTTCGGCAGCAGATCAGCAATAGCACCCCGACTCGAGGAGGATCCCG",
"ACCGTCGATGTGCCCGGTCGCGCCGCGTCCACCTCGGTCATCGACCCCACGATGAGGACGCCATCGGCCGCGACCAAGCCCCGTGAAACTCTGACGGCGTGCTGGCCGGGCTGCGGCACCTGATCACCTTAGGGCACTTGGGCCACCACAACGGGCCGCCGGTCTCGACAGTGGCCACCACCACACAGGTGACTTCCGGCGGGACGTAAGTCCCTAACGCGTCGTTCCGCACGCGGTTAGCTTTGCTGCC",
"GGGTCAGGTATATTTATCGCACACTTGGGCACATGACACACAAGCGCCAGAATCCCGGACCGAACCGAGCACCGTGGGTGGGCAGCCTCCATACAGCGATGACCTGATCGATCATCGGCCAGGGCGCCGGGCTTCCAACCGTGGCCGTCTCAGTACCCAGCCTCATTGACCCTTCGACGCATCCACTGCGCGTAAGTCGGCTCAACCCTTTCAAACCGCTGGATTACCGACCGCAGAAAGGGGGCAGGAC",
"GTAGGTCAAACCGGGTGTACATACCCGCTCAATCGCCCAGCACTTCGGGCAGATCACCGGGTTTCCCCGGTATCACCAATACTGCCACCAAACACAGCAGGCGGGAAGGGGCGAAAGTCCCTTATCCGACAATAAAACTTCGCTTGTTCGACGCCCGGTTCACCCGATATGCACGGCGCCCAGCCATTCGTGACCGACGTCCCCAGCCCCAAGGCCGAACGACCCTAGGAGCCACGAGCAATTCACAGCG",
"CCGCTGGCGACGCTGTTCGCCGGCAGCGTGCGTGACGACTTCGAGCTGCCCGACTACACCTGGTGACCACCGCCGACGGGCACCTCTCCGCCAGGTAGGCACGGTTTGTCGCCGGCAATGTGACCTTTGGGCGCGGTCTTGAGGACCTTCGGCCCCACCCACGAGGCCGCCGCCGGCCGATCGTATGACGTGCAATGTACGCCATAGGGTGCGTGTTACGGCGATTACCTGAAGGCGGCGGTGGTCCGGA",
"GGCCAACTGCACCGCGCTCTTGATGACATCGGTGGTCACCATGGTGTCCGGCATGATCAACCTCCGCTGTTCGATATCACCCCGATCTTTCTGAACGGCGGTTGGCAGACAACAGGGTCAATGGTCCCCAAGTGGATCACCGACGGGCGCGGACAAATGGCCCGCGCTTCGGGGACTTCTGTCCCTAGCCCTGGCCACGATGGGCTGGTCGGATCAAAGGCATCCGTTTCCATCGATTAGGAGGCATCAA",
"GTACATGTCCAGAGCGAGCCTCAGCTTCTGCGCAGCGACGGAAACTGCCACACTCAAAGCCTACTGGGCGCACGTGTGGCAACGAGTCGATCCACACGAAATGCCGCCGTTGGGCCGCGGACTAGCCGAATTTTCCGGGTGGTGACACAGCCCACATTTGGCATGGGACTTTCGGCCCTGTCCGCGTCCGTGTCGGCCAGACAAGCTTTGGGCATTGGCCACAATCGGGCCACAATCGAAAGCCGAGCAG",
"GGCAGCTGTCGGCAACTGTAAGCCATTTCTGGGACTTTGCTGTGAAAAGCTGGGCGATGGTTGTGGACCTGGACGAGCCACCCGTGCGATAGGTGAGATTCATTCTCGCCCTGACGGGTTGCGTCTGTCATCGGTCGATAAGGACTAACGGCCCTCAGGTGGGGACCAACGCCCCTGGGAGATAGCGGTCCCCGCCAGTAACGTACCGCTGAACCGACGGGATGTATCCGCCCCAGCGAAGGAGACGGCG",
"TCAGCACCATGACCGCCTGGCCACCAATCGCCCGTAACAAGCGGGACGTCCGCGACGACGCGTGCGCTAGCGCCGTGGCGGTGACAACGACCAGATATGGTCCGAGCACGCGGGCGAACCTCGTGTTCTGGCCTCGGCCAGTTGTGTAGAGCTCATCGCTGTCATCGAGCGATATCCGACCACTGATCCAAGTCGGGGGCTCTGGGGACCGAAGTCCCCGGGCTCGGAGCTATCGGACCTCACGATCACC"
]
# set t equal to the number of strings in Dna and k equal to 15

# Call GreedyMotifSearch(Dna, k, t) and store the output in a variable called Motifs

# Print the Motifs variable
k = 15

t = 10
# Print Score(Motifs)
print(len(Motifs))
#Determine the count for each neucleotide in each row
def Count(Motifs):

    count = {}

    k = len(Motifs[0])

    for symbol in "ACGT":

        count[symbol] = []

        for j in range(k):

            count[symbol].append(0)

    t = len(Motifs)

    for i in range(t):

        for j in range(k):

            symbol = Motifs[i][j]

            count[symbol][j] += 1

    return count
print(Count(Motifs))

 

def Consensus(Motifs):

  

    k = len(Motifs[0])

    count = Count(Motifs)

    consensus = ""

    for j in range(k):

        m = 0

        frequentSymbol = ""

        for symbol in "ACGT":

            if count[symbol][j] > m:

                m = count[symbol][j]

                frequentSymbol = symbol

        consensus += frequentSymbol

    return consensus

print(Consensus(Motifs))

def Profile(Motifs):

    t = len(Motifs)

    k = len(Motifs[0])

    profile = Count(Motifs)

    for i in 'ACTG':

        for j in range(k):

            profile[i][j] = profile[i][j]/t  

    return profile

 

def Score(Motifs):

    # Insert code here

    score = 0

    k = len(Motifs[0])

    count = Count(Motifs)

    max_symbol = Consensus(Motifs)

    sum1 = 0

    for j in range(k):

        m = 0

        for symbol in "ATCG":

            if count[symbol][j] > m:

                sum1 += count[symbol][j]

    for j in range(k):

        m = 0

        for symbol in "AGTC":

            if count[symbol][j] > m:

                m = count[symbol][j]

        score += m  

    return sum1-score

 

def Pr(Text, Profile):

    p=1

    k = len(Profile["A"])

    for i in range(len(Text)):

        p=p*Profile[Text[i]][i]

    return p

 

#Finally solved it

def ProfileMostProbablePattern(text,k,profile):

    p=-1

    result=text[0:k]

    for i in range(len(text)-k+1):

        seq=text[i:i+k]

        pr=Pr(seq,profile)

        if pr>p:

            p=pr

            result=seq

    return result

 

def GreedyMotifSearch(Motifs,k,t):

    BestMotifs = []

    for i in range(0, t):

        BestMotifs.append(Motifs[i][0:k])

    n = len(Motifs[0])

    for m in range(n-k+1):

        motifs = []

        motifs.append(Motifs[0][m:m+k])

        for j in range(1, t):

            P = Profile(motifs[0:j])

            motifs.append(ProfileMostProbablePattern(Motifs[j], k, P))

        if Score(motifs) < Score(BestMotifs):

            BestMotifs = motifs

    return BestMotifs
print(GreedyMotifSearch(Motifs,k,t))
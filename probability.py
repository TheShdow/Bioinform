# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 20:50:17 2020

@author: Kooffreh Emmanuel
"""
#refer to profile_motifs.py on how to get profile data
Text="GAGCTA"
Profile={"A": [0.4, 0.3, 0.0, 0.1, 0.0, 0.9], "C": [0.2, 0.3, 0.0, 0.4, 0.0, 0.1], "G":[0.1, 0.3, 1.0, 0.1, 0.9, 0.5, 0.0], "T":[0.3, 0.1, 0.0, 0.4, 0.5, 0.0]}
def Pr(Text, Profile):
    # insert your code here
    p = 1
    for i in range(len(Text)):
        p = p*Profile[Text[i]][i]
        if p == 0:
            break
        
    return p
print(Pr(Text, Profile))
def test (Text,Profile):
    for i in range(len(Text)):
        Test = Profile[Text[i]]  

    return Test
print (test (Text,Profile))
# Input:  A string Pattern
# Output: The reverse of Pattern
Pattern = "AAAACCCGGT"

def Reverse(Pattern):
    rev = ""
    for i in Pattern:
        rev = i + rev
    return rev

print (Reverse(Pattern))
#Finding the complimetary Strand of DNA
Pattern = "AAAACCCGGT"
def Complement(Pattern):
        comp = ""
    n = len(Pattern)
    for i in Pattern:
        if i == "A":
            comp += "T"
        if i == "C":
            comp += "G"
        if i == "G":
            comp += "C"
        if i == "T":
            comp += "A"
    return comp
print (Complement(Pattern))
#Reversing the Complimetary strand
def ReverseComplement(Pattern):
        compfunc = Complement(Pattern)
    revcomp = ""
    for i in compfunc:
        revcomp = i + revcomp
    return revcomp

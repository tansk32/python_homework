code = {
    "UUU": "F",      "CUU": "L",      "AUU": "I",      "GUU": "V",
    "UUC": "F",      "CUC": "L",      "AUC": "I",      "GUC": "V",
    "UUA": "L",      "CUA": "L",      "AUA": "I",      "GUA": "V",
    "UUG": "L",      "CUG": "L",      "AUG": "M",      "GUG": "V",
    "UCU": "S",      "CCU": "P",      "ACU": "T",      "GCU": "A",
    "UCC": "S",      "CCC": "P",      "ACC": "T",      "GCC": "A",
    "UCA": "S",      "CCA": "P",      "ACA": "T",      "GCA": "A",
    "UCG": "S",      "CCG": "P",      "ACG": "T",      "GCG": "A",
    "UAU": "Y",      "CAU": "H",      "AAU": "N",      "GAU": "D",
    "UAC": "Y",      "CAC": "H",      "AAC": "N",      "GAC": "D",
    "UAA": "Stop",   "CAA": "Q",      "AAA": "K",      "GAA": "E",
    "UAG": "Stop",   "CAG": "Q",      "AAG": "K",      "GAG": "E",
    "UGU": "C",      "CGU": "R",      "AGU": "S",      "GGU": "G",
    "UGC": "C",      "CGC": "R",      "AGC": "S",      "GGC": "G",
    "UGA": "Stop",   "CGA": "R",      "AGA": "R",      "GGA": "G",
    "UGG": "W",      "CGG": "R",      "AGG": "R",      "GGG": "G"
}

# dna = "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"
dna="AACTTT"

#for line in fasta:
def parse_fasta(fasta):
    lines = fasta.strip().split("\n") #to separate the string into a list of lines
    s = "".join(lines[1:])
    return s

rna_forward = dna.replace("T", "U") #ooder for x in s, if xx == "T", print "U", elif x!=T print 
#Replace T with U

#template strand übersetzen in coding strand
def complement(x):
    if x == "A":
        return "T"
    elif x == "C":
        return "G"
    elif x == "G":
        return "C"
    elif x == "T":
        return "A"

def aug_finder(test):
    s = test #eig rna, for both
    t = "AUG"
    starts = []
    for i in range(len(s) - len(t) +1):
        if s[i:i+len(t)] == t:
            starts.append(i)
    return starts


rna_backward = "" 
for base in dna:
	rna_backward += complement(base)
rna_backward = rna_backward[::-1] #(reverse complement)

rna_backward = rna_backward.replace("T", "U")

test = "UUAUGCCCAUG"
positions = aug_finder(test)
print(positions)

#print everything from AUG to stop(UAA, UAG, UGA)

def find_orfs(rna, starts):
    orfs = []
    for start in starts:
        orf = ""
        for i in range(start, len(rna), 3):
        codon = rna[i:i+3]
        orf += codon
        if len(codon) < 3:
            break
        if code[codon] == "Stop":
            orfs.append(orf)


    
    
 



# #translate to protein
# peptide = ""
# for start in range(0, len(t), 3):
#     codon = t[start:start+3]
#     aminoacid = code[codon]
#     if aminoacid == "Stop":
#         break
#     peptide += aminoacid
# return aminoacid
# # go over s and t, 
# #start at readingfram [0], [1], [2]





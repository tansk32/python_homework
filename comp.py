
DNA = "TGCCCCTCTTTTCGCCGCGAGCGAGTGAACGCACCCCATTCTCGGGAACAGTCCTCGTTATACTAACGATGATGCCGGCTCCCGAGCCCACCGGCCGCTGATTCTCGGCGAAGCGGCTTATTTAATCAACATGGGATCGGTTACACTCGTTGGAAGAATAATTAATGTTCGTTGCACCCGGCCATCCCCTTAGGTAAACGAAAGTTACCGGGTGCTCTATCTCTGCGGGGCTCGCTTCTCTAACATTGGACTCTTGACGGAATCAATCGAAAGGTCAAACGACGATATCAATACACGTATACCGGACGACGCACTTACTTAGTCTCCGAGGAATCGTAGCGCGACCAGCATGCGCCGTTTTCCCCATGTCAATGACGGTTTCGCGCTACGGCCATACAATTATGGCGTGCCAATCGGCGTTCTCAGCACACTGGGTAAGGCGGATGGATAGTATTAGGGTGACCAATACAAGTTTATAACCAGTCAAGAAGTGCGCTAATACAATGGCGAGCGGAACCGCGGCTGGTCCACTACTTCACAGGCAAGGCGCTCTAAGCCGGCCCGACGCATATTTCGATGGTAAGCTGCTCCTTTACTCACTGGAGGACTTTAGGCGTGCGCACCCAGGTAATATTCCGGAGTGTTACCATACAGCCATCTTACGTCTCCAAATGTGAATTCTTTCCGCTTTAACCGATACGGATGGTTGCGATCTTATCAGGTTGGATCCCATTTCCCCGGGGCCCGCAAACCCGTGGCACCCATTCGCTCCATATCATTAACATAGTTCCACCCACTCTCTAACCATAAAACGCATTGCATGACCCAGTAGGAGGACCAGTAGGACGATGCATCCGCGTGGCACCAGAGGCCGTTGGTGTCGGCACGAAATAAAAGGTCGACGAACGTATCGAAGACGCTTTACTCTTTCGGATCTGTGGGTGGGCCGTGGGATTAGGGTGTAGCAATGTACCATACTGAAAG"


for x in DNA:
	def complement(x):
		if x == "A":
			return "T"
		elif x == "C":
			return "G"
		elif x == "G":
			return "C"
		elif x == "T":
			return "A"
complementary_dna = ""
for base in DNA:
	complementary_dna += complement(base)
print(complementary_dna[::-1]) #(reverse complement)
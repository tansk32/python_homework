letters = "GAGCCGTGCAACCGCCTACATGGCCTTAGGAGTGCAGATCAGGCTAATATCAAATAATTATGAGGGTGCCGAGATTACTTAGTAACCTGCTGTTCACCTAAACCTTATACGACTTCCACGGGAGCTAAACGACTCTTTACACGCCCAATGCCTTGGTCCTGTTATCCAGTTGAATCTAGTACAGCATGTGGTTAAGCCATGTCCCAGGTTTGCGTCTGGAGCCTCGGCGGTGAATTGCGTGAGATCTATCGCTGCCGGCACAAAGGCCCCTCCAGAATCATTGTGTGGACAACAGCCGCGAGTCTATCTCGGTCCGGTTTAATCTCGAGATGTAAAACCATTCTAACAGTCAGCTGGATGGAACGGATGTCTATGAACGGCGTGTTGGATCGATTTAAAACCCACGTAGGCAAACGGTACTTGCTATGCTAGTCTGACGACCTCCCCGCGCCCTCAACCTCTTGGCTTGCGATCGTATTTTATTTTAGACGTTATCGGACCGCGTGGTTAGGTGGGTCTCACTTCTGTCCTAAGGTCGTGGTTAACCCCATCCGATGATCGTCATTTTAGGTATTTGTGATGTGGCGACCGTAGCTCAACATTCCGGCCGATTCCTTTGTAAGTGGTCGCACAGGTACAGACGTCATCGTCATGAGCTGAAAATATTAAGGCCTAAGTGATGGATGTAATTTTCGGCGCGGAACGCGTTTACGAGCGTTTAATAATTGCCTCTGGCAACTCACAAGTGACTGAACCGGAGACTCAGATCAACGTTAATCCATTGCGGGCGTCACGCAACCACGATCAACGGACCTACTTACGCATACCCCCTGTACTCTGGTTCCTCCACCCACCAGACTACATCGGCGGAGACGCTACGTACCAACGGGCTTTAGCCGTTGGGTG"


rna = []
for base in letters: 
	if base == "T":
		rna.append("U")
	else:
		rna.append(base) 
	
print("".join(rna))
#SUBS
s = "GATATATGCATATACTT"
t = "ATAT"

#go over sequence compare with substring
locations = []
for i in range(len(s) - len(t) +1)
if s[i:i+len(t)] == t:
    locations.append(i +1)
 print(" ".join(map(str, locations)))



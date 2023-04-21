def split_dna(k, dna):
    k = int(k)
    parts = []
    for i in range(0, len(dna)-k+1):
        parts.append(dna[i:i+k])
    return parts

k = input()
dna = input()

for i in split_dna(k,dna):
    print(i)


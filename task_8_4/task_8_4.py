

def split_dna(k, dna):
    k = int(k)
    parts = []
    for i in range(0, len(dna)-k+1):
        parts.append(dna[i:i+k])
    kmer = []
    for i in parts:
        kmer.append(i[0:k-1])
        kmer.append(i[1:k])
    unique_kmer = set(kmer)
    d = dict.fromkeys(unique_kmer)
    for i in unique_kmer:
        d[i] = []
    # left = []
    # right = []
    for i in parts:
        left = i[0:k-1]
        right = i[1:k]
        if left[1:k-1] == right[0:k-2]:
            d[left].append(right)
    return d


k = input()
dna = input()

d = split_dna(k,dna)

for i in d:
    if len(d[i])!=0:
        if len(d[i]) == 1:
            print(i+' -> '+str(d[i][0]))
        else:
            print(i+' -> '+','.join(d[i]))







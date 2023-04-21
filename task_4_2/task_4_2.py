
def combinations(start):
    base = ['A', 'G', 'T', 'C']
    new = []
    for i in range(0, len(start)):
        for j in range(0, len(base)):
            new.append(start[i] + base[j])
    return new
def _combinations(k):
    l = 0
    tmp = ['']
    new_combinations_1 = []
    while l<k:
        tmp = combinations(tmp)
        l+=1
    return(tmp)


def hamming(s1,s2):
    d = 0
    for i in range(0,len(s1)):
        if s1[i] != s2[i]:
            d +=1
    return d

def d(pattern, dna):
    motif = 0
    l = len(dna[0])
    for i in range(0,len(dna)):
        distance = 1000000
        for j in range(0,l-len(pattern)+1):
            if distance > hamming(dna[i][j:j+len(pattern)],pattern):
                distance = hamming(dna[i][j:j+len(pattern)],pattern)
        motif += distance
    return motif

#print(d('AAT',['AAATTGACGCAT','GACGACCACGTT','CGTCAGCGCCTG','GCTGAGCACCGG','AGTACGGGACAG']))

def MedianString(k,dna):
    k = int(k)
    distance = 10000000
    comb = _combinations(k)
    for i in range(0,len(comb)):
        if distance > d(comb[i],dna):
            distance = d(comb[i],dna)
            median = comb[i]
    return median

k = input()
dna=[]
num_of_elem=5
for i in range(num_of_elem):
    dna.append(input())

print(MedianString(k,dna))

# AAATTGACGCAT GACGACCACGTT CGTCAGCGCCTG GCTGAGCACCGG AGTACGGGACAG

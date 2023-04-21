
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
    for i in tmp:
        pieces = [i[j:j + 1] for j in range(0, len(i), 1)]
        new_combinations_1.append(pieces)
    return new_combinations_1

def factorial(n):
    if n == 0:
        return 1
    i = 1
    f = 1
    while i<=n:
        f = f * i
        i += 1
    return f

def num_of_combinations(n,k):
    return int(factorial(n)/(factorial(n-k)*factorial(k)))

def pow(a,b):
    result = a
    for i in range(0,b-1):
        result = result *a
    return result


def check_to_all_strings(dna, j, d):
    misses = 0
    missess = 0
    for i in dna:
        for k in range(0,len(i)-len(j)+1):
            part = i[k:k+len(j)]

            pieces = [part[m:m+1] for m in range(0, len(part),1)]

            for u in range(0,len(j)):
                if pieces[u] != j[u]:
                    misses += 1
            if misses > d:
                missess +=1

            misses = 0
        if missess == (len(i)-len(j)+1):
            return False
        missess = 0

    return True


def MotifEnumeration(dna, k, d):
    patterns = []
    k = int(k)
    d = int(d)
    comb = _combinations(k)
    for o in dna:
        parts = [o[i:i + k] for i in range(0, len(o), 1)]
        print(parts)
        for i in parts:
            print(i)
            pieces = [i[s:s + 1] for s in range(0, k, 1)]
            for j in comb:
                misses = 0
                for s in range(0,k):

                    if j[s] != pieces[s]:
                        misses +=1
                if misses <= d:
                    if check_to_all_strings(dna,j, d) == True:
                        patterns.append(j)
    patterns_unique = []
    for i in patterns:
        if i not in patterns_unique:
            patterns_unique.append(i)
    return patterns_unique
str1 = input().split()
k = int(str1[0])
d = int(str1[1])
dna = input().split()
result = MotifEnumeration(dna,k,d)
tmp = []
for i in result:
    tmp.append("".join(i))

print(" ".join(tmp))
#  3 1 ATTTGGC TGCCTTA CGGTATC GAAAATT
#  4 1 CACTGATCGACTTATC CTCCGACTTACCCCAC GTCTATCCCTGATGGC CAGGGTTGTCTTGTCT
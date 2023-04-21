def MostProbableKmer(text, k, matrix):
    max_prob = 0
    index = 0
    prob = 1.0
    for i in range(0,len(text)-k+1):
        kmer = text[i:i+k]
        for j in range(0,k):
            if kmer[j] == 'A':
                prob = prob * matrix[0][j]
            elif kmer[j] == 'C':
                prob = prob * matrix[1][j]
            elif kmer[j] == 'G':
                prob = prob * matrix[2][j]
            elif kmer[j] == 'T':
                prob = prob * matrix[3][j]
        if prob > max_prob:
            max_prob = prob
            index = i
        prob = 1.0
    result = []
    for i in range(0,k):
        result.append(text[index+i])
    return result

def form_profile(motifs,t,k):
    profile = []
    for i in range(0,4):
        tmp = []
        for j in range(0,k):
            tmp.append(0)
        profile.append(tmp)
    for i in range(0,k):
        count = [1] * 4
        for j in range(0,t):
            if motifs[j][i] == 'A':
                count[0] += 1
            if motifs[j][i] == 'C':
                count[1] += 1
            if motifs[j][i] == 'G':
                count[2] += 1
            if motifs[j][i] == 'T':
                count[3] += 1
        for j in range(0,4):
            profile[j][i] = count[j]/t
    return profile

def score(dna,t,k):
    sum = 0
    for i in range(0,k):
        col = []
        count = 0
        for j in range(0,t):
            col.append(dna[j][i])

        most_frequent = max(set(col), key = col.count)
        for j in range(0,t):
            if col[j] != most_frequent:
                count += 1
        sum += count
    return sum

def GreedyMotifSearch(dna, t, k):
    l = len(dna[0])
    best_motifs = []
    for i in range(0,t):
        tmp = []
        for j in range(0,k):
            tmp.append(dna[i][j])
        best_motifs.append(tmp)




    for i in range(0, l-k+1):
        m = []
        for o in range(0, t):
            tmp = []
            for j in range(0, k):
                tmp.append(None)
            m.append(tmp)
        for j in range(0,k):
            m[0][j] = dna[0][i+j]

        for j in range(1,t):
            profile = form_profile(m[0:j],j,k)
            str = ''
            for g in range(0,l):
                str = str + dna[j][g]
            m[j] = MostProbableKmer(str, k, profile)

        if score(m,t,k)<score(best_motifs,t,k):
            best_motifs = m

    return best_motifs

str1 = input().split()
k = int(str1[0])
t = int(str1[1])


matrix = []

for i in range(t):
    str = input()
    parts = [str[k:k+1] for k in range(0, len(str), 1)]
    matrix.append(parts)

best_motifs = GreedyMotifSearch(matrix,t,k)

for i in best_motifs:
    print(''.join(i))



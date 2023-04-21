

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
    return text[index:index+k]

text = input()
k = int(input())

row = 4
col = k

matrix = []

for i in range(row):
    str = input().split()
    matrix.append(str)

for i in range(row):
    for j in range(col):
        matrix[i][j] = float(matrix[i][j])
print(MostProbableKmer(text, k, matrix))
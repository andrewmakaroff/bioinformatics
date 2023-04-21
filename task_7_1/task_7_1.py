import numpy as np


def score(v_i,w_j):

    matrix = [
        [4, 0, -2, -1, -2,  0, -2, -1, -1, -1, -1, -2, -1, -1, -1,  1,  0,  0, -3, -2],
        [0,  9, -3, -4, -2, -3, -3, -1, -3, -1, -1, -3, -3, -3, -3, -1, -1, -1, -2, -2],
        [-2, -3,  6,  2, -3, -1, -1, -3, -1, -4, -3,  1, -1,  0, -2,  0, -1, -3, -4, -3],
        [-1, -4,  2,  5, -3, -2,  0, -3,  1, -3, -2,  0, -1,  2,  0,  0, -1, -2, -3, -2],
        [-2, -2, -3, -3,  6, -3, -1,  0, -3,  0,  0, -3, -4, -3, -3, -2, -2, -1,  1,  3],
        [0, -3, -1, -2, -3,  6, -2, -4, -2, -4, -3,  0, -2, -2, -2,  0, -2, -3, -2, -3],
        [-2, -3, -1,  0, -1, -2,  8, -3, -1, -3, -2,  1, -2,  0,  0, -1, -2, -3, -2,  2],
        [-1, -1, -3, -3,  0, -4, -3,  4, -3,  2,  1, -3, -3, -3, -3, -2, -1,  3, -3, -1],
        [-1, -3, -1,  1, -3, -2, -1, -3,  5, -2, -1,  0, -1,  1,  2,  0, -1, -2, -3, -2],
        [-1, -1, -4, -3,  0, -4, -3,  2, -2,  4,  2, -3, -3, -2, -2, -2, -1,  1, -2, -1],
        [-1, -1, -3, -2,  0, -3, -2,  1, -1,  2,  5, -2, -2,  0, -1, -1, -1,  1, -1, -1],
        [-2, -3,  1,  0, -3,  0,  1, -3,  0, -3, -2,  6, -2,  0,  0,  1,  0, -3, -4, -2],
        [-1, -3, -1, -1, -4, -2, -2, -3, -1, -3, -2, -2,  7, -1, -2, -1, -1, -2, -4, -3],
        [-1, -3,  0,  2, -3, -2,  0, -3,  1, -2,  0,  0, -1,  5,  1,  0, -1, -2, -2, -1],
        [-1, -3, -2,  0, -3, -2,  0, -3,  2, -2, -1,  0, -2,  1,  5, -1, -1, -3, -3, -2],
        [1, -1,  0,  0, -2,  0, -1, -2,  0, -2, -1,  1, -1,  0, -1,  4,  1, -2, -3, -2],
        [0, -1, -1, -1, -2, -2, -2, -1, -1, -1, -1,  0, -1, -1, -1,  1,  5,  0, -2, -2],
        [0, -1, -3, -2, -1, -3, -3,  3, -2,  1,  1, -3, -2, -2, -3, -2,  0,  4, -3, -1],
        [-3, -2, -4, -3,  1, -2, -2, -3, -3, -2, -1, -4, -4, -2, -3, -3, -2, -3, 11,  2],
        [-2, -2, -3, -2,  3, -3,  2, -1, -2, -1, -1, -2, -3, -1, -2, -2, -2, -1,  2,  7]
    ]

    order = ['A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y']
    pos_v = 0
    pos_w = 0
    for i in range(0,len(order)):
        if v_i == order[i]:
            pos_v = i
        if w_j == order[i]:
            pos_w = i

    return matrix[pos_v][pos_w]

def get_distance(v,w):
    s = np.zeros((len(v), len(w)), dtype=int).tolist()
    backtrack = np.zeros((len(v), len(w)), dtype=int).tolist()
    for j in range(0,len(w)):
        s[0][j] = (-5)*j
    for i in range(0,len(v)):
        s[i][0] = (-5)*i

    for i in range(1,len(v)):
        for j in range(1,len(w)):
            s[i][j] = max(s[i-1][j]-5,s[i][j-1]-5,s[i-1][j-1]+score(v[i],w[j]))
            if max(s[i-1][j]-5,s[i][j-1]-5,s[i-1][j-1]+score(v[i],w[j])) == s[i-1][j]-5:
                backtrack[i][j] = 0 # down
            elif max(s[i - 1][j] - 5, s[i][j - 1] - 5, s[i - 1][j - 1] + score(v[i], w[j])) == s[i][j-1] - 5:
                backtrack[i][j] = 1 # right
            elif max(s[i - 1][j] - 5, s[i][j - 1] - 5, s[i - 1][j - 1] + score(v[i], w[j])) == s[i -1][j-1] + score(v[i],w[j]):
                backtrack[i][j] = 2 # diag


    print(s[len(v)-1][len(w)-1])

    return backtrack

def output(backtrack,v,w,i,j):
    result_v = ''
    result_w = ''
    while (i > 0) | (j > 0):
        if backtrack[i][j] == 0:
            result_v = v[i] + result_v
            result_w = '-'+result_w
            i = i - 1

        elif backtrack[i][j] == 1:
            result_w = w[j] + result_w
            result_v = '-'+result_v
            j = j - 1

        elif backtrack[i][j] == 2:
            result_v = v[i] + result_v
            result_w = w[j] + result_w
            i = i - 1
            j = j - 1
    result = []
    result.append(result_v)
    result.append(result_w)
    return result


v_input = input()
w_input = input()

v = '-'+v_input
w = '-'+w_input
i = len(v)-1
j = len(w)-1

result = output(get_distance(v,w),v,w,i,j)

print(result[0])
print(result[1])
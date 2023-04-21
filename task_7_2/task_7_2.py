import numpy as np
import sys

file = open("matrix.txt", "r")

strings = []
while True:
    line = file.readline()
    if not line:
        break
    strings.append(line.strip()[2:])

file.close

matrix = []
for i in strings:
    matrix.append([int(x) for x in i.split()])

def score(v_i,w_j,matrix):


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
    """for j in range(0,len(w)):
        s[0][j] = (-5)*j
    for i in range(0,len(v)):
        s[i][0] = (-5)*i
    """
    for i in range(1,len(v)):
        for j in range(1,len(w)):
            s[i][j] = max(s[i-1][j]-5,s[i][j-1]-5,s[i-1][j-1]+score(v[i],w[j],matrix),0)
            if max(s[i-1][j]-5,s[i][j-1]-5,s[i-1][j-1]+score(v[i],w[j],matrix)) == s[i-1][j]-5:
                backtrack[i][j] = 0 # down
            elif max(s[i - 1][j] - 5, s[i][j - 1] - 5, s[i - 1][j - 1] + score(v[i], w[j],matrix)) == s[i][j-1] - 5:
                backtrack[i][j] = 1 # right
            elif max(s[i - 1][j] - 5, s[i][j - 1] - 5, s[i - 1][j - 1] + score(v[i], w[j],matrix)) == s[i -1][j-1] + score(v[i],w[j],matrix):
                backtrack[i][j] = 2 # diag
            elif max(s[i - 1][j] - 5, s[i][j - 1] - 5, s[i - 1][j - 1] + score(v[i], w[j],matrix)) == 0:
                backtrack[i][j] = 3 # null
    j = np.argmax(s) % (len(w))
    i = (np.argmax(s) - len(w) - 2) // (len(w)) + 1
    global new_i
    global new_j
    new_i = (np.argmax(s) - len(w) - 2) // (len(w)) + 1
    new_j = np.argmax(s) % (len(w))
    print(s[i][j])

    return backtrack

def output(backtrack,v,w,i,j):
    result_v = ''
    result_w = ''
    while (i > 0) | (j > 0):
        if backtrack[i][j] == 0:
            i = i - 1
            result_v = v[i+1] + result_v
            result_w = '-'+result_w


        elif backtrack[i][j] == 1:
            j = j - 1
            result_w = w[j+1] + result_w
            result_v = '-'+result_v
        elif backtrack[i][j] == 2:
            i = i - 1
            j = j - 1
            result_v = v[i+1] + result_v
            result_w = w[j+1] + result_w

        elif backtrack[i][j] == 3:
            i = 0
            j = 0
    result = []
    result.append(result_v)
    result.append(result_w)
    return result


v_input = input()
w_input = input()

v = '-'+v_input
w = '-'+w_input


result = output(get_distance(v,w),v,w,new_i,new_j)

print(result[0])
print(result[1])
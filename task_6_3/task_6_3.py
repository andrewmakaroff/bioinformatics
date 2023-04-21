import numpy as np

def backtrack(v,w):
    s = np.zeros((len(v), len(w) ), dtype=int).tolist()
    backtrack = np.zeros((len(v) , len(w) ), dtype=int).tolist()
    for i in range(1,len(v)):
        for j in range(1,len(w)):
            if v[i] == w[j]:
                s[i][j] = max(s[i-1][j],s[i][j-1],s[i-1][j-1]+1)
            else:
                s[i][j] = max(s[i-1][j],s[i][j-1])
            if s[i][j] == s[i-1][j]:
                backtrack[i][j] = 0
            elif s[i][j] == s[i][j-1]:
                backtrack[i][j] = 1
            elif (s[i][j] == s[i-1][j-1]+1) & (v[i] == w[j]):
                backtrack[i][j] = 2
    return backtrack
"""
def output(backtrack,v,i,j):
    global result
    result = ''
    if i == 0 | j == 0:
        return
    if backtrack[i][j] == 0:
        output(backtrack,v,i-1,j)
    elif backtrack[i][j] == 1:
        output(backtrack, v, i , j-1)
    elif backtrack[i][j] == 2:
        output(backtrack,v,i-1,j-1)
        result+=v[i]
"""

def output(backtrack,v,i,j):
    result = ''
    print(backtrack)
    while (i != 0) & (j != 0):
        if backtrack[i][j] == 0:
            i = i - 1
        elif backtrack[i][j] == 1:
            j = j - 1
        elif backtrack[i][j] == 2:
            result += v[i]
            i = i - 1
            j = j - 1
    return result

v_input = input()
w_input = input()

v = '_'+v_input
w = '_'+w_input
i = len(v)-1
j = len(w)-1
print(output(backtrack(v,w),v,i,j)[::-1])
#print(result)
#ACACTGTGA
#AACCTTGG
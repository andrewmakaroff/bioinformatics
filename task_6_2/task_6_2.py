import numpy as np

def ManhattanTourist(n,m,down,right):
    s = np.zeros((n+1,m+1), dtype=int).tolist()
    for i in range(1,n+1):
        s[i][0] = s[i-1][0]+int(down[i-1][0])
    for j in range(1,m+1):
        s[0][j] = s[0][j-1]+int(right[0][j-1])
    for i in range(1,n+1):
        for j in range(1,m+1):
            s[i][j] = max(s[i-1][j]+int(down[i-1][j]),s[i][j-1]+int(right[i][j-1]))

    return s[n][m]

str1 = input().split()
n = int(str1[0])
m = int(str1[1])

down = []
for i in range(0,n):
    down.append(input().split())

right = []
for i in range(0,n+1):
    right.append(input().split())
print(ManhattanTourist(n,m,down,right))
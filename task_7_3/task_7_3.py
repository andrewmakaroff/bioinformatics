import numpy as np

def get_distance(str1,str2):
    s = np.zeros((len(str1), len(str2)), dtype=int).tolist()
    for j in range(0,len(str2)):
        s[0][j] = j

    for i in range(1,len(str1)):
        s[i][0] = i

    for i in range(1,len(str1)):
        for j in range(1,len(str2)):
            if str1[i] != str2[j]:
                s[i][j] = min(s[i-1][j]+1, s[i][j-1]+1, s[i-1][j-1]+1)
            elif str1[i] == str2[j]:
                s[i][j] = min(s[i - 1][j] + 1, s[i][j - 1] + 1, s[i - 1][j - 1])
    return s[len(str1)-1][len(str2)-1]

str1_input = input()
str2_input = input()

str1 = '_'+str1_input
str2 = '_'+str2_input

print(get_distance(str1,str2))
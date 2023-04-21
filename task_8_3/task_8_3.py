import sys

def path(parts):
    k = len(parts[0])
    left = []
    right = []
    for i in parts:
        for j in parts:
            if i[1:k] == j[0:k-1]:
                left.append(i)
                right.append(j)
    return left, right




parts = []
while True:
    try:
        parts.append(input())
    except EOFError:
        break

left, right = path(parts)

strings = []
for i in range(len(left)):
    strings.append(left[i]+' -> '+right[i])
print(strings)
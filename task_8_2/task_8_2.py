import sys
def join_dna(parts):
    dna = ''
    for i in parts:
        dna += i[0]
    dna += parts[len(parts)-1][1:]
    return dna
parts = []
while True:
    try:
        parts.append(input())
    except EOFError:
        break

print(join_dna(parts))

#CGCA GCAA CAAA AAAT AATA ATAA TAAG AAGC AGCC
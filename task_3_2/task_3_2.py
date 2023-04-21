mass_dict = {
    'G': 57,
    'A': 71,
    'S': 87,
    'P': 97,
    'V': 99,
    'T': 101,
    'C': 103,
    'I': 113,
    'L': 113,
    'N': 114,
    'D': 115,
    'K': 128,
    'Q': 128,
    'E': 129,
    'M': 131,
    'H': 137,
    'F': 147,
    'R': 156,
    'Y': 163,
    'W': 186
}

def cyclospectrum(pepstr):
    s = pepstr
    subpep = []
    sub = []
    sub.append('')
    doubled_s = s + s
    for i in range(1, len(s)):
        for j in range(0, len(s)):
            subpep = doubled_s[j:j + i]
            sub.append(subpep)
    sub.append(s)

    mass = []

    for i in range(0, len(sub)):
        m = 0
        if sub[i] == '':
            mass.append(0)
        else:
            for j in range(0, len(sub[i]), 1):
                part = [sub[i][j:j + 1]]
                m += mass_dict.get(part[0])
                if j == len(sub[i]) - 1:
                    mass.append(m)
    mass = sorted(mass)
    mass = [str(i) for i in mass]
    return mass
theoretical = input()
experimental = input().split()

count = 0
for i in cyclospectrum(theoretical):
    if i in experimental:
        count += 1
        experimental.remove(i)
print(count)

# NQEL
# 0 99 113 114 128 227 257 299 355 356 370 371 484



#Spectrum = list(map(int, input().split()))

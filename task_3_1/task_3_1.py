# put your python code here

mass_dict = {
    'G': 57,
    'A': 71,
    'S': 87,
    'P': 97,
    'V': 99,
    'T': 101,
    'C': 103,
    'I': 113,
    # 'L': 113,
    'N': 114,
    'D': 115,
    'K': 128,
    # 'Q': 128,
    'E': 129,
    'M': 131,
    'H': 137,
    'F': 147,
    'R': 156,
    'Y': 163,
    'W': 186
}


def mass(peptide):
    parts = [peptide[i:i + 1] for i in
             range(0, len(peptide), 1)]  # delete this raw because peptide - not string it`s a list
    m = 0
    for i in range(0, len(peptide)):
        m += mass_dict.get(peptide[i])
    return m


def parentmass(spectrum):
    max = 0
    for i in spectrum:
        number = int(i)
        if max < number:
            max = number
    return max


def theoretical_spectrum(pep):
    # s = pep
    subpep = []
    sub = []
    sub.append('')
    doubled_s = pep
    for i in range(1, len(pep)):
        for j in range(0, len(pep)):
            if (i + j) <= len(pep):
                subpep = doubled_s[j:j + i]
                sub.append(subpep)
    sub.append(pep)
    return sub


def expand(pep):  # a function which adds one key from dict_mass to each letter of peptide

    masses = mass_dict.keys()
    # parts = [pep[i:i + 1] for i in range(0, len(pep), 1)]   delete this raw because peptide - not string it`s a list
    new = []
    if pep == '':
        for j in range(0, len(list(masses))):
            new.append(list(masses)[j])

    else:
        for i in range(0, len(pep)):
            for j in range(0, len(list(masses))):
                new.append(pep[i] + list(masses)[j])
    return new


def cyclospectrum(pepstr):
    subpep = []
    sub = []
    sub.append('')
    doubled_s = pepstr + pepstr
    for i in range(1, len(pepstr)):
        for j in range(0, len(pepstr)):
            subpep = doubled_s[j:j + i]
            sub.append(subpep)
    sub.append(pepstr)

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
    # mass = " ".join(mass)      We need a list not string
    return mass


def are_equal(list1, list2):
    if len(list1) != len(list2):
        return False
    else:
        for i in range(0, len(list1)):
            if list1[i] != list2[i]:
                return False
    return True


def cyclopeptide_sequencing(spectrum):
    result = ''
    peptide = ['']
    while len(peptide) != 0:
        peptide = expand(peptide)
        i = 0
        while i < len(peptide):

            if mass(peptide[i]) == parentmass(spectrum):
                if are_equal(cyclospectrum(peptide[i]), spectrum):
                    result = result + "-".join(peptide[i]) + ' '
                peptide.remove(peptide[i])
            elif is_consistent(peptide[i], spectrum) == False:
                peptide.remove(peptide[i])

            else:
                i += 1
    return result


def getmasses(pep):
    masses = []
    for i in pep:
        masses.append(str(mass_dict.get(i)))
    return (masses)


def is_consistent(pep, spectrum):
    masses = theoretical_spectrum(pep)
    masses_pass = [None] * len(masses)
    for i in range(0, len(masses)):
        masses_pass[i] = 0
    count = 0
    for i in range(0, len(masses)):
        for j in range(0, len(spectrum)):
            if str(mass(masses[i])) == spectrum[j]:
                masses_pass[i] = 1

    for i in range(0, len(masses_pass)):
        if masses_pass[i] == 0:
            return False
    return True


# print(is_consistent('IK', ['0','113','113','128','128','241','422']))

spectrum = input().split()

result = cyclopeptide_sequencing(spectrum)

translated_result = ''
for i in range(0, len(result)):
    if (result[i] == '-') | (result[i] == ' '):
        translated_result = translated_result + result[i]
    else:
        translated_result = translated_result + str(mass_dict.get(result[i]))
print(translated_result)


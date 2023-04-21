
import sys

mass_dict_1 = {
    'G': 57,
    'A': 71,
    'S': 87,
    'P': 97,
    'V': 99,
    'T': 101,
    'C': 103,
    #'I': 113,
    'L': 113,
    'N': 114,
    'D': 115,
    #'K': 128,
    'Q': 128,
    'E': 129,
    'M': 131,
    'H': 137,
    'F': 147,
    'R': 156,
    'Y': 163,
    'W': 186
}

mass_dict_2 = {
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
def summa(tmp):
    s = 0
    for i in range(0,len(tmp)):
        s +=tmp[i]
    return s
def masses(i):
    masses = list(mass_dict_2.keys())
    return masses(i)

def mass(peptide):
    parts = [peptide[i:i+1] for i in range(0, len(peptide), 1)]
    m = 0
    for i in range(0,len(peptide)):
        m += mass_dict_1.get(peptide[i])
    return m

def parentmass(spectrum):
    max = 0
    parts = spectrum.split(' ')

    for i in parts:
        number = int(i)
        if max < number:
            max = number
    return max


def expand(leaderboard): # a function which adds one key from dict_mass to each letter of peptide

    masses = list(mass_dict_1.keys())
    #parts = [pep[i:i + 1] for i in range(0, len(pep), 1)]   comment this raw because peptide - not string it`s a list
    if len(leaderboard.keys()) == 1:
        new = dict.fromkeys(list(masses),0)

    else:
        new_list = []
        for i in leaderboard:
            for j in range(0, len(masses)):
                new_list.append(str(i) + masses[j])
        new = dict.fromkeys(new_list, 0)
    return new

def cyclospectrum(pep):
    subpep = []
    sub = []
    sub.append('')
    doubled_s = pep+pep
    for i in range(1, len(pep)):
        for j in range(0, len(pep)):
            subpep = doubled_s[j:j + i]
            sub.append(subpep)
    sub.append(pep)

    mass = []

    for i in range(0, len(sub)):
        m = 0
        if sub[i] == '':
            mass.append(0)
        else:
            for j in range(0, len(sub[i]), 1):
                part = [sub[i][j:j + 1]]
                m += mass_dict_1.get(part[0])
                if j == len(sub[i]) - 1:
                    mass.append(m)
    mass = sorted(mass)
    mass = [str(i) for i in mass]
    #mass = " ".join(mass)      We need a list, not string
    return mass



def theoretical_spectrum(pep):

    subpep = []
    sub = []
    sub.append('')
    doubled_s = pep
    for i in range(1, len(pep)):
        for j in range(0, len(pep)):
            if (i+j)<=len(pep):
                subpep = doubled_s[j:j + i]
                sub.append(subpep)
    sub.append(pep)

    mass = []

    for i in range(0, len(sub)):
        m = 0
        if sub[i] == '':
            mass.append(0)
        else:
            for j in range(0, len(sub[i]), 1):
                part = [sub[i][j:j + 1]]
                m += mass_dict_2.get(part[0])
                if j == len(sub[i]) - 1:
                    mass.append(m)
    mass = sorted(mass)
    mass = [str(i) for i in mass]
    return mass


def linearscore(pep,spectrum):
    theoretical = pep

    parts = spectrum.split(' ')
    experimental = parts

    count = 0

    for i in theoretical_spectrum(theoretical):
        if i in experimental:
            count += 1
            experimental.remove(i)
    return count

def cycloscore(pep,spectrum):
    theoretical = pep

    parts = spectrum.split(' ')
    experimental = parts

    count = 0

    for i in cyclospectrum(theoretical):
        if i in experimental:
            count += 1
            experimental.remove(i)
    return count

def trim(leaderboard, spectrum, n):
    for i in leaderboard:
        leaderboard[i] = linearscore(i,spectrum)

    # sorting our leaderboard table
    sorted_values = sorted(leaderboard.values(),reverse = True)
    true_values = set()
    count = 0
    for i in sorted_values:
        count += 1
        if count <= n:
            true_values.add(i)
        else:
            break


    my_dict2 = {k: v for k, v in leaderboard.items() if v in true_values}

    return my_dict2


def LeaderboardCyclopeptideSequencing(n, spectrum):
    leaderboard = {'' : 0}
    leaderpeptide = ''



    while len(leaderboard.keys()) != 0:
        new_dict = {}
        leaderboard = expand(leaderboard)
        for i in leaderboard:
            if mass(i) == parentmass(spectrum):

                if linearscore(i,spectrum) > linearscore(leaderpeptide, spectrum):
                    leaderpeptide = i
            if mass(i) <= parentmass(spectrum):
                new_dict[i] = leaderboard[i]


        leaderboard = trim(new_dict,spectrum,n)


    return leaderpeptide



n = int(sys.stdin.readline().rstrip())
spectrum = sys.stdin.readline().rstrip()

string = (LeaderboardCyclopeptideSequencing(n,spectrum))

masses = []

for i in string:
    masses.append(str(mass_dict_2[i]))
print('-'.join(masses))
#print(LeaderboardCyclopeptideSequencing(9, '0 71 101 103 113 114 128 131 156 156 172 199 232 242 259 269 270 287 300 303 313 372 372 373 388 398 400 414 431 459 469 486 501 501 503 528 545 570 572 572 587 604 614 642 659 673 675 685 700 701 701 760 770 773 786 803 804 814 831 841 857 874 901 917 917 942 945 959 960 970 972 1002 1073'))

d1 = {
    'AAA' : 'K',
    'AAC' : 'N',
    'AAG' : 'K',
    'AAU' : 'N',
    'ACA' : 'T',
    'ACC' : 'T',
    'ACG' : 'T',
    'ACU' : 'T',
    'AGA' : 'R',
    'AGC' : 'S',
    'AGG' : 'R',
    'AGU' : 'S',
    'AUA' : 'I',
    'AUC' : 'I',
    'AUG' : 'M',
    'AUU' : 'I',
    'CAA' : 'Q',
    'CAC' : 'H',
    'CAG' : 'Q',
    'CAU' : 'H',
    'CCA' : 'P',
    'CCC' : 'P',
    'CCG' : 'P',
    'CCU' : 'P',
    'CGA' : 'R',
    'CGC' : 'R',
    'CGG' : 'R',
    'CGU' : 'R',
    'CUA' : 'L',
    'CUC' : 'L',
    'CUG' : 'L',
    'CUU' : 'L',
    'GAA' : 'E',
    'GAC' : 'D',
    'GAG' : 'E',
    'GAU' : 'D',
    'GCA' : 'A',
    'GCC' : 'A',
    'GCG' : 'A',
    'GCU' : 'A',
    'GGA' : 'G',
    'GGC' : 'G',
    'GGG' : 'G',
    'GGU' : 'G',
    'GUA' : 'V',
    'GUC' : 'V',
    'GUG' : 'V',
    'GUU' : 'V',
    'UAA' : '',
    'UAC' : 'Y',
    'UAG' : '',
    'UAU' : 'Y',
    'UCA' : 'S',
    'UCC' : 'S',
    'UCG' : 'S',
    'UCU' : 'S',
    'UGA' : '',
    'UGC' : 'C',
    'UGG' : 'W',
    'UGU' : 'C',
    'UUA' : 'L',
    'UUC' : 'F',
    'UUG' : 'L',
    'UUU' : 'F'
}

def dna_to_rna(dna):
    rna = ''
    for i in dna:
        if i == "T":
            rna += "U"
        else:
            rna += i
    return rna

def reverse(dna):
    tmp = []
    for i in dna:
        if i == "A":
            tmp.append("T")
        elif i == "G":
            tmp.append("C")
        elif i == "T":
            tmp.append("A")
        elif i == "C":
            tmp.append("G")

    reversed = tmp[::-1]
    reversed = "".join(reversed)
    return reversed

def translate(rna):
    parts = [rna[i:i + 3] for i in range(0, len(rna), 3)]
    count=0
    translated = []
    while count<len(parts):
        translated.append(d1.get(parts[count]))
        count +=1
    return "".join(translated)

dna = input()
peptide = input()
for i in range(0,len(dna)-(3*len(peptide))+1):
    if (translate(dna_to_rna(dna[i:i+(len(peptide)*3)])) == peptide):
        print(dna[i:i+(len(peptide)*3)])
for i in range(0, len(dna) - (3*len(peptide))+1):
    if (translate(dna_to_rna(reverse((dna[i:i+(len(peptide)*3)])))) == peptide):
        print(dna[i:i+(len(peptide)*3)])
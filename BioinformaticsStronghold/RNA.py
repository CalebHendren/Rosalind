def transcribe_dna_to_rna(dna_string):
    return dna_string.replace('T', 'U')
dna = input("Enter DNA sequence: ")
rna = transcribe_dna_to_rna(dna)
print(rna)
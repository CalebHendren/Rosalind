def transcribe_dna_to_rna(dna_string):
    return dna_string.replace('T', 'U')
dna = "GATGGAACTTGACTACGTAAATT"
rna = transcribe_dna_to_rna(dna)
print(rna)
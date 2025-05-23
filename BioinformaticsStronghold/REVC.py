s = input("Enter a DNA sequence: ")

complement_map = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
reverse_complement = ''.join(complement_map[nucleotide] for nucleotide in reversed(s))

print(reverse_complement)
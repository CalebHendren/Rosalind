s = "AAAACCCGGT"

reversed_s = s[::-1]

complement_map = {
    'A': 'T',
    'T': 'A',
    'C': 'G',
    'G': 'C'
}

reverse_complement_s = ""
for char in reversed_s:
    reverse_complement_s += complement_map[char]
    
print(reverse_complement_s)
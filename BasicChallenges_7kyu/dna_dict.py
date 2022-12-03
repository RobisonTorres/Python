print('From Code Wars')
print()

def dna_strand(dna):

    # This function replaces letters of dna.
    dna_pair = \
        {
            'A': 'T',
            'T': 'A',
            'C': 'G',
            'G': 'C'
        }
    return ''.join([dna_pair[let] for let in dna])

print(dna_strand('AGAT'))  # Outputs - TCTA

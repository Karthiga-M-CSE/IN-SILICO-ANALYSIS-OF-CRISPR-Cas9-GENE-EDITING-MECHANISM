# CRISPR-Cas9 In-Silico Analysis
# Beginner Bioinformatics Mini Research Project

# Target DNA sequence
dna_sequence = "ATGCGTACGTTAGCTAGCTAGGCTA"

# Function to create complementary DNA strand
def complement_dna(seq):
    complement = {
        'A': 'T',
        'T': 'A',
        'G': 'C',
        'C': 'G'
    }
    return ''.join(complement[base] for base in seq)

# Function to transcribe DNA to RNA
def transcribe_to_rna(seq):
    return seq.replace('T', 'U')

# Generate complementary DNA
complementary_dna = complement_dna(dna_sequence)

# Generate guide RNA
guide_rna = transcribe_to_rna(complementary_dna)

# Display results
print("=== CRISPR-Cas9 In-Silico Analysis ===\n")

print("Original DNA Sequence:")
print(dna_sequence)

print("\nComplementary DNA Sequence:")
print(complementary_dna)

print("\nGuide RNA Sequence:")
print(guide_rna)

# Simulated target matching
if guide_rna[:10] in transcribe_to_rna(dna_sequence):
    print("\nGuide RNA successfully matched target region.")
else:
    print("\nGuide RNA partially matched target region.")

# GC Content Calculation
gc_count = dna_sequence.count('G') + dna_sequence.count('C')
gc_content = (gc_count / len(dna_sequence)) * 100

print(f"\nGC Content: {gc_content:.2f}%")

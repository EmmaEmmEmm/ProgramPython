def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_genes(prefix, suffixes, dna_sequence):
    valid_genes = []

    for suffix in suffixes:
        start = 0
        while True:
            # Find the prefix in the DNA sequence
            start = dna_sequence.find(prefix, start)
            if start == -1:
                break

            # Find the suffix after the prefix
            end = dna_sequence.find(suffix, start + len(prefix))
            if end == -1:
                break

            # Extract the gene
            gene = dna_sequence[start + len(prefix):end]

            # Check rules
            if is_prime(len(gene)) and prefix not in gene and suffix not in gene:
                valid_genes.append(gene)

            start += 1

    # Remove duplicates and sort alphabetically
    valid_genes = sorted(set(valid_genes))

    return valid_genes

# Input handling
prefix = input().strip()
suffixes = input().strip().split()
dna_sequence = input().strip()

# Find genes
genes = find_genes(prefix, suffixes, dna_sequence)

# Output results
if genes:
    genes = sorted(genes, key=len)
    for gene in genes:
        print(gene)
else:
    print("No gene")
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n/2)+1):
        if n % i == 0:
            return False
    return True
def dna_r(s, e, dna):
    i = 0
    genes = []
    while i < len(dna):
        if dna[i:i+len(s)] == s:
            s_l= i + len(s)
            for j in range(s_l, len(dna)):
                if dna[j:j+3] in e and is_prime(len(dna[s_l:j])):
                    genes.append(dna[s_l:j])
                    break
        i += 1
    genes = sorted(genes)
    genes = sorted(genes, key=len)
    return genes if genes else ["No gene"]

start_dna = input()
ends_dna = input().split()
dna = input()

result = dna_r(start_dna, ends_dna, dna)
for gene in result:
    print(gene)
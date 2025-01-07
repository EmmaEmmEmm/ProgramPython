s_d = input()
e_ds = input().split()
dna = input()

def is_prime(n):
    for i in range(2, int(n/2)+1):
        if n% i == 0:
            return False
    return True
def find(dna):
    genes = []
    i = 0
    while i < len(dna):
        if dna[i:i+len(s_d)] == s_d:
            s_l = i + len(s_d)
            for j in range(s_l, len(dna)):
                if dna[j:j+3] in e_ds and is_prime(len(dna[s_l:j])):
                    genes.append(dna[s_l:j])
                    break
        i = i + 1
    genes = sorted(genes)
    genes = sorted(genes, key=len)
    return genes if genes else ["No gene"]
result = find(dna)
for gene in result:
    print(gene)
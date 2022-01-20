# DNA Sequencer, Ryan Kelley, 01/19/22, 9:49PM, v0.2
# This is a simulated DNA base-pair generator.  It will randomly generate a string of bases, then create the matching string. 

import random 

num_genes = int(input("How many random genes do you want to generate?\n"))
next_gene = ""
gene_sequence0 = ""
gene_sequence1 = ""




x = 0
while x < num_genes: 
    random_gene = int(random.randint(1,4))

    if random_gene == 1: 
        next_gene = "A"
    elif random_gene == 2:
        next_gene = "G"
    elif random_gene == 3: 
        next_gene = "T"
    else: 
        next_gene = "C"

    gene_sequence0 = gene_sequence0 + next_gene
    x += 1

print(gene_sequence0)

for i in gene_sequence0: 
    print(i)
    # if gene_sequence0[i] == "A":
    # gene_sequence1 = gene_sequence1 + "T"



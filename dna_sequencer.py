# DNA Base Pair Generator, Ryan Kelley, 01/19/22, 10:13PM, v0.4
# This is a simulated DNA base-pair generator.  It will randomly generate a string of bases, then create the matching string. 

import random 

num_genes = int(input("How many random bases do you want to generate?\n"))
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
    if i == "A":
        gene_sequence1 = gene_sequence1 + "T"
    elif i == "T":
        gene_sequence1 = gene_sequence1 + "A"
    elif i == "G":
        gene_sequence1 = gene_sequence1 + "C"
    else:
        gene_sequence1 = gene_sequence1 + "G"

print(gene_sequence1)

# TO-DO List 
# Sequence Search:  Allow the user to type in a string of base pairs, iterate through the strings to see if that pattern exists in the string. 
# Simulate mutations in the copied string, i.e. random chance of the wrong base added to the string. 
# Read / write sequences to disk. 


# DNA Base Pair Generator, Ryan Kelley, 01/19/22, 10:13PM, v0.4
# This is a simulated DNA base-pair generator.  It will randomly generate a string of bases, then create the matching string. 

import random 

num_base = int(input("How many random bases do you want to generate?\n"))
next_gene = ""
base_sequence0 = ""
base_sequence1 = ""

x = 0
<<<<<<< Updated upstream

# Generate the initial DNA base sequence.

while x < num_genes: 
=======
while x < num_base: 
>>>>>>> Stashed changes
    random_gene = int(random.randint(1,4))

    if random_gene == 1: 
        next_gene = "A"
    elif random_gene == 2:
        next_gene = "G"
    elif random_gene == 3: 
        next_gene = "T"
    else: 
        next_gene = "C"

    base_sequence0 = base_sequence0 + next_gene
    x += 1

<<<<<<< Updated upstream
# Simulate transcription to generate the matching strand.
=======
print(base_sequence0)
>>>>>>> Stashed changes

for each_base in base_sequence0: 
    if each_base == "A":
        base_sequence1 = base_sequence1 + "T"
    elif each_base == "T":
        base_sequence1 = base_sequence1 + "A"
    elif each_base == "G":
        base_sequence1 = base_sequence1 + "C"
    else:
        base_sequence1 = base_sequence1 + "G"

<<<<<<< Updated upstream

print(gene_sequence0)
print(gene_sequence1)
=======
print(base_sequence1)
>>>>>>> Stashed changes

# TO-DO List 
# Sequence Search:  Allow the user to type in a string of base pairs, iterate through the strings to see if that pattern exists in the string. 
# Simulate mutations in the copied string, i.e. random chance of the wrong base added to the string. 
# Read / write sequences to disk. 


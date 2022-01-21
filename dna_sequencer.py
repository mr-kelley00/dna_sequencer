# DNA Base Pair Generator, Ryan Kelley, 01/20/22, 11:17PM, v0.5
# This is a simulated DNA base-pair generator.  It will randomly generate a string of bases, then create the matching string. 

import random 

num_bases = int(input("How many random bases do you want to generate?\n"))
next_gene = ""
base_sequence0 = ""
base_sequence1 = ""

x = 0

# Generate the initial DNA base sequence.

while x < num_bases: 
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

# Simulate transcription to generate the matching strand.

for each_base in base_sequence0: 
    if each_base == "A":
        base_sequence1 = base_sequence1 + "T"
    elif each_base == "T":
        base_sequence1 = base_sequence1 + "A"
    elif each_base == "G":
        base_sequence1 = base_sequence1 + "C"
    else:
        base_sequence1 = base_sequence1 + "G"


print(base_sequence0)
print(base_sequence1)

# TO-DO List 
# Sequence Search:  Allow the user to type in a string of base pairs, iterate through the strings to see if that pattern exists in the string. 
# Simulate mutations in the copied string, i.e. random chance of the wrong base added to the string. 
# Read / write sequences to disk. 


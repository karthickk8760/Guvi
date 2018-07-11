from itertools import permutations
def allPermutations(str):
     permList = permutations(str)
     for perm in list(permList):
         print (''.join(perm))
str =input(); 
allPermutations(str)

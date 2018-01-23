yours = ['Yale', 'MIT', 'Berkeley']
mine = ['Penn State', 'Yale', 'Wisconsin']

ours1 = mine + yours

ours2 = []
ours2.append(mine)
ours2.append(yours)

print(ours1)
print(ours2)

# Question 1 - how ours1 and ours2 differ from each other
# ours1 creates a new list that includes all six schools
# ours2 creates two separate lists within one list separated by a comma and brackets

# Question 2
yours[1] = 'Villanova'
print(ours1)
print(ours2)
# ours1 does not change because this was a list that was created independently
# ours2 changes because the append function reappends our2, so when yours changed,
# when it was printed again, the print of ours2 changes as well

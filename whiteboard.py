# Looks like some hoodlum plumber and his brother has been running around and damaging your stages again.

# The pipes connecting your level's stages together need to be fixed before you receive any more complaints.

# Pipes list is correct when each pipe after the first index is greater (+1) than the previous one, and that there is no duplicates.

# Task
# Given the a list of numbers, return a fixed list so that the values increment by 1 for each index from the minimum value up to the maximum value (both included).

# Example
# Input:  [1,3,5,6,7,8] Output: [1,2,3,4,5,6,7,8]

# Example
# Input:  [5,10] Output: [5, 6, 7, 8, 9, 10]

# 4,5,8,9 list what came in the function what would be the expected output
# output return a new list 
# want to find the mimimum and the max.
# create a new list, strt at the smallest up the the largest.


def solution(pipelist):
    smallest = min(pipelist)
    largest = max(pipelist)
    return [x for x in range(smallest,largest+1)]
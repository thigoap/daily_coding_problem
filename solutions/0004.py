# 0004 [Hard]
# 2022-27-06
'''
This problem was asked by Stripe.
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
You can modify the input array in-place.
'''

def find_missing(array):
    if len(array) == 0:
        return 1
    sorted_list = list(set(sorted([n for n in array if n > 0])))
    for idx, n in enumerate(sorted_list):
        if idx + 1 != n:
            return idx + 1
    return idx + 2


print(find_missing([3, 4, -1, 1])) # should return 2
print(find_missing([1, 2, 0])) # should return 3
print(find_missing([])) # should return 1

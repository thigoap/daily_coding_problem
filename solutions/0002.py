# 0002 [Hard]
# 2022-26-06
'''
This problem was asked by Uber.
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
Follow-up: what if you can't use division?
'''

from math import prod

def multi_items(array):
    multi = [prod([j for j in array if i != j]) for i in array]
    return multi

print(multi_items([1, 2, 3, 4, 5])) # should return [120, 60, 40, 30, 24]
print(multi_items([3, 2, 1])) # should return [2, 3, 6]
print(multi_items([5, 2])) # should return [2, 5]
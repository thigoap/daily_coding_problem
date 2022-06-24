# 0001 [Easy]
# 2022-24-06
'''
This problem was recently asked by Google.
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?
'''

def check_items(numbers_list, result):
    for idx, i in enumerate(numbers_list):
        for j in range(idx + 1, len(numbers_list)):
            if i + numbers_list[j] == result:
                return True
    return False


print(check_items([10, 15, 3, 7], 10)) # should return True
print(check_items([10, 15, 3, 0], 17)) # should return False
print(check_items([5], 17)) # should return False

# Given an integer array nums, return True if any value appears at least twice in the array, and False if every element is distinct.
def duplicate(nums):
    s=set()
    for i in nums:
        if i in s:
            return True
        s.add(i)
    return False
print(duplicate([1,2,3,1]))
print(duplicate([1,2,3,4]))
print(duplicate([1,1,1,3,3,4,3,2,4,2]))
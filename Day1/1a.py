#Given an array of integers nums and an integer target, return the indices of the two numbers that add up to target. You may not use the same element twice. Exactly one solution always exists.
def two_sum(nums,target):
    d={}
    for i in range(len(nums)):
        ans=target-nums[i]
        if ans in d:
            return [d[ans],i]
        d[nums[i]]=i
    return []
print(two_sum([2,7,11,15],9))
print(two_sum([3,2,4],6))
print(two_sum([3,3],6))

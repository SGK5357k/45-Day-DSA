# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
def max_subarray(nums):
    max_sum=nums[0]
    curr=0
    for i in nums:
        curr=max(i,curr+i)
        max_sum=max(curr,max_sum)
    return max_sum

print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))
print(max_subarray([1]))
print(max_subarray([5,4,-1,7,8]))

#Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals k. A subarray is a contiguous part of the array.
def subarray_sum_k(nums,k):
    count=0
    d={0:1}
    curr_sum=0
    for i in nums:
        curr_sum+=i
        if curr_sum-k in d:
            count+=d[curr_sum-k]
        d[curr_sum]=d.get(curr_sum,0)+1
    return count
print(subarray_sum_k([1,1,1],2))
print(subarray_sum_k([1,2,3],3))
print(subarray_sum_k([-1,-1,1],0))
print(subarray_sum_k([1,2,1,2,1],3))


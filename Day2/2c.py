#Given an integer array nums, find a contiguous subarray (at least one element) that has the largest product, and return that product. The array can have negative numbers and zeros.
def max_product_subarray(nums):
    curr_max=nums[0]
    curr_min=nums[0]
    global_max=nums[0]
    for i in range(1,len(nums)):
        new_max=max(nums[i],curr_max*nums[i],curr_min*nums[i])
        new_min=min(nums[i],curr_max*nums[i],curr_min*nums[i])
        curr_max=new_max
        curr_min=new_min
        global_max=max(global_max,curr_max)
    return global_max
print(max_product_subarray([2,3,-2,4]))
print(max_product_subarray([-2,0,-1]))
print(max_product_subarray([-2,3,-4]))

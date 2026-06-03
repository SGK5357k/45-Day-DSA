#Given an integer array nums, return an array output where output[i] is the product of all elements of nums except nums[i]. You must solve it in O(n) time and without using division operator
def product_except_self(sums):
    output=[]
    left=1
    for i in range(len(sums)):
        output.append(left)
        left*=sums[i]
    right=1
    for i in range(len(sums)-1,-1,-1):
        output[i]*=right
        right*=sums[i]
    return output
print(product_except_self([1,2,3,4]))
print(product_except_self([-1,1,0,-3,3]))
print(product_except_self([2,3,4,5]))

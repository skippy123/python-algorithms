"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array

[ -2,1, -3,4, -1,2,1, -5,4 ]

the contiguous subarray 
[ 4, -1, 2, 1 ] 
has the largest sum = 6.

"""
max_list= []
import sys

#O(nlogn) Solution
def maxSubArray1(nums):
    
    if len(nums) ==1:
        return nums[0]

    index = len(nums)/2

    a1 = nums[0:index]
    a2 = nums[index:]

    l_s = maxSubArray(a1)
    r_s = maxSubArray(a2)
    
    lsum = -1 * sys.maxint 
    rsum = -1 * sys.maxint
    ssum = 0
    
    for i in a1:
        ssum += i
        lsum = max(ssum ,lsum)

    ssum = 0

    for i in a2:
        ssum += i
        rsum = max(ssum, rsum)

    
    ans = max(l_s ,  r_s)
    return max(ans, lsum+rsum)


#O(n) solution
def maxSubArray(nums):

    temp = 0
    max_sum = temp
    for i in  nums:
        temp = max(temp+i , i)
        if temp > max_sum:
            temp = max_sum
    return max_sum






nums = [ -2,1, -3,4, -1,2,1, -5,4 ]

print maxSubArray(nums)






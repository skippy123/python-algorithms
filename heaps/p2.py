"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element 
in the sorted order, not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

quick soln:
        nums.sort()
        return nums[len(nums)-k]
        O(nlogn)


Below is the O(n) solution
"""
from random import randint

def findKthLargest(nums, k):
    left, right = 0, len(nums) - 1
    while left <= right:
        pivot_idx = randint(left, right)
        new_pivot_idx = PartitionAroundPivot(left, right, pivot_idx, nums)
        if new_pivot_idx == k - 1:
            return nums[new_pivot_idx]
        elif new_pivot_idx > k - 1:
            right = new_pivot_idx - 1
        else:  # new_pivot_idx < k - 1.
            left = new_pivot_idx + 1
    
def PartitionAroundPivot(left, right, pivot_idx, nums):
    pivot_value = nums[pivot_idx]
    new_pivot_idx = left
    nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
    for i in xrange(left, right):
        if nums[i] > pivot_value:
            nums[i], nums[new_pivot_idx] =  nums[new_pivot_idx], nums[i]
            new_pivot_idx += 1
        
    nums[right], nums[new_pivot_idx] = nums[new_pivot_idx], nums[right]
    return new_pivot_idx

print findKthLargest([3,2,7,1,5,6,4], 2)

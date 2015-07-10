"""

A peak element is an element that is greater than its neighbors.

Given an input array where num[i] not equals num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -infinity.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.

"""


def findPeakElement( nums, mid_index=-10):
    
    #import pdb; pdb.set_trace()
    if nums is None:
        return -1
    
    if len(nums) == 1:
        return 0
    
    if len(nums) == 2:
            if nums[0] > nums[1]:
                return 0
            return 1
    
    n = len(nums)
    if mid_index == -10:
        mid = n/2
    else:
        if mid_index == -1 or mid_index == n:
            return
        mid = mid_index
    
    if mid -1 > 0 and mid+1 < n:
        peak = max(nums[mid], nums[mid-1], nums[mid+1])
    elif mid -1 > 0:
        peak = max(nums[mid], nums[mid-1] )
    elif mid +1 < n:
         peak = max(nums[mid], nums[mid+1] )
    else:
        return
    
    if peak == nums[mid]:
        return mid
    elif peak == nums[mid-1]:
        return findPeakElement(nums, mid_index=mid-1)
    else:
        return findPeakElement(nums, mid_index=mid+1)

print findPeakElement([1,2,1])


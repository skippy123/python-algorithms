

nums1 = [1,2,3,4,5]
nums2 = [6,7,8,9,10]

def get_median(a, b, k):
    
    if len(a) >len(b): return get_median(b, a, k)
    if len(a) == 0 : return b[k-1]
    if k==1: return  min(a[0],b[0])

    pa = min(k/2, len(a))
    pb = k - pa

    if a[pa-1] <= b[pb-1]:
        return get_median(a[pa:] , b, pb)
    else:
        return get_median(a, b[:pb])




def findMedianSortedArrays( nums1, num2 ):

    k = (len(nums1) + len(nums2) )/2
    if (len(nums1) + len(nums2) )%2 != 0:
        return get_median(nums1, nums2, k+1 )
    else:
        return (get_median(nums1, nums2, k) + get_median(nums1 , nums2, k+1))*0.5



        
print findMedianSortedArrays( nums1, nums2)
"""
Maximal product subarray problem

[2,3, -2,4] -> [2,3]

"""

def maxProduct(nums):

    max_temp = min_temp = max_prod = nums[0]

    for i in xrange(1, len(nums)):

        t_max =  max( max_temp*nums[i], nums[i], min_temp*nums[i] )
        t_min = min( min_temp*nums[i], nums[i] , max_temp*nums[i] )

        max_temp = t_max
        min_temp = t_min

        if max_temp > max_prod:
            max_prod = max_temp

    print max_prod

#maxProduct([-4,-3,-2])


## 
##  Below are the sources for python itertools built in functions
## 

def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    #import pdb;pdb.set_trace()
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = range(r)
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1

        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1

        yield tuple(pool[i] for i in indices)

#for k in combinations([1,2,3,4,5,6],3):
#    print k


def combinationSum3( k, n):
        
        nums = [j for  j in xrange(1,10)]
        res = []
        import itertools

        for i in nums:
            if i <= n:
                res.append([i])

        for rows in xrange(1,k):

            if rows == k-1:
                res = [ list(set(r+[i])) for r in res for  i in nums  if reduce(lambda x, y: x+y, r) + i == n  and len(r) == k-1]
            else:
                res = [ list(set(r+[i])) for r in res for  i in nums  if reduce(lambda x, y: x+y, r) + i <= n ]
        
        res.sort()
        out = []
        for k1,_ in itertools.groupby(res):
            if len(k1) == k:
                out.append(k1)
        
        print out

#combinationSum3(3, 9)


def imap(function, *iterables):
    # imap(pow, (2,3,10), (5,2,3)) --> 32 9 1000
    import pdb;pdb.set_trace()
    iterables = map(iter, iterables)
    while True:
        args = [next(it) for it in iterables]
        if function is None:
            yield tuple(args)
        else:
            yield function(*args)


#for k in imap(pow, (2,3,10), (5,2,3)):
#    print k

def combinationSum2(candidates, target):
    
    candidates.sort()
    out = []
    result = []
    
    import itertools
    for i,k in  enumerate(candidates):

        if  k == target:
            result.append([k])
            continue

        out.append( [(k,i)] )    

    for i in xrange(1,  len(candidates)):
        
        print out
        out = [ sorted( (r + [(j,k1)]) , key= lambda x:x[0]) for r in  out for k1,j in  enumerate(candidates) if reduce( lambda x,y: x[0]+y[0], r) <= target-j and k1 not in [z[1] for z in r ]  ]
        print out
        out.sort()
        for _,k1 in itertools.groupby(out):
            if reduce( lambda x,y : x[0]+y[0], k1) == target :
                result.append( [k2[0] for k2 in k] )

    print out

#combinationSum2([1,1], 2)

def maxProfit(prices):
    
        if not prices:
            return 0 
        a = prices
        i = 0
        n = len(prices)
        
        diff = 0
        local_min = a[0]
        start_idx = 0

        while True:
            
            if  i == n:
                break

            #local maxima
            while i < len(prices)-1 and a[i+1] > a[i]:
                i += 1

            #i += 1
            if i == n:
                break
            
            import pdb; pdb.set_trace()
            local_max = a[i]
            local_min = min( a[start_idx: i+1] )
            
            diff += (local_max - local_min)
            
            i += 1
            start_idx = i
        
        return diff

#print maxProfit( [2,1,2,0,1] )


def largestNumber( nums):
    
    import itertools
    import math

    l = nums
    max_n = max(l)
    num_digits = int(math.log( max_n , 10)) + 1
    #import pdb;pdb.set_trace()
    temp = []
    for k in l :
        
        digs = int(math.log( k ,10 )) + 1
        k1 = ''
        flag = False
        for j in xrange( 0,  num_digits - digs  ):
            k1 += str(k)[-1] 
            flag = True

        if not flag:
            temp.append(  (str(k), str(k))  )
        else:
            temp.append( (str(k)+ k1, str(k)) )

    temp = sorted( temp, key=lambda x:x[0] , reverse=True )
    out = ''

    for k in temp:
        out += k[1]
    
    return out

#print largestNumber( [3, 30, 34, 5, 9] )


def divide( dividend, divisor):
        
    import sys
    
    if divisor == 0:
        return sys.maxint
        
    t1 = divisor & 1
    tmp = dividend
    
    while divisor > 0:
        #import pdb;pdb.set_trace()
        dividend =  dividend >> (divisor & 1)
        divisor = divisor >> 1
            
    return dividend

#print divide(100,10) 


def wordBreak(s, wordDict):
    
    
    dum = ''.join(['#']*len(s))
    words = list(wordDict)
    
    for i in xrange(0, len(words)):
        
        word = words[i]
        j = 0
        f = False
        temp = s
        for k in xrange(len(temp)):
            
            if s[k] == word[j]:
                
                f = True
                if j == len(word)-1:
                    s = s[ : k-len(word)+1 ] + ''.join(['#']*len(word))+s[k+1:]
                    break
                j += 1
            else:
                j = 0
                f = False
            
        if s == dum:
            return True
    
    return False

#print wordBreak("leetscode", ["leet", "code"])

def minSubArrayLen( s, nums):


    n = len(nums)
    start = 0
    end = 0
    sm = 0
    best = n +1
    while end < n:

        while end < n and  sm < s:

            sm += nums[end]
            end += 1

        while  start < end  and sm >= s:

            if sm >= s:
                best = min(best, end-start)

            sm -= nums[start]
            start += 1

    return [0, best] [best <= n]

#print minSubArrayLen(7, [2,3,1,2,4,3])

def combinationSum( candidates, target):

    if not candidates or len(candidates) == 0:
        return 0

    res = []
    out = []
    candidates.sort() 
    import itertools

    for k in candidates:
        res.append([k])

    for k in res:
        if sum(k) == target:
            out.append(k)
            break


    for k in xrange(1, len(candidates)):

        res = [  sorted(r + [i]) for r in res for i in candidates if sum(r) + i <= target  ]
        res = sorted(res)
        for k,_ in itertools.groupby(res):
            if sum(k) == target:
                out.append(k)

    return len(out)

#print combinationSum( [2,3,6,7], 7 )



def getMedian(a, b):

    an = len(a)
    bn = len(b)

    def getK(a, b, k):

        if len(a) > len(b) : return getK(b,a, k)
        if len(a) == 0: return b[k-1]
        if  k ==1 : return min( a[0], b[0])

        pa = min( k/2 , len(a) ) ; pb = k - pa
        
        if a[k-1] <= b[k-1]:
            return getK( a[pa:], b, pb)
        elif a[k-1] > b[k-1]:
            return getK( a, b[pb:], pa )

    if (an + bn)%2 == 1:
        return getK(a, b, (an + bn)/2 + 1)
    else:
        return ( getK(a, b, (an + bn)/2 + 1) + getK(a, b, (an + bn)/2 ) )* 0.5


a = [1,2,3,4,5]
b = [6,7,8]
print getMedian(a,  b)























































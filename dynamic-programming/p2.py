"""
 Given a rope of length n , split it into integer segmenets so that the product is the max_p
 example : n = 5 , soln 2,3 as prod is 6
 n =10 , soln is 3,4,3 as producet is 36 and so on ....

"""

def max_prod(n):

    max_p = 1
    a = [ i for i in xrange(1,n)]
    num1 =1
    num2 = 1

    if n == 2:
        return 1
    if n ==3:
        return 2

    for i in xrange(0, n/2+1):

        j = -1-i

        if i == j:
            temp = a[i]*a[i]
        else:
            temp = a[i]*a[j]

        if max_p < temp:
            max_p = temp
            num1 = a[i]
            num2 = a[j]

    if num1 != 1:
        num1 =  max( max_prod(num1), num1)

    if num2 != 1:
        num2 =  max( max_prod(num2), num2)

    return  num1 * num2


def dynamic_prod(n):

    table = [0]*(n+1)

    for  i in xrange(1, n+1):

        temp = 1
        for j in  xrange(1, i/2+1):
            temp = max( temp , max( (i-j)*j , j*table[i-j]) )

        table[i] = temp
        print table

    return table[n]

#print max_prod(10)
print dynamic_prod(10)


#print max_prod(6)
#print max_prod(5)
#print max_prod(4)
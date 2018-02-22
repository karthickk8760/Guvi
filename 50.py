def isPowerOfTwo(n):
    if (n == 0):
        return False
    while (n != 1):
            if (n % 2 != 0):
                return False
            n = n // 2
             
    return True
 
# Driver code
a=input()
if(isPowerOfTwo(a)):
    print('Yes')
else:
    print('No')
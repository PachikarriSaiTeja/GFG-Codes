import math
class Solution:
    def noOfDigits(self, n):
        
        if n==0 or n==1:
            return n
        mod=1000000007
        a=0
        b=1
        c=a+b
        for i in range(2,n+1):
            a=b
            b=c
            c=(a+b)
        return math.floor(math.log10(b)+1)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.noOfDigits(N))
# } Driver Code Ends
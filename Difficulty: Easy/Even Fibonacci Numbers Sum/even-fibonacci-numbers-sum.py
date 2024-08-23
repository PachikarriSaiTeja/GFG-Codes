#User function Template for python3

class Solution:
    def evenFibSum (self, N):
        a=0
        cnt=0
        b=1
        c=a+b
        while(b<=N):
            if b%2==0:
                cnt+=b
            a=b
            b=c
            c=a+b
            
        return cnt


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.evenFibSum(N))
# } Driver Code Ends
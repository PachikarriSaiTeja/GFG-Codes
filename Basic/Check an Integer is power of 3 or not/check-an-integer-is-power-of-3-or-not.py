#User function Template for python3
class Solution:
    def isPowerof3(self, N):
        if N<=0:
            return "No"
        for i in range(0,32):
            if(N==3**i):
                return "Yes"
        return "No"
        # code here 


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N=int(input())

        ob = Solution()
        print(ob.isPowerof3(N))
# } Driver Code Ends
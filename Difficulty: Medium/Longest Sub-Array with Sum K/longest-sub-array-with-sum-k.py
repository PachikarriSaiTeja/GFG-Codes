#User function Template for python3

class Solution:
    def lenOfLongSubarr (self, arr, n, k):
        ans={0:-1}
        an=0
        total=0
        for i in range(n):
            total+=arr[i]
            if total-k in ans:
                an=max(i-ans[total-k],an)
            if total not in ans:
                ans[total]=i
        return an
            
        #Complete the function
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n, k = map(int , input().split())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.lenOfLongSubarr(arr, n, k))




# } Driver Code Ends
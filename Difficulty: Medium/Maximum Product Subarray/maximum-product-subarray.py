#User function Template for python3
#User function Template for python3
class Solution:

    # Function to find maximum
    # product subarray
    def maxProduct(self,arr):
        if(len(arr)==1):
            return arr[0]
        maxn=arr[0]
        maxt=arr[0]
        mint=arr[0]
        for i in range(1,len(arr)):
            if arr[i]<0:
                maxn,mint=mint,maxn
            maxn=max(arr[i],maxn*arr[i])
            mint=min(arr[i],mint*arr[i])
            maxt=max(maxt,maxn)
        return(maxt)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr)
        print(ans)
        tc -= 1

# } Driver Code Ends
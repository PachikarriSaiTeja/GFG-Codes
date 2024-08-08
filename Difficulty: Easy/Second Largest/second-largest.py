#User function Template for python3
class Solution:
    def print2largest(self, arr):
        # Code Here
        m=-9999
        ms=-9999
        for i in range(len(arr)):
            if arr[i]>m:
                ms=m
                m=arr[i]
            elif arr[i]>ms and arr[i]<m:
                ms=arr[i]
        if ms==m:
            return -1
        return ms

#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.print2largest(arr)
        print(ans)

# } Driver Code Ends
#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        
        ans={0:-1}

        total=0
        mx=0
        for i in range(len(arr)):
            total+=arr[i]
            if total in ans:
                mx=max(mx,i-ans[total])
            if total not in ans:
                ans[total]=i
        return mx
                
            
        #Code here


#{ 
 # Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends
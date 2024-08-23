#User function Template for python3

class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def doUnion(self,arr1,arr2):
        #code here
        ans={}
        cnt=0
        for i in arr1:
            if i not in ans:
                ans[i]=1
                cnt+=1
        for i in arr2:
            if i not in ans:
                ans[i]=1
                cnt+=1
        return cnt


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()

        print(ob.doUnion(a, b))

# } Driver Code Ends
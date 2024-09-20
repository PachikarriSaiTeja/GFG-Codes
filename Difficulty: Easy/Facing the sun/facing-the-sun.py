#User function Template for python3

class Solution:
    # Returns count buildings that can see sunlight
    def countBuildings(self, height):
        rmax=height[0]
        tmax=max(height)

        cnt=1
        if tmax!=height[0]:
            cnt+=1
        i=0

        while height[i]!=tmax:
            if height[i]>rmax:
                cnt+=1
                rmax=height[i]
            i+=1
        return cnt
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        height = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.countBuildings(height)
        print(ans)

# } Driver Code Ends
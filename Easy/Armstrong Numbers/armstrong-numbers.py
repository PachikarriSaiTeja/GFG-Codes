#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        m=n
        s=0
        while(m!=0):
            re=m%10
            s+=re**3
            m=m//10
        if(n==s):
            return "true"
        return "false"


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = input()
        n = int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))

# } Driver Code Ends
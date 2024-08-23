# User function Template for python3

class Solution:
    # Complete this function
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,arr):
        total=sum(arr)
        a=[]
        found=False
        b=[]
        pr=0
        sf=0
        for i in range(len(arr)):
            if total-pr-arr[i]==pr:
                return(i+1)
                found=True
            pr+=arr[i]
        if(found==False):
            return -1

        
            
            
        # Your code here



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.equilibriumPoint(arr))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
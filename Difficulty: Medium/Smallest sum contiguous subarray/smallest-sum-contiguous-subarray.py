#User function Template for python3


class Solution:
    def smallestSumSubarray(self, A, N):
        mn=A[0]
        ms=A[0]
        for i in range(1,N):
            mn=min(A[i],A[i]+mn)
            ms=min(ms,mn)
        return ms
        #Your code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3


import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.smallestSumSubarray(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends
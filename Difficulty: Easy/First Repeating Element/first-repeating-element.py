#User function Template for python3

class Solution:
    #Function to return the position of the first repeating element.
    def firstRepeated(self,arr):
        
        #arr : given array
        #n : size of the array
        m=999
        k={}
        f=False
        for i in range(len(arr)):
            if(arr[i] in k):
                m=min(k[arr[i]],m)
                f=True
                
            else:
                k[arr[i]]=i
        if(f):
            return m+1
        return -1
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.firstRepeated(arr))

# } Driver Code Ends
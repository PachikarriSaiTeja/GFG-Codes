class Solution:
    def alternateSort(self,arr):
        ar=sorted(arr)
        i=0
        a=[]
        j=len(ar)-1
        while(i<j):
            a.append(ar[j])
            a.append(ar[i])
            i+=1
            j-=1
        if(len(ar)%2!=0):
            a.append(ar[j])
        return a
            
        
        # Your code goes here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Position this line where user code will be pasted.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.alternateSort(arr)
        print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends
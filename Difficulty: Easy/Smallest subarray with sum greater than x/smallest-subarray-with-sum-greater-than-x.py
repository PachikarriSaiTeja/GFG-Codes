class Solution:
    def smallestSubWithSum(self, x, arr):
        
        
        j=0
        sub=[]
        total=0
        for i in range(len(arr)):
            total+=arr[i]
            while total>x:
                sub.append(i+1-j)
                total-=arr[j]
                j=j+1
        if len(sub)>0:
            return min(sub)
        return 0
        # Your code goes here 
        



#{ 
 # Driver Code Starts
def main():

    T = int(input())

    while (T > 0):
        x = int(input())
        a = [int(x) for x in input().strip().split()]
        print(Solution().smallestSubWithSum(x, a))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
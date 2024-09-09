class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        
        j=len(arr)-1
        i=0
        m=0
        temp=0
        while(m<=j):
            if arr[m]==2:
                temp=arr[m]
                arr[m]=arr[j]
                arr[j]=temp
                j-=1
            elif arr[m]==0:
                temp=arr[m]
                arr[m]=arr[i]
                arr[i]=temp
                i+=1
                m+=1
            else:
                m+=1
        return arr

        # code here


#{ 
 # Driver Code Starts
def main():
    t = int(input().strip())  # Read the number of test cases
    ob = Solution()

    while t > 0:
        t -= 1
        arr = list(map(int,
                       input().strip().split())
                   )  # Read the array as space-separated integers
        ob.sort012(arr)  # Sort the array

        print(' '.join(map(str, arr)))  # Print the sorted array


if __name__ == "__main__":
    main()

# } Driver Code Ends
# your task is to complete this function
# function should return index to the any valid peak element
class Solution:   
    def peakElement(self,arr, n):
        if len(arr)==1:
            return 0
        elif len(arr)==2:
            return arr.index(max(arr))
        for i in range(len(arr)):
            if i==0 and arr[i]>=arr[i+1]:
                return i
            elif i==len(arr)-1 and arr[i-1]<=arr[i]:
                return i
            else:
                if arr[i-1]<=arr[i] and arr[i+1]<=arr[i]:
                    return i
            
        # Code here



#{ 
 # Driver Code Starts

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        index = Solution().peakElement(arr.copy(), n)
        flag = False
        if index<0 or index>=n:
            flag = False
        else:
            if index == 0 and n==1:
                flag = True
            elif index==0 and arr[index]>=arr[index+1]:
                flag = True
            elif index==n-1 and arr[index]>=arr[index-1]:
                flag = True
            elif arr[index-1] <= arr[index] and arr[index] >= arr[index+1]:
                flag = True
            else:
                flag = False

        if flag:
            print(1)
        else:
            print(0)
# Contributed by: Harshit Sidhwa

# } Driver Code Ends
#User function Template for python3

class Solution:
    ##Complete this function
    def pairInSortedRotated(self,arr, target):
        maxInd=len(arr)-1
        minInd=0
        for i in range(1,len(arr)):
            if arr[i]<arr[i-1]:
                maxInd=i-1
                minInd=i
        addSum=0
        j=maxInd
        i=minInd
        while(i!=j):
            addSum=arr[i]+arr[j]
            if(addSum==target):
                return True
            elif(addSum>target):
                j-=1
            else:
                i+=1
            if j==-1:
                j=len(arr)-1
            if i==len(arr):
                i=0
        return False
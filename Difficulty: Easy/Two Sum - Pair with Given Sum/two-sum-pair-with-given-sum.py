class Solution:
	def twoSum(self, arr, target):
		i=0
		j=len(arr)-1
		arr=sorted(arr)
		while(i<j):
		    
		    su=arr[i]+arr[j]
		    
		    if(su==target):
		        return True
		    elif su>target:
		        j-=1
		    else:
		        i+=1
		return False 
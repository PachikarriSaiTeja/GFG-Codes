#User function Template for python3
class Solution:
	def isSame(self, s):
	    jk=""
	    for i in s:
	        if (i.isdigit()):
	            jk=jk+i
	    k=int(jk)
	    if(k==len(s)-len(jk)):
	        return 1
	    return 0     
	 
	   
	      
		# code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		
		ob = Solution()	
		answer = ob.isSame(s)
		
		print(answer)


# } Driver Code Ends
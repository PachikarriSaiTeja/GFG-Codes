#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    
    #Complete this fuction
    #Function to count the number of subarrays which adds to the given sum.
    def subArraySum(self, arr, tar):
                pr = 0
                prm = {0: 1}  # Start with a sum of 0 that has occurred once
                cnt = 0
                
                for i in range(len(arr)):
                    pr += arr[i]  # Update the prefix sum
                    
                    # Check if there's a prefix sum that would make a subarray sum to tar
                    if (pr - tar) in prm:
                        cnt += prm[pr - tar]  # Add the number of times this prefix sum has occurred
                    
                    # Add/update the current prefix sum in the map
                    if pr in prm:
                        prm[pr] += 1
                    else:
                        prm[pr] = 1
                        
                return cnt

                
            
        
        #Your code here

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        tar= int(input())
        ob = Solution()
        res = ob.subArraySum(arr,tar)
        print(res)
        # print("~")
        t -= 1


# } Driver Code Ends
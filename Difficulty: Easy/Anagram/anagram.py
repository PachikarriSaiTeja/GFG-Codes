#User function Template for python3
class Solution:
    
    # Function to check whether two strings are anagrams of each other.
    def areAnagrams(self, s1, s2):
        if len(s1) != len(s2):
            return False  # Quick check to avoid unnecessary work
        
        mp = {}
        for ch in s1:
            mp[ch] = mp.get(ch, 0) + 1  # Count characters in s1
        
        for ch in s2:
            if ch in mp:
                mp[ch] -= 1
                if mp[ch] < 0:
                    return False  # More occurrences in s2 than in s1
            else:
                return False  # Character not in s1 at all
        
        # If all values are zero, strings are anagrams
        return all(value == 0 for value in mp.values())

        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a = input().strip()
        b = input().strip()
        if (Solution().areAnagrams(a, b)):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends
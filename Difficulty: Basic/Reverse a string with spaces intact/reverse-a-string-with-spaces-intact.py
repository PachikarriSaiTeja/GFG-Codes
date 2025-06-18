#User function Template for python3

class Solution:
    def reverseWithSpacesIntact(self, s):
        if len(s) <= 1:
            return s

        spaces = set()
        for i in range(len(s)):
            if s[i] == " ":
                spaces.add(i)

        

        if len(spaces) == 0:
            return s[::-1]

        str_arr = [c for c in s if c != " "]
        str_arr=str_arr[::-1]
        ans = []
        ind=0

        for i in range(len(s)):
            if i in spaces:
                ans.append(" ")
            else:
                ans.append(str_arr[ind])
                ind+=1

        return ''.join(ans)

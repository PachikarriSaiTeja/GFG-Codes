class Solution:
    # FunctIon to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        zI=0
        tI=len(arr)-1
        i=0
        while(i<=tI):
            if arr[i]==0:
                arr[i],arr[zI]=arr[zI],arr[i]
                zI+=1
                i+=1
            elif arr[i]==2:
                arr[i],arr[tI]=arr[tI],arr[i]
                tI-=1
            else:
                i+=1
            
        
                
            
        
        
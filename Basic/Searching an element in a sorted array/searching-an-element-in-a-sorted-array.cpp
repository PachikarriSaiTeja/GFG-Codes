//{ Driver Code Starts
#include <bits/stdc++.h> 
using namespace std;


// } Driver Code Ends
class Solution{
    public:
    int searchInSorted(int arr[], int N, int K) 
    { 
    int i=0,j=N-1;
      int f=arr[i];
      int l=arr[j];
      while(i<=j)
      {
          int m=i+(j-i)/2;
          if(arr[m]==K)
          {
              return 1;
          }
          else if(arr[m]>K)
          {
              j=m-1;
          }
          else if(arr[m]<K)
          {
              i=m+1;
          }
      }
      return -1;
       
    }
};

//{ Driver Code Starts.


int main(void) 
{ 
    
    int t;
    cin >> t;
    while(t--){
        int n, k;
        cin >> n >> k;
        
        int arr[n];
        
        for(int i = 0;i<n;i++){
            cin >> arr[i];
        }
        
        Solution ob;
        cout << ob.searchInSorted(arr, n, k) << endl;

    }

	return 0; 
} 

// } Driver Code Ends
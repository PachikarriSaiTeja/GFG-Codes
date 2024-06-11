//{ Driver Code Starts
// Initial template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function template for C++

class Solution {
  public:
    int binarysearch(int arr[], int n, int k) 
    {
        int i=0,j=n-1;
     
        int f=arr[i];
        int l=arr[j];
        while(i<=j){
          int m=i+(j-i)/2;  
                if(k<arr[m])
                {
                j=m-1;
                }
                else if(k>arr[m])
                {
                    i=m+1;
                }
                else
                {
                    return m;
                }
            }
            return -1;
        }
};


//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;

    while (t--) {
        int N;
        cin >> N;
        int arr[N];
        for (int i = 0; i < N; i++) cin >> arr[i];
        int key;
        cin >> key;
        Solution ob;
        int found = ob.binarysearch(arr, N, key);
        cout << found << endl;
    }
}

// } Driver Code Ends
//{ Driver Code Starts
import java.io.*;
import java.util.*;
import java.util.stream.*;

class Array {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter ot = new PrintWriter(System.out);
        int t = Integer.parseInt(br.readLine().trim()); // Inputting the testcases

        while (t-- > 0) {

            // input size of array
            int n = Integer.parseInt(br.readLine().trim());
            int arr[] = new int[n];
            String inputLine[] = br.readLine().trim().split(" ");

            // inserting elements in the array
            for (int i = 0; i < n; i++) {
                arr[i] = Integer.parseInt(inputLine[i]);
            }

            Solution obj = new Solution();

            StringBuffer str = new StringBuffer();
            ArrayList<Integer> res = new ArrayList<Integer>();

            // calling leaders() function
            res = obj.leaders(n, arr);

            for (int i = 0; i < res.size(); i++) {
                ot.print(res.get(i) + " ");
            }

            ot.println();
        }
        ot.close();
    }
}

// } Driver Code Ends


class Solution {
    // Function to find the leaders in the array.
    static ArrayList<Integer> leaders(int n, int arr[]) {
        
        Stack<Integer> st=new Stack<>();
        ArrayList<Integer> al=new ArrayList<>();
        for(int i=arr.length-1;i>=0;i--)
        {
            if(!st.isEmpty())
            {
                while(!st.isEmpty() && st.peek()<=arr[i])
                {
                    st.pop();
                }
            }
            if(st.isEmpty())
            {
                al.add(0,arr[i]);
            }
            st.add(arr[i]);
        }
        return al;
        // Your code here
    }
}

//{ Driver Code Starts
import java.util.*;
import java.io.*;
import java.lang.*;

class Driverclass
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        
        //Reading total number of testcases
        int t= sc.nextInt();
        
        while(t-- >0)
        {
            //reading the string
            String st = sc.next();
            
            //calling ispar method of Paranthesis class 
            //and printing "balanced" if it returns true
            //else printing "not balanced"
            if(new Solution().ispar(st) == true)
                System.out.println("balanced");
            else
                System.out.println("not balanced");
        
        }
    }
}
// } Driver Code Ends



class Solution {
    // Function to check if brackets are balanced or not.
    static boolean ispar(String x) {
        // If the length of the string is odd, it cannot be balanced
        if (x.length() % 2 != 0) {
            return false;
        }
        
        Stack<Character> st = new Stack<>();
        
        for (int i = 0; i < x.length(); i++) {
            char ch = x.charAt(i);
            
            // If it's an opening bracket, push it onto the stack
            if (ch == '{' || ch == '(' || ch == '[') {
                st.push(ch);
            } 
            // If it's a closing bracket
            else if (ch == '}' || ch == ']' || ch == ')') {
                // If the stack is empty, there's no matching opening bracket
                if (st.isEmpty()) {
                    return false;
                }
                
                // Check for matching pairs
                if ((ch == '}' && st.peek() == '{') ||
                    (ch == ']' && st.peek() == '[') ||
                    (ch == ')' && st.peek() == '(')) {
                    st.pop(); // If they match, pop the opening bracket
                } else {
                    return false; // Mismatched brackets
                }
            }
        }
        
        // If the stack is empty, all brackets were matched
        return st.isEmpty();
    }
}

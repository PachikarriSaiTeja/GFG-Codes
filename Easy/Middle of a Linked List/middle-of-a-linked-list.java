//{ Driver Code Starts
import java.util.*;
import java.io.*;

class Node{
    int data;
    Node next;
    
    Node(int x){
        data = x;
        next = null;
    }
    
}
class GFG{
	static void printList(Node node) 
	{ 
		while (node != null) 
		{ 
			System.out.print(node.data + " "); 
			node = node.next; 
		} 
		System.out.println(); 
	}
    public static void main(String args[]) throws IOException { 
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while(t > 0){
        	int n = sc.nextInt();
            Node head = new Node(sc.nextInt());
            Node tail = head;
            for(int i=0; i<n-1; i++)
            {
                tail.next = new Node(sc.nextInt());
                tail = tail.next;
            }
            Solution g = new Solution();
            int ans = g.getMiddle(head);
            System.out.println(ans);
            //printList(head); 
            t--;
        }
    } 
} 
   
// } Driver Code Ends


/* Node of a linked list
 class Node {
   int data;
    Node next;
    Node(int d)  { data = d;  next = null; }
}
*/
class Solution
{
    Vector<Integer> v=new Vector<>();
    int getMiddle(Node head)
    {
        while(head!=null)
        {
            v.add(head.data);
            head=head.next;
        }
        int mid=v.size()/2;
         // Your code here.
         return v.get(mid);
    }
}

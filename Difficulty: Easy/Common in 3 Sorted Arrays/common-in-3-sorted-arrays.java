//{ Driver Code Starts
// Initial Template for Java

import java.util.*;

public class GFG {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int t = Integer.parseInt(sc.nextLine());
        while (t-- > 0) {
            List<Integer> arr = new ArrayList<>();
            List<Integer> brr = new ArrayList<>();
            List<Integer> crr = new ArrayList<>();

            String input1 = sc.nextLine();
            Scanner ss1 = new Scanner(input1);
            while (ss1.hasNextInt()) {
                arr.add(ss1.nextInt());
            }

            String input2 = sc.nextLine();
            Scanner ss2 = new Scanner(input2);
            while (ss2.hasNextInt()) {
                brr.add(ss2.nextInt());
            }

            String input3 = sc.nextLine();
            Scanner ss3 = new Scanner(input3);
            while (ss3.hasNextInt()) {
                crr.add(ss3.nextInt());
            }

            Solution ob = new Solution();
            List<Integer> res = ob.commonElements(arr, brr, crr);

            if (res.size() == 0) System.out.print(-1);
            for (int i = 0; i < res.size(); i++) System.out.print(res.get(i) + " ");
            System.out.println();
        
System.out.println("~");
}
    }
}

// } Driver Code Ends


// User function Template for Java

class Solution {
    // Function to find common elements in three arrays.
    public List<Integer> commonElements(List<Integer> arr1, List<Integer> arr2,
                                        List<Integer> arr3) {
        // Code Here
        List<Integer> li=new ArrayList<>();
        HashMap<Integer,Integer> hm=new HashMap<>();
        
        for(int i:arr1){
         
         if(!hm.containsKey(i))
         {
             hm.put(i,1);
         }
        }
        for(int i:arr2){
         
         if(hm.containsKey(i) && hm.get(i)==1)
         {
             hm.put(i,2);
         }
        }
        for(int i:arr3){
         
         if(hm.containsKey(i) && hm.get(i)==2)
         {
             hm.put(i,3);
         }
        }
        int mx=0;
        hm.forEach((key,value)->
        {
           if(value==3)
           {
               li.add(key);
           }
        });
        
        Collections.sort(li);
        return li;
        
        
    }
}
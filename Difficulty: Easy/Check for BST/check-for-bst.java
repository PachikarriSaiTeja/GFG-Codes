class Solution {
    int prev = Integer.MIN_VALUE;
    boolean isValid = true;
    
    boolean isBST(Node root) {
        check(root);
       return isValid;
        }
       
                                                                                                                                                                                                        
    
    public boolean check(Node root)
    {
        if(root!=null)
        {
            check(root.left);
            
            if(root.data<prev)
            {
                isValid = false;
            }
            prev = root.data;
            check(root.right);
        }
        return true;
    }
    
}
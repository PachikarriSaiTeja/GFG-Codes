/*
class Node{
    int data;
    Node left;
    Node right;
    Node(int data){
        this.data = data;
        left=null;
        right=null;
    }
}

*/
class Solution {
    public boolean isSymmetric(Node root) {
        // Code here
        if(root==null)
        {
            return true;
        }
        return isMirror(root.right,root.left);
        
    }
    public boolean isMirror(Node r1,Node r2){
        if(r1==null && r2==null || r1==null && r2==null){
            return true;
        }
        if(r1==null || r2==null || r1==null || r2==null){
            return false;
        }
        return r1.data==r2.data && isMirror(r1.right,r2.left) && isMirror(r1.left,r2.right);
    }
}
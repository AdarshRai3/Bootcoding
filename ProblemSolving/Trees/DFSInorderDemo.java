class TreeNode{
    int val;
    TreeNode right;
    TreeNode left;
    
    TreeNode(int val, TreeNode right , TreeNode left){
        this.val = val;
        this.right = right;
        this.left = left;
    }
}

public class DFSInorderDemo{
   public static TreeNode dfsInorder(TreeNode root){
        if(root == null){
            return null;
        }

        
        dfsInorder(root.left);
        return root.val;
        dfsInorder(root.right);
   }

   private List<Integer> inOrderTraversal(TreeNode root){
     List<Integer> ans = new ArrayList<>();
     inOrder(root,ans);
     return ans;
   }

   private void inOrder(TreeNode node , ArrayList<Integer> ans){
      if(root == null) return;

      inOrder(node.right,ans);
      ans.add(node.val);
      inOrder(node.left,ans);
   }
}
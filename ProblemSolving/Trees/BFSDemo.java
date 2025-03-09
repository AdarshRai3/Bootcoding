class TreeNode{
    int val;
    TreeNode right;
    TreeNode left;

    TreeNode(int val, TreeNode right ,TreeNode left){
        this.val = val;
        this.right = right;
        this.left = left;
    }
}

public class BFSDemo{
    
    public static void levelOrderTraversal(TreeNode root){
        
        //In case of level order traversal the first thing we need is queue.
        //Basic steps are first we have to put element in the queue , then polling them out on the correct interval
        
        Queue<Integer> q = new LinkedList<>();

        q.add(root);

        while(!q.isEmpty()){
            int levelSize = q.size();

            for(int i=0;i<levelSize;i++){
                TreeNode node = q.poll();
                
                if(root.right!=null) q.add(root.right);
                if(root.left !=null) q.add(root.left);
            }
        }

    }
}
public class ProductOfSum {
    public int maxProduct(int[] nums) {
        int n = nums.length;
        int prod1 = nums[0];
        int prod2 = nums[0];
        int res = nums[0];

        for(int i =1 ; i<n; i++){
     
           int temp = Math.max(nums[i],Math.max(prod1*nums[i],prod2*nums[i]));
           prod2 = Math.min(nums[i],Math.min(prod1*nums[i],prod2*nums[i]));
           prod1 = temp;

           res = Math.max(res,prod1);
           
        }
        return res;
    }
}
//Time complexity = O(n)
//Space complexity = O(1)

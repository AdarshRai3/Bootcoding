public class BSInRotatedSortedArray {
    
    public boolean search(int[] nums, int target){
        int n = nums.length;
        int low = 0;
        int high =0;

        while(low<=high){
            if(nums[mid]==target){
                return true;
            }

            if(nums[high]==nums[mid] && nums[low]==nums[mid]){
                low=low+1;
                high=high-1;
                continue;
            }
            
            if(nums[low]<nums[mid]){
              
                if(nums[])

            }else{

            }
        }
    }
}

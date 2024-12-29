public class BSInRotatedSortedArray {
    
    public boolean search(int[] nums, int target){
      int n = nums.length;
      int low =0;
      int high=n-1;

      while(low<=high){
        int mid = low + ((high-low)>>1);

        if(nums[mid]==target){
            return true;
        }

        if(nums[low]==nums[mid] && nums[high]==nums[mid]){
            low=low+1;
            high=high-1;
            continue;
        }

        if(nums[low]<nums[mid]){
           if(nums[low]<=target && nums[mid]>=target){
                high = mid - 1;
           }else{
                low = mid + 1;
           }
        }else{
           if(nums[mid]<=target && nums[high]>=target){
               low = mid + 1;
           }else{
               high = mid - 1;
           }
        }
      }
         return true;
    }
}
// Input Format:
//  arr = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6], k = 3
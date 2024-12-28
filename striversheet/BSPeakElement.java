public class BSPeakElement {
    public int findPeakElement(int[] nums) {
         
        int n = nums.length;
        
        if(n == 1) return 0;
        if(nums[0]>nums[1]) return 0;
        if(nums[n-2]<nums[n-1]) return n-1;

        while(low<=high){

            int mid = low + ((high-low)>>1);
            
            if(nums[mid-1]< nums[mid] && nums[mid]>nums[mid-1]){
                return mid;
            }
            
            if(nums[mid-1]<nums[mid]){
                low=mid+1;
            }else{
                high=high-1;
            }
        }

        return -1;
    } 
}

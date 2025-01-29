public class Solution1 {
    public int[] twoSum(int[] nums, int target) {
        //Intializing the hashmap where element are the keys and index are the values
        HashMap<Integer,Integer> hm = new HashMap<>();
        
     //Iterae using a for loop
        for(int i=0;i<nums.length;i++){
            
            //find the complement of the nums[i]
            int complement = target - nums[i];

            //Checking if complement exist in the hashmap or not
            if(hm.containsKey(complement)){
                //if exist return the index of the complement 
                return new int[]{hm.get(complement),i};
            }
            //else put the element in the hashmap 
            hm.put(nums[i],i);
        }
        //if complement does not exist then we simply return empty array
        return new int[]{};

        //Time Complexity : O(n)
        //Space Complexity : O(n)   
    }
}
// ---------------------------------------------------------------
// Brute force 
// Using two for loop  and check if check the sum for every combination 
// Time Complexity : O(n^2)
// Space Complexity : O(1)
// for(int i =0;i<n;i++){
//     for(int j=i+1;j<n;j++){
//         if(nums[i]+nums[j]==target){
//             return new int[]{i,j};
//         }
//     }
// }
//             return new int[]{};
// ------------------------------------------------------------
//Better Approach 
//First sort the array.
//Then we two pointer approach for the two sum 
//Since the array is sorted we can use binary search to find the complement.
// for(int i =0;i<n;i++){
    //   int complement = target - nums[i];
    //   int low =i+1;
    //   int high = n-1;
    //   while(low<=high){
    //     int mid = low + (high-low)/2;
    //     if(nums[mid]==complemenet){
    //         return new int[]{i,mid};
    //     }else if(nums[mid]>complement){
    //         high = mid-1;
    //     }
    //     else{
    //         low = mid+1;
    //     }
    //   }
    //   return new int[]{};
    // 
    // -------------------------------------------------------

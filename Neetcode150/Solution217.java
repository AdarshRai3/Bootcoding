public class Solution217 {
    public boolean contansDuplicates(int[] nums){
        //Create HashSet for the array element
        HashSet<Integer> isSeen = new HashSet<>();

        //Iterate over the array
        for(int i =0;i<n;i++){
            //check the element already exit in the set
            if(isSeen.contains(nums[i])){
                //if it does return true 
                return true;
            }
            //if not then add the nums element in the array
            isSeen.add(nums[i]);
        }
           //After the iteration if we dont find the element retrn false 
            return false;
    }
    
}

// Notes: Contains Duplicates :
// Brute force Approach : 
// for(int i =0;i<n;i++){
//     for(int j=i;j<n;j++){
//        if(nums[i]==nums[j]){
//          return true;
//        }
//     }
// }
// return false;
// Basically we iterate on the all the loop using 2 for loop due to which it has time complexity of O(n^2) and the space complexity of O(n);
// --------------------------------------------------------------
// Better Approach
// In this approach what we do is we first sort the array and then after first sort what we do check the adjacent elemenet of the element during the first interation and which led to solve the problem:
// Arrays.sort(nums[i]);
// for(int i=0;i<n-1;i++){
//     if(nums[i]==nums[i+1]){
//         return true;
//     }
//     return false;
// // }
// Time Complexity=O(Nlog(N))  --------------------------------------------------------------
//Optimise Approach
// In this approach what we do is we used hashset we know that in we have to put unique element in the array for that we used hashSet.

// HashSet<Integer> isSeen = new HashSet<>();
// for(int i=0;i<n;i++){
//     if(isSeen.contains(nums[i])){
//         return true;
//     }
//        isSeen.add(nums[i]);
// }
//  return false;
//  Time Complexity = O(n);
//  Space Complexity = O(n); for the hashset
// ------------------------------------------------------------
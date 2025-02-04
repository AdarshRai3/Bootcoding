public class Solution238 {
    public int[] productExceptSelf(int[] nums) {
      int n = nums.length;
      //we need post and pre variable to store the product of the left and right side of the element except itself;
      //We have to intialise it with one.
      int post = 1;
      int pre = 1;

      //Now we have result array to store the result of the products of the left and right side
      int [] result = new int [n];

      //First we will iterate over the array from the left side and get all the pre results in the result array.
      for(int i =0;i<n;i++){
        result = pre;
        pre = pre * nums[i];
      }
      
      //Then we will iterate over the array from the right side and get all the post results in the result array
      for(int i =n-1;i>=0;i--){
        //Here we have to multiply the pre results with the post results
        result[i] = post * result[i];
        post = post * nums[i];
      }
       
      //Now we will return the result array
      return result;
   }
}
// -------------------------------------------------------------
// Brute force approach is the take the two nested for loops 
// for(int i = 0 ; i<nums.length;i++){
//      int res = 1;
//    for(int j=i+1 ; j<nums.length;j++){
//        res = res * nums[j];
//    }
//    for(int j=i-1;j>=0;j--){
//        res = res * nums[j];
//    } 
//    result[i] = res;   
// } 

// Time Complexity : O(N^2)
// Space Complexity : O(N)
// -------------------------------------------------------------------------------
// Better approach
//In this approach we will you use two arrays to store the products one is pre[] and other is post[]
//First we will iterate over the array from the left side and get all the pre results in the pre array.
//then we will iterate over the array from the right side and get all the post results in the post array
//then we multiply both the arrays values on the same index to get the answer array
// --------------------------------------------------------------------------------
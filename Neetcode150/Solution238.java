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

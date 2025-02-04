public class Solution11 {
    
    class Solution {
        public int maxArea(int[] height) {
            //first we handle the base case 
            if(height.length == 0){
                return 0;
            }
            
            //then we low and high pointer where low starts from 0 and high = height.length -1
            int low = 0;
            int high= height.length-1;
            //Max Area varaiable is intialised with 0;
            int maxArea = 0;
    
            //iterate with condition where low < high 
            while(low<high){
              
               //we know we can calculate the widht = high - low formala 
                int width = high - low;
                //for height we need to find lower height among to comparing indexes 
                int length = height[low]>height[high]?height[high]:height[low];
                // we know the formula for area is width * length
                int area = width * length;
    
                //compare to get the max value of the area 
                maxArea = Math.max(maxArea, area);
                
                //to get greater area we need height if height[low]>height[high] we do high-- to find greater height by moving left and otherwise we will move right by moving low++ to find greater height 
                if(height[low]>height[high]){
                    high--;
                }
                else{
                    low++;
                }
    
            } 
    
            //In the end of the loop we simply return the maxArea value 
            return maxArea;
            
        }
    }
}
// ------------------------------------------------------------------------------
//Time Complexity : O(N)
//Space Complexity : O(1)
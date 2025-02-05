
// This is most optimal approach : Two pointer approach
public class Solution42 {
    public int trap(int[] height) {
        int n = height.length;
        //In this we are solving for the edge case 
        if(n == 0){
            return 0;
        }
         //We intialise two pointer low and high since we see a patten in the point of infliction at index 8 , till index 8, high>low but after pointer low>high , based on this we can apply two pointers here low = 0 and high = n-1
          int low = 0;
          int high = n-1;

          //lowMax is intialised by height[low]
          int lowMax = height[low];

          //highMax is intialised by height[high]
          int highMax=height[high];

          //total capacity is what we want to calculate 
          int total = 0;
        
        //now we start iteration low<=high using while loop 
        while(low<=high){
            //now we take advantage of infliction point at index 8 and check this will decrease unnecessary comparision, now highMax>lowMax 
            if(highMax>lowMax){
              // highMax > lowMax that means all the comparision we are doing here is from index 0 to 8 
              //Now we need to find the lowMax value;
               lowMax = Math.max(lowMax, height[low]);

               //we observe that from the pic that for the value to hold any capicity lowMax>height[low]
               if(lowMax - height[low]>0){

                //if we find any instances where lowMax > height[low] we just need to add that to total 
                 total = total + (lowMax - height[low]);
               }
               //Now we have to move the low++ pointer forward 
               low++;
            }

            //Similary for the case when lowMax> highMax that means now we have compare index from 8 to n-1;
            else{
                //find the highMax 
                highMax = Math.max(highMax, height[high]);

                //for the value to hold any capicity we know that highMax>height[high]
                if(highMax - height[high]>0){

                    //if highMax>height(high) then we similary add that to total 
                    total = total + (highMax - height[high]);
                }
                //now we have move high-- pointer backwards 
                high--;
            }
        }
        //as the loop end we just have to return total capicity
        return total;

    }
}
//Time Complexity : O(N)
//Space Complexity : O(1)

// ---------------------------------------------------------------------
// //This is better approach 
// public class Solution42 {
//     public int trap(int[] height) {

//         int n = height.length;

//         // first we are going to manage the edge case
//         if (n == 0) {
//             return 0;
//         }

//         // First we create low aray which will traverse from low end
//         int[] low = new int[n];
//         int k = 0;
//         // Now we traverse from the left and only put those element which are greater in
//         // the low array
//         for (int i = 0; i < n; i++) {
//             k = Math.max(k, height[i]);
//             low[i] = k;
//         }

//         // Now we again create the high array and put the element inside it which are
//         // greater as we traverse from the high end
//         int m = 0;
//         int[] high = new int[n];

//         // now we raverse from the high end and only put the value which are greater
//         for (int j = n - 1; j >= 0; j--) {
//             m = Math.max(m, height[j]);
//             high[j] = m;
//         }
//         // After we have both high array and low array now we can traverse using a
//         // equation that we made that is Math.min(high[i],low[i])-height
//         int ans = 0;
//         for (int i = 0; i < n; i++) {
//             // Now if iterate through the array using this equation we have to add to the
//             // ans
//             ans += Math.min(low[i], high[i]) - height[i];
//         }
//         // After the end of the loop we can finally return the answer
//         return ans;
//     }
// }

//Time Complexity : O(3N)->O(N)
//Space Complexity : O(2N)-> O(N) since we require high and low array to store data
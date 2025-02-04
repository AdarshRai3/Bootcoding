import java.util.HashSet;

public class Solution128 {
      public int longestConsecutive(int[] nums) {
        //First we need to take care of the edge case if the nums array is empty in that case the longest subsequence will be 0;
        if(nums.length == 0){
            return 0;
        }

        //Now we now when we need to prevent/detect duplication we use HashSet   
         HashSet<Integer> numSet = new HashSet<>();
       
         for(int num : nums){
            numSet.add(num);
         }

          //Now we need a variable to store the longest Sub which is intialise with 0;
          int maxSeq = 0;
         
        //Now we add all the elements from the array to numSet to filter out the duplicates 
        for(int num : numSet){
            //we only start counting and reinitailising value if numSet does not contains any nums for which num-1 is already present in the hashSet 
            if(!(numSet.contains(num-1))){
                      //Now we will iterate throught the numSet while initialising the currSeq = 1 and currNum = num
                int currSeq = 1;
                int currNum = num;
                while(numSet.contains(currNum + 1)){
              
                  currSeq++;
                  currNum++;
                }
                //After this we will choose the max of maxSeq and currSeq 
                maxSeq = Math.max(maxSeq,currSeq);
            }
        }
        //return the max value of maxSeq
               return maxSeq;

    }
}
// ----------------------------------------------------------------------------
//Time Complexity : O(N)
//Space Complexity : O(N) - > For HashSet
// ------------------------------------------------------------------------------
// Better Approach : First we will sort the given array and then iterate through it to find the largest seq with help of condition (num[i+1]-num[i]==1) amd two variable maxSeq and currSeq to store the largest seq and current seq.
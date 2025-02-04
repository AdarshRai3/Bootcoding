import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution15 {
    public List<List<Integer>> threeSum(int[] nums) {
        // savs the length of the array in the variable
        int n = nums.length;
        // Declare the list<list<Integer>> to store the answer
        List<List<Integer>> result = new ArrayList<>();
        // solving for the edge case
        if (n == 0) {
            return null;
        }
        // Sort the given array
        Arrays.sort(nums);

        // Now we will iterate through the array
        for (int i = 0; i < n; i++) {
            // to avoid duplicates if we find any adjacent value equal we will simple skip
            // that value;
            if (i == 0 || nums[i] != nums[i - 1]) {
                // this is modularized method to solve this problem
                twoSum2(nums, i, result);
            }
        }
        return result;
    }

    public void twoSum2(int[] nums, int i, List<List<Integer>> ans) {

        // We know that the array we have is sorted there we use two pointer here low
        // which start from i+1 and high which start from the end of the array
        int low = i + 1;
        int high = nums.length - 1;

        // now we start traversing the nums array until we reach the end
        while (low < high) {

            // first we save the sum in the variable
            int sum = nums[low] + nums[high] + nums[i];

            // if the sum is high we need to move high--
            if (sum > 0) {
                high--;
            }
            // if the sum is low we need to move low++
            else if (sum < 0) {
                low++;
            }
            // if the sum is excalty equals to 0 , then we need to save the triplets in our
            // arrays and save that arrray in our answer list
            else {
                ans.add(Arrays.asList(nums[i], nums[low++], nums[high--]));

                // after adding that to answer list we need to move our low and high until
                // low<high and nums[low]==nums[low-1]
                while (low < high && nums[low] == nums[low - 1]) {
                    ++low;
                }
            }
        }
    }
}

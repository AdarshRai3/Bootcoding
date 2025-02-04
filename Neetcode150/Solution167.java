
public class Solution167 {

    public int[] twoSum(int[] numbers, int target) {

        // first we handle the edge case where the array is empty
        if (numbers.length == 0) {
            return null;
        }
        // Since we know the array is sorted we can use two pointer approach 
        //where one pointer starts from the end and other starts from the beginning
        int low = 0;
        int high = numbers.length - 1;
        
        // now our while loop will until low < high 
        while (low < high) {
            //if the sum of low + high > target -> high--
            if (numbers[low] + numbers[high] > target) {
                high--;
            } 
            
            //if the sum of low + high < target -> low++
            else if (numbers[low] + numbers[high] < target) {
                low++;
            } 
            //if the sum of low + high == target -> return the index in the array
            else {
                return new int[] { low + 1, high + 1 };
            }
        }
        // if iterate through the whole still not able to find the array then just return null
        return null;

    }

}
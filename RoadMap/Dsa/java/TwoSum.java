import java.utils.*;

public class TwoSum{
    private twoSumfunc(int[] nums, int target){
       HashMap<Integer,Integer> map = new HashMap<>();
       
       for(int i = 0;i<nums.length;i++){
          int complement = target-nums[i];
          if(map.containsKey(compement)){
            return new int[]{map.get(complement),i};
          }
          map.put(nums[i],i);
       }
       
       return new int[]{};
    }
}
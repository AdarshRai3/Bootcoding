import java.utils.*;

public class ContainsDuplicate {
    private static boolean containsDuplicate(int[] nums){
        HashSet<Integer> set = new HashSet<>(); 
        
        for(int i=0;i<nums.length;i++){
            if(set.contains(nums[i])){
                return true
            }

            set.add(num[i])
        }

        return false
    }
}

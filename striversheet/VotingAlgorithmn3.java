import java.util.List;

public class VotingAlgorithmn3 {
    public List<Integer> majorityElement(int[] nums) {
        //Moore's Voting Algorithm

        int cnt1 = 0;
        int cnt2 = 0;
        int e1 = Integer.MIN_VALUE;
        int e2 = Integer.MIN_VALUE;

        for(int i =0;i<nums.length;i++){
            // Find the max two numbers
            if(cnt2==0 && nums[i]!=e1)
            {
                cnt2=1;
                e2 = nums[i];
            }
            else if(cnt1==0 && nums[i]!=e2){
                cnt1=1;
                e2=nums[i];
            }else if(e1 == nums[i]){
                cnt1++;
            }else if(e2 == nums[i]){
                cnt2++;
            }
        
            
        }//O(n)

         int min = (int)(n/3+1);
         cnt1 = 0; cnt2 = 0;
         
         for(int i =0; i<nums.length;i++){
            
             if(nums[i]==e1){
                cnt1++;
             }
             if(nums[i]==e2){
                cnt1++;
             }
         }//O(n)

        List<Integer> ans = new ArrayList<>(); 
        if(cnt1>=min){
            ans.add(e1);
        }
        if(cnt2>=min){
            ans.add(e2);
        }
        return ans;
    }
}
//Time Complexity = O(n)+O(n)=2O(n)
//Space Complexity =O(1)

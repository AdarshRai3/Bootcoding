
public class DutchNationalAlgorithm {

    public void swap(int[] nums , int j , int i){
        if(i!=j){
            nums[i]=nums[i]^nums[j];
            nums[j]=nums[i]^nums[j];
            nums[i]=nums[i]^nums[j];
        }
    }
    public void sortColors(int[] nums) {
       int n = nums.length;
       int low = 0;
       int mid = 0;
       int high = n-1;
       while(mid<high){
        if(nums[mid]==0){
            swap(nums,low,mid);
            low++;
            mid++;
        }else if(nums[mid]==1){
            mid++;
        }else{
            swap(nums,mid,high);
            high--;
        }
       }

    }
}
// time complexity is O(n)
// space complexity is O(1)
//This is dutch national flag , here we using three pointers since we have only three types of element in the array,
// this is the algorithm we are using 
// First we start low = 0, mid =0 and high= nums.length-1;
// now we are creating a swap method to swap the element of the array
// swap(nums , j , i){
//     if(i!=j){
//         nums[i]=nums[i]^nums[j];
//         nums[j]=nums[i]^nums[j];
//         nums[i]=nums[i]^nums[j];
//     }
// }
// now we using three point we start with a while loop mid < high  
// in that we are adding the condition where if nums[mid] == 0 then swap(low,mid) and low++, mid++, if nums[mid] == 1 then mid++, if nums[mid] == 2 then swap(mid , high) and high--;
// ---------------------------------------------------------

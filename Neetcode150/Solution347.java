import java.util.HashMap;
import java.util.PriorityQueue;
import java.util.Queue;

public class Solution347 {
      public int[] topKFrequent(int[] nums, int k) {

        // Handle the edge case K == nums.length
        if(nums.length == k){
            return nums;
        }

        //Create a hashMap to store the elements of the array as key and the frequecy of their occurences inside the array as values
         HashMap<Integer,Integer>count = new HashMap<>();

         //Iterate over the array and put the values as key in the hashMap as key and the frequecy of their occurences inside the array as values
         for(int n:nums){
            count.put(n, count.getOrDefault(n,0)+1);
         }

         //Now after putting the values in the hashMap we will use the PQ and inside that PQ we will the logic of comparision between two element for that we use lambda expression 
         Queue<Integer> heap = new PriorityQueue<>(
             (a,b)-> count.get(a)-count.get(b)
         );

         //Now we will iterate over the keys of the hashMap and put them in the PQ
         for(int n : count.keySet() ){
            heap.add(n);

            //If the size exceeds the K than we will remove the element from the PQ
            if(heap.size()>k){
                heap.poll();
            }
         }
           //Now we put these element in the answer array of size k
           int ans [] = new int[k];
           for(int i =0;i<k;i++){
            ans[i]=heap.poll();
           }
           return ans;
    }
}
// ---------------------------------------------------------
// Solution 1 
// Steps of solving this problems : 
// 1.To use a hashmap where we will store the elements of the array as key and the frequecy of their occurences inside the array as values.
// 2.After than we will iterate over the keys of the hashmap and put them in the SortedArray and than pt the first K elements from this SortedArray into our answer array.
//Time complexity of this approach is O(nlog(n)) and space complexity is O(n)
// ---------------------------------------------------------------------
// But eventually we know their is far better approach to solve this problem using HashMap + PQ(heap) 
// Steps of Solving this problem:
// 1> Use a HashMap and store the elements of nums array in inside that hashmap as key and value will be number of occureneces of that particular element in the nums array.
//Then we use priority queue to store the ke of thyse hashmap by comparing them on their key values and then we put them in the ans array 
//Time Complexity of this approach is O(nlog(k)) and space complexity is O(n)
// Here that K is the Kth largest elements
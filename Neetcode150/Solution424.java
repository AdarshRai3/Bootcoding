public class Solution424 {
    public int characterReplacement(String s, int k) {

        //Basicaly we have to check what the question is demanding from us, s="ABAB" K is how many operation we can perform such that we can replace the character to get the longest string 
         
         //first we get array of occurence  to check how many time a character occured in an array 
         int[] occurence = new int[26];
         //Now we will solve it using two pointer approach for that we will need a low pointer and high pointer, low pointer will start from 0 and high pointer will start from 0
         int low = 0;
         int high = 0;
         //we put the max occcurence as 0 
         int maxOccurence = 0;

         //Answer length is also 0 
         int ans =0;
        
        //Now we start our high pointer start iterating on the string 
        for(high = 0 ; high<s.length() ; high++){

            //low we will check the max occrence of any character 
            maxOccurence = Math.max(maxOccurence, ++occurence[s.charAt(high)-'A']);
            //Now if we have high - low + 1 - maxOccurence > replacement operation 
            if(high - low + 1 - maxOccurence > k){
                
                //that means String has more multiple character that means how we have to reduce our occurence character at low -- to decrease its count in the array 
                occurence[s.charAt(low)-'A']--; 
                //low we move the low pointer ahead 
                low++;
            }

         //now if high-low+1-maxOccurence<K that means we can create a long string by performing k operation that means ans = Math.max(ans, high-low+1) for every iteration of loop 
            ans = Math.max(ans,high-low+1);
        }
        //As the loop end we finally return the answer 
        return ans;
    }
    
}
//Time Complexity : O(N)
//Space Complexity : O(1) has we using just array of fixed length.

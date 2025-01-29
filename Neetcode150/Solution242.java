public class Solution242 {
  public boolean validAnagram(String s , String t){
     s.toLowerCase();
     t.toLowerCase();
     if(s.length() != t.length()){
         return false;
     }
     int charCount[] = new int[26];
     for(int i=0;i<s.length;i++){
       charCount[s.charAt(i)-'a']++;
       charCount[t.charAt(i)-'a']--;
     }
     for(int count:charCount){
        return false;
     }
        return true;
  }   
}
// -----------------------------------------------------------
//BruteForce Approach 
//basically in this we are using two for loop and check if the string has same charaters or not 
//  for(int i = 0; i<s.length();i++){
//     int flag =0;
//      char c = s.charAt(i);
//     for(int j=0;i<t.length();j++){
//         if(t.charAt(i)==c){
//           flag =1;
//           break;
//         }
//     }
//         if(flag==0){
//             return false;
//         }
//  }
//  return true;
// ------------------------------------------------------------
//In the optimised approach we have two choice we can use hashmaps and count array in this case I have choose count array to solve this prooblem . These are the steps  :
// 1> First we check both strings(s,t) are of same length or not 
// 2> After that we convert s and t into lowercase using toLowerCase() method
// 3>After that we create a count array of fixed length 26 and initialize it with 0;
// 4>Now we iterate over both the string and since both  string is of same length we can 1 use for loop to iterate during iteration we increase the count of the character for s and decrease the count of the character for t.
// 5>After we again run a for loop to  check whether all the count is zero or not if it is zero then return true else return false 
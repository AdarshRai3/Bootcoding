class Solution567 {
    public boolean checkInclusion(String s1, String s2) {
      //First we will solve for the edge case that if we have s1.length() > s2.length() , then we return false 
      s1.toLowerCase();
      s2.toLowerCase();
      if(s1.length()>s2.length()){
        return false;
      }
       
      //s1 is array of string s1 and s2 is first window of  string s2
      int [] s1Map = new int[26];
      int [] s2Map = new int[26];
      
      //Now we need to intialise the map for s1 and first window of s2 and add for s1Map and s2Map 
      for(int i = 0 ; i<s1.length();i++){
        s1Map[s1.charAt(i)-'a']++;
        s2Map[s2.charAt(i)-'a']++;
      }

      //Now after adding the number of char in both s1Map for string s1 and first sliding window of s2 in s2Map we if start checking in both s1Map and s2Map by traversing the index if at any point we find out that our array dont match we will return false 
      for(int i = 0; i<s2.length()-s1.length(); i++){
        //checker method which checks both Maps
        if(checker(s1Map,s2Map)){
            return true;
        }
        // if we find our present window is not equals to s1Map of string s1 then we shift the window by moving window by s2.charAt(i+s1.length)
        s2Map[s2.charAt(i+s1.length)-'a']++;
        //this will empty the value that was already stored in s2Map
        s2Map[s2.charAt(i)-'a']--;
      }
          //now after completing the loop we will again check for s1Map and s2Map , that means s2 string contain s1 character
          return checker(s1Map,s2Map);
    }

    //This function will help us to travese through the array and check the count
    private boolean checker( int[] s1Map , int[] s2Map){
        for(int i = 0;i<26;i++){
            if(s1Map[i] != s2Map[i]){
                return false;
            }
            
        }
        return true;
    }
}
//Optimal Solution
//So the optimal solution is to use sliding window approach with hashmap to check the patten of string  s1 in string s2 by traversing using a window 
//Time complexity : O(N)
//Space Complexity : O(1) Since there finite character 26 in english alphabet so in no time we will store more than 26 character in the map/array
// --------------------------------------------------------------
//Brute Force Solution : So in the brute force we will generate all the permutation of the substring and then check if it is present in the second string or not using contains method 
//Time Complexity: O(N!)(Creating all the permutation) + O(N!)(For checking for all permutation that are can be present in the substring) 
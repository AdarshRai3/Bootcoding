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
      
      //Now we need to intialise the map for s1 and first window of s2 and add 
      for(int i = 0 ; i<s1.length();i++){
        s1Map[s1.charAt(i)-'a']++;
        s2Map[s2.charAt(i)-'a']++;
      }

      for(int i = 0; i<s2.length()-s1.length(); i++){
        if(checker(s1Map,s2Map)){
            return true;
        }
        s2Map[s2.charAt(i+s1.length)-'a']++;
        s2Map[s2.charAt(i)-'a']--;
      }
          return checker(s1Map,s2Map);
    }

    //This function will help us to travese through the array and check the count
    public boolean checker( int[] s1Map , int[] s2Map){
        for(int i = 0;i<26;i++){
            if(s1Map[i] != s2Map[i]){
                return false;
            }
            return true;
        }
    }
}
//Optimal Solution
//So the optimal solution is to use sliding window approach with hashmap to check the patten of string  s1 in string s2 by traversing using a window 
//Time complexity : O(N)
//Space Complexity : O(1) Since there finite character 26 in english alphabet so in no time we will store more than 26 character in the map/array
// --------------------------------------------------------------
//Brute Force Solution : So in the brute force we will generate all the permutation of the substring and then check if it is present in the second string or not using contains method 
//Time Complexity: O(N!)(Creating all the permutation) + O(N!)(For checking for all permutation that are can be present in the substring) 
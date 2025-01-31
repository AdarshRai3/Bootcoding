import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

public class Solution49 {
     public List<List<String>> groupAnagrams(String[] strs) {
        //THis is for the edge case when the strs array is empty
        if(strs.length == 0){
            return new ArrayList();
        }

        //We declare a hashmap with HashString as key and list as value
        HashMap<String,List> hm = new HashMap<>();

        //we need a 26 size array to store the count of each character of the string 
        int [] countArray = new int[26];

        //Now we run a for loop for each string in a array 
        for(String s : strs){
             
            s.toLowerCase();
            //For each new string s we need to reset the countArray values as 0.
            Arrays.fill(countArray,0);

            //for each character in the String we need to increase the countArray index by +1 but we are storing count of each character in the countArray
            for(char c : s.toCharArray()){
                countArray[c-'a']++;
            }
            
            //sb is used for the StringBuilder, since String is immutable in java
            StringBuilder sb = new StringBuilder();

            //Now for each string we need to generate a hashcode by using the countArray of that string
            for(int i =0;i<26;i++){

                //this is language requirement for the hashcode
                sb.append("#");
                sb.append(countArray[i]);
            }

            //Now we convert sb.toString() into String and store it in the key
            String key = sb.toString();

            //Now we check out hashMap if the key exist or not in the hashMap if doesnot we put the key and hashMap and generate the new ArrayList.
            if(!hm.containsKey(key)){
                hm.put(key, new ArrayList());
            }
            //Add the key in the ArrayList of the HashMap
                hm.get(key).add(s);
        }
          //Add the value of the HashMap in the answer of the ArrayList and return the ArrayList
          return new ArrayList(hm.values());
    }
}
// brute force approach
// In this solution there are steps we used to solve this problem
//1. First we will taken another array of same length as strs and take the string from each index of the str array and then sort string in alphabetical order and store it in the new array 
//2. Then compare the strings in the new array and index of string having same string need to be used to select the string from the str array and then add it to the answer list 
// {

//    int n =strs.length;
//     Strng [] ans = new String[n]; 
//    for(int i = 0;i<strs.length;i++){
//     char[] charArray = strs[i].toCharArray();
//     Arrays.sort(charArray);
//     String sortedString = new String(charArray);
//     ans[i]=sortedString;
//    }
   
//    HashMap<String,List<Integer>ls> hm = new HashMap<>();
//    for(int i=0;i<ans.length;i++){
//        if(hm.containsKey(ans[i])){
//             hm.put(ans[i],ls.add(strs[i]));
//        }
//          hm.put(ans[i],ls.add(strs[i]));
//    }
   
//    return new ArrayList<>(hm.values());

// }
// ------------------------------------------------------------
//Optimised Appraoch in this appraoch we are using the concept of indexing and hashing to solve this problem
//These are the steps : 
//1.first we check for the edge case if the string is empty or not if the string is empty them we have to return empty arraylist
//2.Now we first declare a hashmaps with String as key and List as value
//3.Then we start our first loop in the string for this we use for each loop for(String s : strs){}
//4.Arrays.fill(countArray,0); this will fill the countArray with 0
// 5.After filling it with 0 we will not run a for loop and we will run a for each loop for(char c : s.toCharArray()){}
//6.In this we will increment the countArray index by 1 for each character of the string 
//7.After that we will create a StringBuilder sb = new StringBuilder(); 
//8.Again we run a for loop on the countArray for this we wil run a for loop on the countArray length and we will add the countArray index to the StringBuilder sb
//9. After that we will create a String key = sb.toString();
//10 Now we will check if the key already exist in the hashmap or not if it does then we will add the string to the list else we will create a new list and add the string to the list
//11.After that we will add the list to the hashmap with the key
//12.After that we will return the value of the hashmap
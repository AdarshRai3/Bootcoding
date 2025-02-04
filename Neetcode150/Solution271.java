public class Solution271 {
    public String encode(List<String> strs) {
        //Edge case if the string is empty then we insert character at 258 index since according to question character from 0-256 are already booked for messages
          if(strs.size() == 0){
            return Character.toString((char)258);
          }

          //Now we create a string builder to store the strings from strs list 
          StringBuilder sb = new StringBuilder();
          //To encode we will use the character 257 between each string
          String seperator = Character.toString((char)257);

          //Now we will run a for each loop for each string in strs
          for(String s : strs){

            //Now we will append the string to the string builder with a seperator in the end.
            sb.append(s);
            sb.append(seperator);
          }

          //In the case of last string we will just remove the seperator from the end
          sb.deleteCharAt(sb.length() - 1);

          //Now after that we will return the sb as a string
          return sb.toString();
    }
    
    public List<String> decode(String str) {
        //Now in the decoding process we will first check for the edge case if the string is empty then we will return an empty arraylist
        if(str.equals(Character.toString((char)258))){
            return new ArrayList<String>();
        }
        
        //Now we have reintialise seperator with the same character that we used in encoding so we can decode the string 
        String seperator = Character.toString((char)257);
        
        //Now we can use the seperator with string str with split method to decode the str string into a list 
        return Arrays.asList(str.split(seperator,-1));
    
    }
    
}

// TimeComplexity = O(N);
// SpaceComplexity = O(N);
// --------------------------------------------------------------------
public class Solution125 {
    public boolean isPalindrome(String s) {

        //First we need to take care of edage case when the string is empty and an empty string is a palandrome so the answer for that is true.
        if(s.length() == 0){
            return true;
        }
        //Now we use two variables as pointer low and high we high starts from end of the string and low starts from the start of the string 
          int low = 0;
          int high = s.length()-1;
        
        //Now we run a while loop until low < high 
        while(low < high)
        {
            //now while we find any other character that is non-alphanumeric we ignore it and move the pointer towards the middle by low++;
            while(low<high && (!Character.isLetterOrDigit(s.charAt(low)))){
                low++;
            }
           //while the character is not alphanumeric for high also we do the same thing but move the pointer high--
            while(low<high && (!Character.isLetterOrDigit(s.charAt(high)))){
                high--;
            }

            //if the the character is alphanumerica we first convert it to lower case and then compare with high and low if they are not same we return false
           if(Character.toLowerCase(s.charAt(low))!= Character.toLowerCase(s.charAt(high))){
            return false;
           }

           //now we move the pointers towards the middle low++ and high--
           low++;
           high--;
        }
        //if the loop get completed then we return true.
        return true;
    }
}
// ------------------------------------------------------------------------\
//Time Complexity : O(N)
//Space Complexity : O(1);
// ----------------------------------------------------------------------------
// Better Approach
// we just take s and filter it for alphanumeric characters and put this result in one string s1 and then put the other result in s2 which is reverse of s1 and after that we just compare s1 and s2 and if both s1 and s2 are equal then we return true else we return false.
// Time Complexity : O(n)
// Space Complexity : O(2n)
// -------------------------------------------------------------------------
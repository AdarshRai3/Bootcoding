import java.util.HashSet;

public class Solution3 {
    public int lengthOfLongestSubstring(String s) {
        // First we need to take care of the edge cases
        if (s.length() == 0 || s == null) {
            return 0;
        }
        if (s.length() == 1) {
            return 1;
        }

        // Now we need maxLen variable to store value;
        int maxLen = 0;

        // Now we have low pointer and high pointer for two pointer approach
        int low = 0;
        int high = 0;
        // HashSet to prevent duplication and add unique character
        HashSet<Character> visited = new HashSet<>();

        // now we will start iterating using high on the string until we reach the end
        while (high < s.length()) {
            // First we will check s.charAt(high) exist in the string or not
            char c = s.charAt(high);
            // we have to use while loop instead of if because there can sequence of
            // duplicate character in test case and check whether the s.charAt(high) exist
            // on the array or not if it does
            while (visited.contains(c)) {
                // first we remove that character from the visited hashset
                visited.remove(s.charAt(low));
                // move low pointer ahead
                low++;
            }
            // if not then we simply add the character c in the visited hashset
            visited.add(c);
            // Now we check and update the max length
            maxLen = Math.max(maxLen, high - low + 1);
            // move the high pointer ahead
            high++;
        }
        // returning the length maxLen
        return maxLen;

    }
}

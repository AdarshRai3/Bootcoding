import java.util.*;
class isAnagram{
    public boolean isAnagramFun(String s , String t){
        if(s.length() != t.length()){
            return false
        }

        int[] hash = new int[26];
        int n = s.length();
        Arrays.fill(hash,0);
        
        for(int i =0;i<n;i++){
            hash[s.charAt[i]-'a']+=1;
            hash[s.charAt[i]-'a']-=1;
        }

        for(int i=0;i<26;i++){
            if(hash[i]!=0){
                return false
            }
        }

        return true;
    }

    public static void main(String[] args){
        System.out.println("This is solved");
    }
}
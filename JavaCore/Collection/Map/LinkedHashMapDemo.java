import java.util.*;

public class LinkedHashMapDemo {
    public static void main(String[] args) {
        // LinkedHashMap: Insertion order will be preserved
        LinkedHashMap<Integer, String> lhs = new LinkedHashMap<>(16, 0.76f, true);

        //There are 3 parameters of LinkedHashMap
        //Intial Capicity
        //Load Factor: how much intial capicity has to be filled before size will double
        //Access Order : The default value is false that means insertion order will be preserved and if it is true then access order will be preserved in access order least recently order will be removed first.
        //Used in LRU Cache 
        //Linked Hash Map is not Thread Safe not it is synchronized

        lhs.put(1, "Ram");
        lhs.put(2, "Laxman");
        lhs.put(3, "Hari");
        for (Map.Entry<Integer, String> e : lhs.entrySet()) {
            System.out.println(e.getKey() + ":" + e.getValue());
        }

        // Now on running this we can clearly see we have recently get the key 2 therefore it will go to the last 
        lhs.get(2);
        for(Map.Entry<Integer, String> e : lhs.entrySet()){
            System.out.println(e.getKey() + ":" + e.getValue());
        }

    }
}
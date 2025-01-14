import java.util.*;
public class hashMaps{
    public static void main(String[] args) {
        
        // HashMaps
        HashMap<Integer,String> map = new HashMap<>();
        map.put(1,"Adarsh");
        map.put(2,"Raj");
        map.put(3,"Rajiv");
        map.put(4,"Rama");
        System.out.println(map.toString());
        
        // System.out.println(map.get(2));
        // System.out.println(map.containsKey(3));
        // System.out.println(map.containsValue("Rama"));
        // Set<Integer> keys = map.keySet();
        // for(int i : keys){
        //     System.out.println(i);
        // }
        // map.remove(4);
        // System.out.println(map);
        // System.out.println(map.size());
        for(int i : map.keySet()){
            System.out.println(i+"*"+map.get(i));
        }
        for(Map.Entry<Integer,String> i : map.entrySet()){
            System.out.println(i.setValue(i.getValue().toUpperCase()));
            System.out.println(i);
        }
    }
}
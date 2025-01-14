import java.util.*;
public class hashMaps{
  
    public static void main(String[] args) {
        //Maps
        //Maps Has Key-Value Pair
        //Keys must be unique but Values can be duplicated 
        //One value per Key
        //Order
        // HashMap : No order
        // TreeMap : Sorted order
        // LinkedHashMap : Insertion(Natural) order
        // HashMaps
        //Allow Null key but only once 
        //Not Synchronized , Not Thread Safe
        //O(1) time for get() AND put() method depending hash function dispease on the element properly
        //There are 4 basic components of a hashMap
        //1.Key : The unique identity used to retrieve the value
        //2.Value : The value associated with the key
        //3. Bucket:The intenal list that stores key value pairs 
        //4.Hash Function : Converts a key into an index (bucket location) for storage.
        //The primary purpose of a hash function to give a code of a key in a fixed size value irresepective of the key size.
        //Key featurs of Hashcode:
        //Deterministic : The same input will produce a same output.
        //Fixed Size Output: Regardless of the input size, the output will be of fixed size of 32-64 bits.
        //Effecient Computation: The hash function is efficient to compute the hash code.

        //How data is stored inside a hashMap?
        //Steps
        //1.Hashing the key
        // The value of the key is passed to the hash function which will generate a unique value for the key which will help help us determine the location of the key in the bucket.
        //2.Calculating the index 
        // int index = hashCode % arraySize;
        //3.Storing the key value pair in the bucket

        //How we retrive data from the hashMap?
        //Steps
        //1.Hashing the key 
        //2.Finding the index
        //3.Searching the bucket

        //Why Searching in the bucket?
        //In case of a hashcode which is finite set that we can have collision in the bucket when two input creates a same output.

        //How we handle the collision?
        //Bucket in the hashMaps are kind of Arrays which have linked list attached to it to prevent collison 
        //For example if two arrayList have the same hashcode then we can put them in the same bucket with the help of linked list attached to it.
        //But the problem with linked list is that the search operation take O(n) time where n is the number of elements in the linked list.
        //To reduce this chainging problem we can convert the linked list into a balanced binary tree which has search operation of O(log n)time if the linked list size cross the threashold of 8.

        //Rehasing of HashMap
        //The default capicity of the hashMap bucket is 16 and the default load factor is 0.75 that means when the hashMap has 12 buckets filled size will be doubled 
       
        // HashMap<Integer,String> map = new HashMap<>(16,0.75f);
        // map.put(1,"Adarsh");
        // map.put(2,"Raj");
        // map.put(3,"Rajiv");
        // map.put(4,"Rama");
        // System.out.println(map.toString());
        
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
        // for(int i : map.keySet()){
        //     System.out.println(i+"*"+map.get(i));
        // }
        // for(Map.Entry<Integer,String> i : map.entrySet()){
        //     System.out.println(i.setValue(i.getValue().toUpperCase()));
        //     System.out.println(i);
        // }
        // Time Complexiy of HashMap
        //get : O(1) ->O(log n)
        //put : O(1) ->O(log n)
        //remove : O(1)->O(log n)
        //containsKey : O(1)->O(log n)
        //containsValue : O(n)->O(n)
        //size : O(1) // Size store in seperate field
        // same is with isEmpty() method
        HashMap<String,Integer> map = new HashMap<>();
        map.put("Apple",50);
        map.put("Banana",100);
        map.put("Orange",200);
        map.put("Mango",300);
        System.out.println(map);
    }
}
import java.util.Map;
import java.util.*;
public class LRUCache<K, V> extends LinkedHashMap<K, V> {

    private int capacity;

    public LRUCache(int capacity) {
        super(capacity,0.75f,true);
        this.capacity = capacity;
    }

    @Override
    public boolean removeEldestEntry(Map.Entry<K, V> eldesEntry) {
        return size() > capacity;
    }

    public static void main(String[] args) {
      LRUCache<String,Integer> lru = new LRUCache<>(3);
      lru.put("Alice",1);
      lru.put("Bob",2);
      lru.put("Raj",3);
      lru.put("Alice",5);
      lru.put("Ad",4);

      lru.get("Alice");

      System.out.println(lru);

    }
}

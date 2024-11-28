import java.util.*;

public class ComparatorsMethods {

    public static class MyComparator implements Comparator<Integer> {
        // In what order we will get the list sorted ascending or descending will be decided by using this compare method
        // compare method return positive value if o1 > o2  order will be ascending and negative value if o1 < o2 order will be descending    
        @Override
        public int compare(Integer o1, Integer o2) {
            return o2-o1;
        }
    }
    public static void main(String[] args) {
        List<Integer> ls = new ArrayList<>();
        ls.add(3);
        ls.add(6);
        ls.add(1);
        ls.add(2);
        ls.add(5);
        ls.sort(new MyComparator());
        // with the help of comparator by comparing just first two element of the list we can decide the order of the list
        System.out.println(ls);
    }
}
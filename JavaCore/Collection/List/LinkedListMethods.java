import java.util.Arrays;

public class LinkedListMethods {
    
    public class Node{
        private int value;
        private Node next;
        private Node prev;
    }
    public static void main(String[] args) {  

        //Linked list is better in  performance compare to arraylist in the following context:

        // LinkedList<String> list = new LinkedList<>();
        // list.add("Ad");
        // list.add("Raj");
        // list.add("Rajiv"); 
        // list.add("Rama");
        // list.add("Ad");
        // list.remove("Rajiv");
        // list.add(ls);
        // list.addFirst("Adarsh");
        //list.addLast("AD");
        //list.removeFirst();
        //list.removeLast();
        //list.removeFirstOccurrence("Ad");
        //list.removeLastOccurrence("Ad");
        //list.removeif(s->s.length()>3);
        
        // System.out.println(list);


        //if we want to create a linked list on the go without using add method we can use this Arryas.asList();
        // LinkedList<String> ls = new LinkedList<>(Arrays.asList("Karan","Aditya","Adarsh","Chirag"));

        // LinkedList<String> removels = new LinkedList<>(Arrays.asList("Aditya","Adarsh"));
        // ls.removeAll(removels);

        // System.out.println(ls);

    }  
}

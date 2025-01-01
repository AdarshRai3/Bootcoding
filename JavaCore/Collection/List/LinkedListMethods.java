
public class LinkedListMethods {
    
    public class Node{
        private int value;
        private Node next;
        private Node prev;
    }
    public static void main(String[] args) {  

        //Linked list is better in  performance compare to arraylist in the following context:

        LinkedList<String> list = new LinkedList<>();
        list.add("Ad");
        list.add("Raj");
        list.add("Rajiv"); 
        list.add("Rama");
        list.add("Ad");
        list.remove("Rajiv");
        LinkedList<String> ls = new ArrayList<>(Array.asList("Karan","Aditya"));
        list.add(ls);
        System.out.println(list);

    }  
}

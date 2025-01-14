import java.util.*;
public class HashandEqualsMethod {
    
    public static void main(String[] args){
        HashMap<Person,String>hs = new HashMap<>();
        Person p1 = new Person(1,"Ram");
        Person p2 = new Person(2,"Laxman");
        Person p3 = new Person(1,"Ram");

        hs.put(p1, "Enginner");
        hs.put(p2,"Manager");
        hs.put(p3,"CTO");

        
        System.out.println(hs);
    }
}



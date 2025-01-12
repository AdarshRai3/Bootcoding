import java.util.Vector;
import java.utils.*;
public class VectorListMethods {
    //vector is legacy class in java, unlike linked list and arraylist it is synchronized and thread safe 
    //Since vector are thread safe and synchronized that means it has overhead which means it take time to perform operation on it therefore generally we prefer ArrayList over LinkedList
    //Dynnamic Array
    //Index based accessing random access
    //Synchronized means it is thread safe means it can be used in multithreaded environment without corrupting the data 

    public static void main(String[] args) {
    Vector<Integer>vector = new Vector<>();
    vector.add(3);
    vector.add(5);
    vector.add(6);
    vector.add(7);
    vector.remove(2);
    vector.add(2,4);
    vector.set(2,6);
    vector.get(3);
    vector.size();
    vector.capcity(5);
    vector.capicity(3,5);
    vector.isEmpty();
    vector.clear();
    vector.contains(3);
    vector.indexOf(3);
    vector.lastIndexOf(3);
    vector.trimToSize();
    vector.ensureCapacity(5);
    vector.toArray();
    vector.firstIndexof(3);

    //Unlike arrayList and linkedList , vector does have method to get the capicity
    //Default capicity is 10
    //Default resizing is 2x 
    //Vector has internally dynamic array impleamentation
    //Vector are thread safe and synchronized means they can be used in multithreaded environment but but to this they also have an overhead due to locking and unlocking of the thread     
    // example for vector thread safety 

    Thread t1 = new Thread(()->{
        for(int i =0;i<1000;i++){
            vector.add(i);
        }
    });
    Thread t2 = new Thread(()->{    
        for(int i =0;i<1000;i++){
            vector.add(i);
        }   
    });
    t1.start();
    t2.start();
    try{
        t1.join();
        t2.join();
    }catch(InterruptedException e){
        e.printStackTrace();
    }
    System.out.println(vector.size());
  }
}
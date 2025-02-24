public class GC {
    
    public static void main(String[] args){
        WeakReference<Phone> phoneWeakRefererence = new WeakReference<>(new Phone("Nokia105", 10000));
        System.out.println(phoneWeakRefererence.get());
        System.gc();
        try{
             Thread.sleep(10000);
        }catch(Exception ignored){

        }
        System.out.println(phoneWeakReference);
        
    }
    //this is part of garbage collection , generally garbage collector remove the value of weak hashmap
}

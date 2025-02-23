import java.util.*;
import java.util.List;
import java.util.concurrent.CopyOnWriteArrayList;

public class CopyOnRightArrayListDemo{
       
    // In Java we have ArrayList and LinkedList which are not thread safe and vectors are thread safe but have massive overhead due to locking and unlocking of the thread.
   
    // to solve this problem we have CopyOnWriteArrayList which creates a copy of an array and update in that array and after updates set the reference from old array to new updated array. 

    //This is used when we need more read operation than write operations
    
    //Read Operations are fast and direct as it will not update it is the copy that will be updated .
    //For every write operation there will be a copy that has to be generated and then after updating we change the reference of old list to this list and delete the old list.
    public static void main(String[] args) {
    // List<String> ls = new CopyOnWriteArrayList<>();
    //   ls.add("Milk");
    //   ls.add("Eggs");
    //   ls.add("Butter");
    //   System.out.println(ls);

    //   for(int i=0;i<ls.size();i++){
    //     if(item==milk){
    //         ls.add("Butter");
    //     }
    //   }
    //   System.out.println(ls);
    // }
       List<String> sharedList = new CopyOnWriteArrayList<>();
       sharedList.add("item1");
       sharedList.add("item2");
       sharedList.add("item3");

       Thread readerThread = new Thread(()->{
         try{
          while(true){
            for(String s : sharedList){
               System.out.println("Reading from List: "+s);
               Thread.sleep(100);
            }
          }
         }catch(Exception ex){
             System.out.println("Exception from Reader Thread");
         }
       });
       Thread writerThread = new Thread(()->{
         try{
          Thread.sleep(500);
          sharedList.add("item4");
          System.out.println("Add item to the list");

          Thread.sleep(500);
          sharedList.remove("item5");
          System.out.println("Delete from the list");
         }catch(Exception ex){
           System.out.println("Exception is from writer Thread");
         }
       });
       readerThread.start();
       writerThread.start();
    }
}
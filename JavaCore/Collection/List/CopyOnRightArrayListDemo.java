public class CopyOnRightArrayListDemo{
       
    // In Java we have ArrayList and LinkedList which are not thread safe and vectors are thread safe but have massive overhead due to locking and unlocking of the thread.
   
    // to solve this problem we have CopyOnWriteArrayList which creates a copy of an array and update in that array and after updates set the reference from old array to new updated array. 

    //This is used when we need more read operation than write operations
    
    //Read Operations are fast and direct as it will not update it is the copy that will be updated .
    //For every write operation there will be a copy that has to be generated and then after updating we change the reference of old list to this list and delete the old list.
    public static void main(String[] args) {
    List<String> ls = new CopyOnWriteArrayList<>();
      ls.add("Milk");
      ls.add("Eggs");
      ls.add("Butter");
      System.out.println(ls);

      for(int i=0;i<ls.size();i++){
        if(item==milk){
            ls.add("Butter")
        }
      }
      System.out.println(ls);
    }
}
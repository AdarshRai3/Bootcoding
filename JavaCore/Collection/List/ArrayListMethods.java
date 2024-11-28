package JavaCore.Collection.List;

import java.util.*;
import java.util.ArrayList;

public class ArrayListMethods {
  public static void main(String[] args) {
    
    ArrayList<Integer> list = Arrays.asList(1,2,3);

    

    System.out.println(list);


    


    // List<Integer>list1= new ArrayList<>();
    // // this is  all a valid method to declare arraylist since List is a parent interface to ArrayList 
    // List list2 = new ArrayList<>();
    // //this is also a valid method to declare arraylist since we don't want to type bound our carrylist it can have any type of data
    // ArrayList<Integer>list= new ArrayList<>();
    // //this is a valid method to declare arraylist but here we have to specify the data type of the arraylist

    
    // list.add(1);
    // list.add(3);
    // list.add(4);
    
    
    // //Here we have used add method to add elements in the arraylist
    // list1.add(22);
    // list2.add(33);
    // list2.add("Ram");
    // list2.add(true);

   
    // //since there is a 0 base indexing in Arraylist we can add the element in the Arraylist by using add method and it will add the number at the place of the index and increase the size of the list. like here we list:[1,3,4] after running list.add(1,10) list:[1,10,3,4]
    // list.add(1,10);
    
    // //this set() method will not increase the  size of the arraylist but just go to the index 1 and replace the value 10 with 20;
    // list.set(1,20);

    // //this get() method will get the value present at index 2;
    // list.get(2);

    // //this contains() method will check whether the element is present in the arraylist or not and give us the boolean value in true or false;
    // list.contains(20);

//    //What is difference between size and capacity?
//    //Size is the number of element in the arraylist 
//    //Capacity is the maximum number of element that we can store in the arraylist before we have to resize it.
//    //Capicity will increase by 50% of the capicity means if the default capacity of 10 is 50% of 10 then the capacity will be 15}
   
//    ArrayList<Integer> list3 = new ArrayList<>(15);
//    //here we change the capicity of the arraylist make it equal to 15 so arraylist will now resize after size is 15
   
//    //now suppose we have the arraylist and we have to somehow remove the number of element from the arraylist

//    // if we want to remove the unnecessary overhead in the memory we can use the trimToSize() method

//      list3.trimToSize();
// //    this will make capicity == size , therefore remove the unnecessary overhead in the memory


// //    //now suppose we to make any other collection as List for that we simply use 
//    List<Integer> list4 = Arrays.asList(1,2);
//    //this will convert the array into the list

  }

}  
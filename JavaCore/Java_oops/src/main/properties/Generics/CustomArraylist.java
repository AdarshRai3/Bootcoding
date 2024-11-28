package src.main.properties.Generics;
import java.util.*;
public class CustomArraylist {
    
    private int [] data;
    private static int DEFAULT_SIZE = 10;
    private int size = 0;

    public CustomArraylist(){
        this.data = new int[DEFAULT_SIZE];
    }

    public void add(int num){
        if(isFull()){
            resize();
        }

        data[size++]=num;

    }

    private boolean isFull(){
        return size==data.length;
    }
    
    private void resize(){

        int []  temp = new int[data.length * 2];
        //copy the current items in the new array.
        for(int i = 0;i<data.length;i++){
            temp[i]=data[i];
        }
        data = temp;
    }

    public int remove(int num){
        int removed = data[--size];
        return removed;
    }

    public int get(int index){
        return data[index];
    }
    public int size(){
        return size;
    }

    public void set(int index, int value){
        data[index]= value;
    }

    public String toString(){
        return "CustomArraylist{" + "data=" + Arrays.toString(data) + ", size=" + size + '}';
    }
    public static void main(String[] args) {
        
       CustomArraylist list = new CustomArraylist();
         list.add(3);
         list.add(6);
         list.add(0);

         System.out.println(list);
         ArrayList<Integer>list2 = new ArrayList<>();
         list2.add(3);
         list2.add(6);
         list2.add(0);
         System.out.println(list2);

         ArrayList<String>list3 = new ArrayList<>();
         list3.add("Adarsh");
         list3.add("Raj");
         list3.add("Rajiv");
         System.out.println(list3);
       
    }
}
//here we can see that our custom arraylist can perform all the function of the arraylist but the major drawback of the customArrayList that we have created is that it only works for int type whereas Arraylist will work for all the types since it use Generics.  
//Generic helps to provide parameterized types to our data structure such as Arraylist so we can use it with different data types.
//Generic helps us to provide type safety to our code by using generics in ArrayList<Integer> list2 = new ArrayList<Integer>();we are making sure that the Arraylist will only all Integer type data.


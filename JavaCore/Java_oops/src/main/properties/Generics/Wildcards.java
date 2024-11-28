package src.main.properties.Generics;
import java.util.*;
public class Wildcards<T extends Number> {
    private Object[] data;
    private static int DEFAULT_SIZE = 10;
    private int size = 0;

    public Wildcards(){
        this.data = new Object[DEFAULT_SIZE];
    }
    public void add(T num){
        if(isFull()){
            resize();
        }

        data[size++]=num;

    }

    private boolean isFull(){
        return size==data.length;
    }
    
    private void resize(){

        Object []  temp = new Object[data.length * 2];
        //copy the current items in the new array.
        for(int i = 0;i<data.length;i++){
            temp[i]=data[i];
        }
        data = temp;
    }

    public T remove(int num){
        @SuppressWarnings("unchecked")
        T removed =(T)(data[--size]);
        return removed;
    }

    public T get(int index){
        @SuppressWarnings("unchecked")
        T ans = (T)(data[index]);
        return ans;
    }
    public int size(){
        return size;
    }

    public void set(int index, T value){
        data[index]= value;
    }
 
    @Override
     public String toString(){
        return "CustomGenericArrayList{" + "data=" + Arrays.toString(data) + ", size=" + size + '}';
    }
    public static void main(String[] args) {
        
        Wildcards<Integer> list = new Wildcards<>();
        for(int i =0;i<15;i++){
            list.add(2*i);
        }
        System.out.println(list);
    }
   
}
//Wildcards are used to restrict the type we can use in generics,for example <T extends Number> will only allow use the types that are subclasses of Numberor Number.
//that means that T is either be a number or a subclass of number
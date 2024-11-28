package src.main.properties.Generics;

import java.util.Arrays;

public class CustomGenericArrayList<T> {
    private Object[] data;
    private static int DEFAULT_SIZE = 10;
    private int size = 0;

    public CustomGenericArrayList(){
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
        
       CustomGenericArrayList<Integer> list = new CustomGenericArrayList<>();
        for(int i =0;i<15;i++){
            list.add(2*i);
        }
        System.out.println(list);
    }

}
//as we can see here we are using class A<T>{} for using T as generic type so we can use this list for all the data types but note that we cannot use t to create object so for object creation we still uses Object class
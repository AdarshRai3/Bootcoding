package src.main.Cloning;

public class Sheep implements Cloneable{
    int age;
    String name;
    int [] arr;

    public Sheep(int age, String name, int[] arr) {
        this.age = age;
        this.name = name;
        this.arr = arr;
    }
    
    // public Sheep(Sheep other){
    //     this.age= other.age;
    //     this.name=other.name;

    // }
    //Alternative method if we not using cloning but this is not good in terms of performance.

    // @Override
    // protected Object clone() throws CloneNotSupportedException {
    //     return super.clone();
    // }this method creates shallow copy of an object.

    @Override
    protected Object clone() throws CloneNotSupportedException {
        Sheep twin = (Sheep) super.clone();//this will create a shalow copy
        //make a deep copy
        twin.arr = new int[twin.arr.length];
        for(int i=0;i<twin.arr.length;i++){
            twin.arr[i] = this.arr[i];
        }
        return twin;
    }
}
//Cloning the object in java 
// We can clone object in java using Clonable interface present in java.lang package
// we using clonable clone method we must use throws CloneNotSupportedException 

//clone method we are using here is overriding the clone method present in object.

//In clone() method we are doing shallow copy of an object.
//Shallow copy means that we are making copy of an object then the primitive types get copy(int,char,float, double,long,boolean) and the object type(String, array,Integer) dont get copy by passed as reference pointer to original object that means if we create change in original copy after cloning then it will reflect in clonned object.

//this problem of shallow copying can be solved by using deep copying in which we also copy object type such that there is not connection between original object and cloned object.

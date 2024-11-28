package src.main.properties.Encapsulation;

public class Alpha{
    private int num;
    protected int color;
    public int id;
    String name;
    int [] arr;
    //by using private int num we are data-hiding num 
    //but we can access as well as changed the data of num by using getter and setter function.

    public int getNum(){
        return num;
    }
    public void setNum(int num){
        this.num = num;
    }

    //we cant access num since it is private but we can access num via getNum() and setNum() functions.
    public Alpha(int num, int color,String name) {
        this.num = num;
        this.name = name;
        this.color = color;
        this.arr = new int[10];
    }
}
//Access modifiers are : Default,Public, Private and Protected
//Public: We can access the data of the class anywhere
//Private: We can only access data within the same class.
//Default: In the different package it will not be able to allow but in the same package it will be allowed to access it .
//Protected: It is linked with the inheritance.Means that if A is parent then all the subclass(children) can access the protected data of A. 
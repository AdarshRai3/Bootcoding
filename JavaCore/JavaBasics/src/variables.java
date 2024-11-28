package JavaCore.JavaBasics.src;
import java.util.*;

public class variables {
    static int c=12;//static variable
    public void fun(){
        final int f=10;//instance variable
        System.out.println(f);
    }
    public static void main(String [] args){
        int k = 45;//instance variable
        System.out.println(k);
        System.out.println(c);
        variables obj = new variables();
        obj.fun();
    }
}
//There are 3 types of variables in java:Instance variables,Static variables,Local variables
//Instance variables:
//Declare inside class but outside method
//Created when object of the class is instantiated
//Each object has its own copy of instance variables
//Accessible within the class
//Decalred with static keyword 
//Only one copy exist for each object
//Associated with class instead of object
//Shared among all the instances of the class
//Local variables:
//Declared inside the method or the block
//Scope is limited within a method or a block
//Created when the method is called & destroyed when the method returns
//final keyword
//Used to create constant ,once assigned value cannot be changed 
//Can be used with static, instance and local variables
//When used with methods it cannot be overriden
//When used with classes it cannot be inherited
//static keyword
//static keyword when used with method or varible then that method or variable belongs to the class
//can be accessed without creating the object of the class
//often used for utility method and shared resources.
//static varaible and methods are class level rather than object level.
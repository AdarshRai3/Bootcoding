package src.main.Cloning;

import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws CloneNotSupportedException {
        Sheep s1 = new Sheep(7,"Mary",new int[]{1,2,3,4,5});
        // Sheep twin = new Sheep(s1);

        Sheep twin = (Sheep) s1.clone();
        System.out.println(twin.age + " " + twin.name);
        System.out.println(Arrays.toString(twin.arr));
        s1.arr[0]=100;
        System.out.println(Arrays.toString(twin.arr));
        //Due to shallow copy we can see change in value of S1 object type reflects change in value of object type in twin object.
        //now we using a deep copy in cloning the object in which we encounter object type during cloning we simply copy those clone object replace them with the existing one hence each object get its own uniquie copy of cloned object

    }
}
//here we can see that the object twin is the copy of S1 in Sheep class but it taking more time by using new keyword to create a copy of object S1
//In twin we are just using excat copy of S1, we can reduce time and esources by using clone method.
//In Java.lang we have interface called as clonable.
// cloning is the process of creating a copy of an object and it is much faster than using constructor(Sheep other){this.age=other.age;this.name=other.name;} 

//the main question that we have here is "This inteface dont have any abstract method then why are you implementing this"
//the simple answer is implements Clonable interface is the way of telling JVM that have to perform clone() method on Object of type Human.


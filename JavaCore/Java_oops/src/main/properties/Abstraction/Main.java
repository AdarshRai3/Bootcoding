package src.main.properties.Abstraction;

public class Main {
   public static void main(String args[]){
     Son Ram = new Son(500000);
     Ram.career("Engineer");
     Ram.partner("Sita",25);
    

     Daughter Rose = new Daughter(200000);
     Rose.career("Doctor");
     Rose.partner("Jack",28);

    //  Parent Raj = new Parent();
    //We cannot create object of the abstract class
    Parent Mahima = new Daughter(100000);
    Mahima.career("Engineer");
    // this is perfectly valid since we can have reference variable of abstract parent class but we cannot create object of the abstract class.

     Son.hello();
   }
}
//Abstraction is the process of hiding the unnecessay details and showing only the essential ones 
//when we create an  abstract method, the child class also have to be abstract 
//In abstract method we dont write any body of the method we give child class to implement the body of the method by itself
//We cannot create object of the abstract class also we cannot create abstract constructor  
//We use abstract keyword to create abstract class which implictely also make all the methods() also abstract that means.
//abstract class Parent(){abstract void career(String name); }but the body of this function is return in son and duaghter class and these method in child class will run at the time of implementation using method overriding concept of run time polymorphism
//static method cannot be abstract because abstract method requires to be overriden and static method cannot be overriden because of early binding but we can create static method in abstract classes. 
//normal method() can be put in abstract class

//Interface 
//As of now we have seen that java dont support multiple inheritance due to the collisions but we can using interface 
//Interface are adjacent to class but with some major differences such as : all the instance varibles in interface are static final by default.
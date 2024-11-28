package src.main;
import static src.helper.Helper.hello;

import src.main.Singleton.Singleton;
import src.main.properties.Encapsulation.Alpha;
public class Main{
    public static void main(String[] args) {
        // Your code here
        //Class: A class is the named group of properties and functions. Think of it as a car blueprint, it is logical construct that we use to create instance(actulal physical structure) called as object.Class is just the blueprint , but object is something that exist in the real world . That means object occpies the space in the memory
        class Student{
           int rno;
           String name;
           float marks;
           
           Student(int rollno, String name , float marks ){
            this.rno = rollno;
            this.name = name;
            this.marks = marks;
           }

           Student(Student other){
            this.name = other.name;
           }

           Student (String name){
            this.name = name;
           }

           Student(){
            //this is how you can call other constructor inside the constrctor 
            //internally , new Student(12,"Raj",98.5f)
            this(12,"Raj",98.5f);
           }

           void greeting(){
            System.out.println("Hi this is "+ this.name);
           }
           void changeName( String othername){
              this.name = othername;
           }


           @Override
           protected void finalize() throws Throwable {
               System.out.println("Object is destroyed ");
           }
           
        }
        //    Student obj;

        // for(long i =0; i<1000000000;i++){
        //     obj = new Student();
        //     System.out.println(obj);
        //    }  
        //whenever the memory get overloaded , the garbage collector run and it will destroy the objects and then finalize method will be called

        //Object: It is instance of the class. The object has 3 essentail properties: State, Identity and behaviour.Object are stored in heap memory whereas as the refernce variable are stored in the stack memory and stack is faster than heap; The variable inside the class which are outside the method are called as instance variable which are use to create the object(instance of the class).
        //Create the object in java we use reference varible=> Student s1 = new Student(); 
        // The new keyword dynamically allot memory to the object at run time and returns a refence variable in this case s1 to it. Student s1 = new Student(); The left side of the code excutes at compile time whereas the right part of the code execute at runtime and that time memory location take dynamically(memory allocation take place during runtime)
        //
        // Student S1 = new Student();
        // S1.name = "Adarsh";
        // S1.rno = 7;
        // S1.marks=90;

        //in the above intiation of the object : Student S1 = new Student(); in the above example we have to call the value continously to using dot operator to set the value of the instance variable for that object , to avoid this we can use consturctor => Student() but it is by default constructor, it name will be smae as the name of the class 

        //Constructor is the special type of the function in the class that runs whenever the object is created and it allocates some variable to the class.

        //Constructor name will be same as that of the class.
        // In constructor we use "this" keyword to bind the refernce vaiable of the current object to the instance variable values
        //"this" basically means which object you are referring currently. 

        // As in the above student class you can we that we have used 2 constructor with different argument this is called as function overloading which is concept of polymorphism

        // Calling constuctor from another constructor 
        Student S1 = new Student(3,"Adarsh",70.8f);
        S1.changeName("Priyansh");
        S1.greeting();
        System.out.println(S1.name);
        System.out.println(S1.rno);
        System.out.println(S1.marks);
         
        Student random = new Student(S1);
        
        System.out.println(random.name);
        Student random2  = new Student();

        System.out.println(random2.name);
        Student one = new Student();
        Student two = one;
        
        one.name = "Adarsh";
        System.out.println(two.name);
        //in this case two.name will be same as one.name ,means these refernce variable are just pointing to the object in the memory heap.
        //primitive datatype in java are stored in memory stack because in java primitive datatypes are not treated as object but as seprately as primitive that is why we dont have we dont use new keyword in java.
        // int a = 10; char a = 'a' these are not objects
        
        //Wapper classes
        //It is true that primitve datatype are not treated as object but we can use them as object by using wapper class in java 
        //Integer num = 12; now num is the object

        //We know that in java primitive datatypes are pass by value , but object can be pass by refernce 
        
        //Since the primitive datatype in java are only passed by value that means we cannot swap the value of these using the function swap which is taking the value like we do in C++. also we use wapper class to convert primitive datatypes(int a -> Integer a) into objects which are pass by reference then also we cannot swap the integer reason is that Integer class is final.
        
        //final keyword means that we cannot change it further its value is fixed also we should always initialise while declearing.
        
        //when the no-primitive is final we cannot reassign it

        final Student kunal = new Student("kunal");
        kunal.name ="james";
        //kunal = new Student(name : "Ajay") this reintialisation will give you an error because after using the final keyword we can't reintialise the class we can tweek with instance variable but not the class.
        

        //grabage collection:In java collection is automatic , unlike c++ where we have to use destructors to free the memory but in java we can use finalize() method to define the activities after garbage collection means we cannot destroy object but we can  decide what to do after the object is destroyed.
         
     
         //Packages
        //  In java packages are used to group classes together , you can understand package as folder with good naming convention that help us to access the functionality across multiple different folder among multiple different classes easily 
        //by using package name convention we can access the classes' functionality using "import statement" in java
        
        hello(); //this hello function is defined in the package helper folder and it can be accessed from the main folder
       
        Human Adarsh = new Human(25,"Adarsh",5.10f,1000000000);
        Human Sagar = new Human(0, "Sagar", 6.2f, 0);

        System.out.println(Adarsh.income);
        System.out.println(Sagar.income);
        //Notice that since Human.java and Main.java are in same folder we dont need import statement 
        
        //staic keyword
        // static keyword in java can be used to when we used to define the property of the class that don't change with the object and it should always be called by classname.static_variable_name
        //staic variable can be accessed without creating or referring to the object of that class
        // public static void main (String[] args) {} in this we have to put main method as static because we can use staic method without creating an object of the class
        // A staic method() can only access static variables or method
        // A non-static data: methods() and variable cannot be access without creating or referring to an object, static method() cannot use it because it requires an instance.
        // there is solution to this problem , it is to create the object and then call the non-static method viva staic method inside that object
        
         
        System.out.println(Human.gravity);
     

    } 
    
    //Read Inner classes and SingleTon classes from classes.java 
   //. operator is used to binds the instance method and instance variable with the refernce class
     Singleton S1 = Singleton.getInstance();
     Singleton S2 = Singleton.getInstance();
     Singleton S3 = Singleton.getInstance();
    // we can create refence variable using the instance of the singleton class and all of them are pointing the same instance variable that have beeen created in the singleton class.
    //instead of creating new onject the singleton class will create only one object and passed it as reference to the many refence variable.
    //All the 3 referene variable will point to the same object

    Alpha a = new Alpha(10,459874,"Ajay");
    int nos = a.id;
    int noa = a.getNum();
    //Access modifier of id is public that means that we can access it anywhere within the project.
    //Access modifier of num is private to access it we use getter and setter function and since the getter function return int type we need to create variable of int type to access it value.



    
}


 //Now we will learn about the four most important properties of object oriented programming :
    //Inheritance, Encapsulation, Abstraction, and Polymorphism
    //read properties folder
    //Java doesnt support multiple inheritance since it creates ambugity in the program suppose if A(n==3) and B(n==5) then if C extends A,B and we create object (C obj = new C(n) )this will give us ambugity that from which class C inherit the n , therefore java dont support multiple inheritance.
    // Heirarcahal inheritance One parent class have may children classes
    //Hybrid Inheritance is the combination of multiple and single inheritance but as we know that java dont support multiple inheritance so we dont have Hybrid inheritance in java.

    //Polymorhism:Use the one thing in many forms 
    // there are two types of polymorphism 
    // Compile time Polymorphism (Method overloading)
    // Run time polymorphism (Method Overriding)
    //read properties folder

    //Encapsulation 
    //Wapping up the implementation of the data members and methods() of the class in a class
    //Enscapsulation is sovling implementation issue
    //Encapsulation focuses on the internal working 
    //Enscapuslation is the process of containing the information
    //Enscapulation is implemented using access modifiers:private, public,protected and be accessed using getter and setter function
    //Data Hiding focuses on data security whereas Encapsulation focuses on wapping the data to hide the complexity of the System.
    //Enscapsulation is the sub process in data hiding.

    //Abstraction
    //Hiding the unecessary details and showing only the essential details.
    //Abstraction is solving design issue
    //Abstraction focuses on the external 
    //Achived using abstract classes and interfaces
    //Abstraction is the process of gaining the information


    //packages
    //There are two types of Packages: User-define and In-built packages.
    //In-Built packages: java.lang, java.util, java.io, java.sql, java.awt, java.text
    //java.lang is language specific package , it is automatically installed
    //java.util is package contains collection framework and data-struture 
    //java.io is package contains input and output stream
    //java.sql is package contains jdbc driver
    //java.awt is package contains all the awt classes
    //java.net is package contains all the network related classes

    //now we talk about java Object class which is topmost class in class hierarchy
    //look at object demo in Encapsulation folder.
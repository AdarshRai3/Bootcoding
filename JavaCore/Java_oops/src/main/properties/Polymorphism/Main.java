package src.main.properties.Polymorphism;

public class Main {
    
    public static void main(String[]args){
       
       Shapes shapes = new Shapes();

       shapes.area();

       Circle circle = new Circle();

       circle.area();

       Triangle triangle = new Triangle();
      
       triangle.area();

    
       
    }
}
//Polymorphism 
// It means using same thing in different ways 
// In Java we have two types of polymorphism 
// 1>Static/Compile time polymorphism(method overloading)
// Method overloading means when the class having the multiple functions(methods, constructors) with the same name but are different on the bases of number of arguments, return types and datatypes.
//EX: A a = new A(); A b = new A(3,4); A c = new A(3,4,5);this is called compile time polymorphism because in this java can determine on compile time which method should be called.
// 2>Dyanamic/Run Time  polymorphism/Late Binding(method overiding)
//Above example in the Main.java is the example of method overriding. In this we have area() method in parent class Shapes as well as child class circle but we can clearly see on the runtime child class method will override the parent class method,because that we created object that we created is the object of the child class since java is able to determine which method to call at runtime, hence this type of polymorphism is called dyanamic/runtime polymorphism.
// In java if we want to check wether the child class method override the parent class we use @Override annotation.
// if the annotation dont give us the error that means the method is overriding otherwise in case of the error it is not overriding 

//Now we are dealing with the main question 
//Shapes shapes = new Circle(); in this we have 
// Refence type variable = object type variable
// Refence type determines what can be accessed and what can't be accessed whereas Object Type determines what class object is created which ultimately determines which method will override which method at runtime 

//What method can be access is determine by the referenc type variable and which method it can called at runtime is determine by the object type variable

//Method Overriding 
// 1.Child class Object will call the child class method 
// Childclass obj = new Childclass();
//2.Upcasting:ParentClass obj = new ChildClass(); which method() will be called at runtime is determine by Object type variable

// Now the question can be asked how java know that ,so java know which method to override by dynamic method dispatch it is mechanism of java , in which call to overriden method is resolved at runtime rather than compiled time 

// if you put final keyword in front of the method than you will not be able to overrride that method means if I put final area() in shapes class , this also means that the final method is resolved at compile time hence it known as "Early Binding".

//final keyword can also be used to prevent inheritance as well as dynamic polymorhism , will you want to prevent the class to inherited by other class just out final in front of them.

//whenever we put class as final that means implictly all its method will be final too.


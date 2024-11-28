package src.main;

// static public class InnerClasses
// this cannot be used as we cannot use static keyword with outer class
public class InnerClasses {

    static class Test{
          String name ;

          public Test(String name){
              this.name = name;
          }
    }
    
    public static void main (String[]args){
           Test a = new Test("Adarsh");
           Test b = new Test("Raj");
           System.out.println(a.name + "is friend of " + b.name);
    }
}
//outside class cannot be static 
//using static keyword with inner class Test is allowed 
//because it is dependent on Innerclasses , that is independent class(outer classes ) cannot be static
//if use the contents of the Test class without making it static , it will give error because Test is dependent on InnerClasses to use the Test class we have to create the object of the inner class first
// we can avoid this error by making the Test class static
// static means the class created using static keyword has its own property used, without creating the object of the outer class , but doesnt means static class cannot have it own object.  
//static level methods can be used without creating the object of the dependent class that means they are revovled during compile time not on runtime since it dont need any object 
//static variables are the property of the class not the object. 




package src.main.properties.Inheritence;

public class Box{
    double height;
    double width;
    double length;

    Box(){
        // super(); Object class
        this.height=-1.00;
        this.width=-1.00;
        this.length=-1.00;
    }
    //create a static method 
    //static method are the method that we can use directly without creating the refernce variable.
    // we can inherit static method but we cannot override static method.
    static void greeting(){
        System.out.println("Hey, look I am in the Box class.Greetings");
    }

    Box(double side){
        this.width=side;
        this.height=side;
        this.length=side;
    }

    Box(double l,double w,double h){
        this.height=h;
        this.width =w;
        this.length=l;
    }

    Box( Box old){
        this.height = old.height;
        this.width = old.width;
        this.length=old.length;
    }
    
    public void Info(){
        System.out.println("Running the box...");
    }
}
  //Inheritance 
    //Inheritance is property by which we can inherit the properties of the parent(base) class to the children class
    //This is done by using the extends keyword
    // public class Box2 extends Box{}, this extend that Box2 will have all the properties of Box
    // Object of child class can access all the properties of the parent class but the child of parent class cannot access the properties of the parent class 

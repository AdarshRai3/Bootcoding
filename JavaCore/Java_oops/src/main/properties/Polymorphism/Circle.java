package src.main.properties.Polymorphism;

public  class Circle extends Shapes{
   //Late Binding
    @Override
   
    void area(){
        System.out.println("Area of the circle=Math.pie*radius*radius");
    }
}

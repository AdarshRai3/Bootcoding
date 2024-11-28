package src.main.properties.Inheritence;

public class Main {
    public static void main(String[]args){
        Box box1 = new Box();
        System.out.println(box1.height+" "+box1.length+" "+box1.width);
        Box box2 = new Box(3.00);
        System.out.println(box2.height+" "+box2.length+" "+box2.width);
        Box box3 = new Box(3.00,4.00,5.00);
        System.out.println(box3.height+" "+box3.length+" "+box3.width);
        BoxWeight box4 = new BoxWeight(13,12 , 5,75);
        System.out.println(box4.height+" "+box4.length+" "+box4.width+" "+box4.weight);
        Box box5 = new BoxWeight(24,25,10,100);
        System.out.println(box5.height+" "+box5.length+" "+box5.width);
        //In this case of Box5 reference variable we will only be able to access the properties of box only that are passed in super() in boxweight.
        //we can't access the weight property since it is the property of the child class object and the refence variable is of parent class.

        // BoxWeight box6 = new Box(0, 0, 0);
        //the reason we will get error in this case, because the child class reference variable can't access the object of parent class.

        //every class that we create refers to the object class hence we can use super() in every class
        //Importance point => What we can inherit depends on the type of referene variable not the object type.
        //"reference variable = new object types"
        Boxprice box6 = new Boxprice(3.00,5.00,7.00);
        System.out.println(box6.height+" "+box6.length+" "+box6.width+" "+box6.weight+" "+box6.cost);

        BoxColor box7 = new BoxColor(3.00,5.00,7.00,100,"red");
        System.out.println(box7.height+" "+box7.length+" "+box7.width+" "+box7.weight+" "+box7.color);
       // Both BoxColor and Boxprice are inherited from BoxWeight hence this is example of heirachical inheritance
       Box.greeting();
       //Since greeting is the static method in the box class we can use it without creating the refernce variable of the box class that means to use greeting we dont need to write Box box 8 = new Box();box8.greeting(); we can use it directly.
       BoxWeight.greeting();
       //we can inherit static methods like greeting from the box class but we cannot override it since for overriding the method we require refernce variable and object variable and both are not need for static method.
    } 
}

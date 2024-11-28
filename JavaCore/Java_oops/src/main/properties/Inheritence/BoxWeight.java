package src.main.properties.Inheritence;

public  class BoxWeight extends Box{
    double weight;
   public BoxWeight(double l,double w,double h,double weight){
       super(l,w,h);//this is super(l,w,h) constructor which is used to intialise the value of the parent class
       //also this child class includes the members and poperties of the parent class but we will still be not able to access the members which are declared as private 
       // super keyword we can call the super constructor of the parent class in the child class
       //we can also used super keyword to access the properties of the parent class in the child class just like this
    //    super.height=4;
    //    super.width=5;
    //    super.length=6;
    // this is usually if the child class and parent class both have the properties of the same name then we can use super keyword to access the properties of the parent class 
    // means if parent class also have weight then we can access it using the super keyword
    //super.weight = weight;
       this.weight = weight;
   }

   public BoxWeight(double sides,double weight){
    super(sides);
    this.weight=weight;
   }
    
   public BoxWeight(Box other){
    this.height = other.height;
    this.length = other.length;
    this.width = other.width;
    // this.weight = other.weight;this will give us an error because it is the reference variable that decides what we can inherit 
   }

}

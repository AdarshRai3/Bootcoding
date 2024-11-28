package src.main.properties.Encapsulation;

public class Objectdemo {
    int num;
    float gpa;
    
    public Objectdemo(int num, float gpa){
        this.num = num;
        this.gpa = gpa;
    }
    @Override
    public int hashCode(){
        return super.hashCode();
    }
    //hashCode will convert the object into an unique integer value
  
    
    public boolean equals(Object obj){
        return this.num == ((Objectdemo)obj).num;
        //since this.num is int type and obj is Objectdemo type, solution is we havve to cast it.
    }

    public Object clone() throws CloneNotSupportedException{
        return super.clone();
    }
    @Override
    public String toString(){
        return super.toString();
    }
    //toString method will give us the string representation of the Object.
    public static void main(String[] args) {
        Objectdemo obj = new Objectdemo(10,3.75f);
        Objectdemo obj2 = new Objectdemo(10,4.5f);
        System.out.println(obj);
        System.out.println(obj.hashCode());
        if(obj==obj2){
            System.out.println("Objects are same");
        }
        if(obj.equals(obj2)){
            System.out.println("Objects are same");
        }

        System.out.println(obj instanceof Objectdemo);
        //this will return true that means obj is object of Object demo.

        System.out.println(obj.getClass());
    }
    
}
//everyclass extends to object class internally.
//Object class is the topmost in heiracrchy in java.lang package.
//equals is a method whereas == is a operator , equals to method check the contents of the object whereas == check the address of the object in the memory.
//here we can also see that Objectdemo has 2 attributes num and gpa. it can create the ambiguity when we check the equality this can be solved by overriding the equals method.

//checking that something is object(instance of class) or not we can use instanceof operator it will give us the boolean value. 

//obj.getclass method it will return us the class in which the object belongs to we can use to get data aout the class like getconstructors getfields etc. also get class is final so we cannot override it.
package src.main.properties.Encapsulation;

public class Subclass extends Alpha{

    public Subclass(int num,int color,String name){
        super(num,color,name);
    }
    public static void main(String[] args) {
        Subclass obj = new Subclass(10,478123,"Raj");
        obj.getNum();
        obj.setNum(12);
        int colour = obj.color;
        System.out.println(colour);
        //Since color is protected we can access it within the subclass of A,since here main extends to A it becomes subclass of A 
    }
}

package src.main.properties.Encapsulation;

public class Main {
    public static void main(String args[]){
        Alpha obj = new Alpha(10,8974561,"Bhasma");
        obj.getNum();
        obj.setNum(12);

        String naam = obj.name;
        System.out.println(naam);
        //Access modifier of name is default so we can access it within the same package.
    }
}

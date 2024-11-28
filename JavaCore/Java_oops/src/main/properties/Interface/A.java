package src.main.properties.Interface;

public interface A {
    // static interface method should always have a body
    public static void heyGen(){
        System.out.println("Hey generator");
    }
    void greet();
}

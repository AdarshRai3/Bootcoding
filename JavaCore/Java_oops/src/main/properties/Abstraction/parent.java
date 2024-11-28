package src.main.properties.Abstraction;

abstract class Parent {

    int income;
 
    public Parent(int income) {
        this.income = income;
    }

    static void hello(){
        System.out.println("Hello from the Parent Side");
    }
    abstract void career(String name);
    abstract void partner(String name, int age);
}

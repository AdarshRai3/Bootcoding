package src.main;

public class Human {
    int age;
    String name;
    float height;
    long income;
    static float gravity = 9.81f;

    public Human(int age, String name, float height, long income) {
        this.age = age;
        this.name = name;
        this.height = height;
        this.income = income;
        Human.gravity = 9.81f;
    }

  
}

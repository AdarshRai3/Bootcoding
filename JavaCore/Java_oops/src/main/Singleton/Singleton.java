package src.main.Singleton;

public class Singleton{
    private Singleton(){

    }
    private static Singleton instance;

    public static Singleton getInstance(){
        if(instance == null){
            instance = new Singleton();
        }
        return instance;
    }
}
//Singleton class is used to create only one object.
//That means for Singleton class we dont want people to use constructors because the constructor is called whenever new object is created.
//that means it will create only one object and it will do it creating the object inside the singleton class and making the constructor private so that it can only be accessable to the that one object and that one object can be passed as refernce to other refence variable outside the singleton class by using the getInstance method;
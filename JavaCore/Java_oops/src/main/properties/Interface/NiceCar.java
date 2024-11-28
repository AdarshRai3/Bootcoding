package src.main.properties.Interface;

public class NiceCar {
    private Engine engine;
    private MediaPlayer player = new CDPlayer();
    public NiceCar(){
        engine = new PowerEngine();
    }

    public NiceCar(Engine engine){
        this.engine = engine;
    }

    public void start(){
        engine.start();
    }

    public void stop(){
        engine.stop();
    }

    public void startMusic(){
        player.start();
    }

    public void stopMusic(){
        player.stop();
    }

    public void upgradeCarEngine(){
        this.engine = new ElectricEngine();
        System.out.println("Car engine is upgraded from Power Engine to Electric Engine");

    }
}
//What method can be accessed depends on Refernce Variable and which version of the method will be executed depends on the object type 
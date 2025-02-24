public class WeakHashMapDemo {
    public static void main(String[] args){
        WeakHashMap<String,Image> WM = new WeakHashMap<>();
        
    }

    private static void simulateApplicationRunning(){
        try{
            System.out.println("Simulate Application Running ...");
            Thread.sleep(10000);
             
        }catch(Exception ex){
            System.out.println("Throwing Exception");
        }
    }
}

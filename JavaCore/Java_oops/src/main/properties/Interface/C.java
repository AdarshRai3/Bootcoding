package src.main.properties.Interface;

public class C {
    public interface NestedInterface {
        boolean isOdd(int num);
    }
}

class D implements C.NestedInterface{
    @Override
    public boolean isOdd(int num){
        return((num & 1)==1);
    }
}

//NestedInterface can be declared as public private or protected
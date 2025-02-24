
public class Phone{
    String model;
    Integer price;

    public Phone(String model ,Integer price  ){
        this.model = model;
        this.price = price;
    }

    public String getModel(){
        return model;
    }

    public Integer getPrice(){
        return price;
    }
    
    //whenever we run printf, println or print method toString() method will automatically run
    public String toString(){
        return "Model :"+model+",  Price :"+price;
    }

    public setModel(String model){
        return this.model = model;
    }

    public setPrice(Integer price){
        return this.price = price;
    }
    
}



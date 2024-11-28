package src.main.properties.Inheritence;

public class Boxprice extends BoxWeight{
     double cost;

    public Boxprice(double sides, double weight, double cost) {
        super(sides, weight);
        this.cost = cost;
     //parents class properties should be put in super and the children class properties should be put in this.properties
     //Box(l,w,h)->BoxWeight(l,w,h,weight){super(l,w,h) this.weight =weight;}->Boxprice(l,w,h,cost){ super(l,w,h,weight);this.cost = cost;}
    }
}

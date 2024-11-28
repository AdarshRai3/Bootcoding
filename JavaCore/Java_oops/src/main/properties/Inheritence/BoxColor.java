package src.main.properties.Inheritence;

public class BoxColor extends BoxWeight {
    String color;
    public BoxColor(double l, double w, double h, double weight, String color) {
        super(l, w, h, weight);
        this.color = color;
    }
}

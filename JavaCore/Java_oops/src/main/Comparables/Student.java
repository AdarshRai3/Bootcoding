package src.main.Comparables;

public class Student implements Comparable<Student> {
    int rollNos;
    float marks;

    public Student(int rollNos, float marks) {
        this.rollNos = rollNos;
        this.marks = marks;
    }
    
    @Override
    public String toString(){
        return marks + " ";
    }
    @Override
    public int compareTo(Student other) {
        int diff = (int)(this.marks - other.marks);
        // int diff = -(int)(this.marks - other.marks);
        //if we use this version we will get the list in descending order
        return diff;
    }
}
// When we compare the object it get difficult since unlike primiteve type the object dont have one value , it can have different attributes/fields and each field can have its own value
//to compare between two attributes of objects we use comparable interface in that we have method called compare to which we override in our Student class and customize it to compare the marks attributes  of two students
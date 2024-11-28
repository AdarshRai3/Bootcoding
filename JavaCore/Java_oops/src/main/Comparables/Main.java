package src.main.Comparables;

import java.util.Arrays;

public class Main  {
    public static void main(String[] args) {

        Student Mayur= new Student(1, 80.0f);
        Student Shreyas = new Student(2, 50.0f);
        Student Adarsh = new Student(3, 81.0f);
        Student Raj = new Student(5, 84.5f);
        Student Aditya = new Student(6 , 75.0f);

        Student[] list = {Mayur,Shreyas,Adarsh,Raj,Aditya};
        
        System.out.println(Arrays.toString(list));
        Arrays.sort(list);
        System.out.println(Arrays.toString(list));

        

        // if(Mayur>Shreyas){
        //     System.out.println("Mayur is greater");
        // }
        //this statement will give us error because mayur and shreyas are object having multiple  attributes using a compare operator we create the ambugity that which two attributes of Mayer and Shreyas are comparing.
        //This main problem is solve by using the interface called Comparables it also has generic type that can be used to compare any attibutes of objects.
        //Arrays.sort is using the compareTo method of the student class override the compare method of Arrays.sort class
        //we can also write our own compareto method inside Array.sort by using new Comparator<Student> directly like this 
        //Array.sort(list, new Comparator<Student>() {
        //     @Override
        //     public int compare(Student o1, Student o2) {
        //         return o1.marks-o2.marks;
        //     }
        //})
        // Array.sort(list, (o1, o2) -> o1.marks-o2.marks);
        //This will sort in descending order
        if(Mayur.compareTo(Shreyas)>0){
            System.out.println("Mayur got more marks than Shreyas");
        }

    }
}

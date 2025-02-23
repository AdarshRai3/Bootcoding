import java.util.*;

public class ComparatorsMethods {

    // public static class MyComparator implements Comparator<Integer> {
    //     // In what order we will get the list sorted ascending or descending will be decided by using this compare method
    //     // compare method return positive value if o1 > o2  order will be ascending and negative value if o1 < o2 order will be descending    
    //     @Override
    //     public int compare(Integer o1, Integer o2) {
    //         return o2-o1; // descending order
    //         // return o1-o2; // ascending order
    //         //In general O1 is always taken a larger value and O2 is always taken a smaller value.
    //         //O1>O2 -> O1-O2 is negative , that means int is -ve hence descending order.
    //         //O1<O2 -> O1-O2 is positive , that means int is +ve hence ascending order 
    //     }
    // }

    // public class StringComparator implements Comparator<String> {
    //     @Override
    //     public int compare(String o1, String o2) {
    //         return o1.length()-o2.length();
    //     }
    // }
    
    public static class Student{
        
        private String name;
        private float gpa;
    
    
    
        public Student(String name, float gpa){
            this.name = name;
            this.gpa = gpa;
        }
    
        public String getName(){
            return name;
        }
        public float getGpa(){
            return gpa;
        }
        
    }
    
  
    public static void main(String[] args) {
      
      


     List<Student> list = new ArrayList<>();
     list.add(new Student("Adarsh", 8.5f));
     list.add(new Student("Raj", 9.5f));
     list.add(new Student("Rajiv", 7.5f));
     list.add(new Student("Raja", 6.5f));
     list.add(new Student("Rama", 5.5f));
     
     list.sort((a,b)-> {
      if(a.getGpa()-b.getGpa()>0){
        return 1;
      }else if(a.getGpa()-b.getGpa()<0){
        return -1;
      }else{
        return a.getName().compareTo(b.getName());
      }
     });

     for(Student s : list){
        System.out.println(s.getName() + ":" + s.getGpa());
     }

     
    //    List<String> ls = Arrays.asList("Ramcharan","Raja","Rajiv");
    //    System.out.println(ls);
    // //    ls.sort((a,b)->a.length()-b.length());
    // //  (a,b)->a.length()-b.length(); // same order of a and b inside bracket then outside bracket then we can call it as lambda expression , it will sort in ascending order 

    //    ls.sort((a,b)->b.length()-a.length());
    // // (a,b)->b.length()-a.length(); // same order of a and b inside bracket then outside bracket then we can call it as lambda expression , it will sort in descending order
    //    System.out.println(ls);
    
    
       //    //We have given a task to sort the string by length in ascending order
    //    ls.sort(new StringComparator());
    //    System.out.println(ls);

    //    //Doing the same in descending order
    //    ls.sort(Comparator.comparingInt(String::length).reversed());
    //    System.out.println(ls);
    // this is long method to compare and sort the more easy method is using the lambda expression

    
    
    
    
        // List<Integer> ls = new ArrayList<>();
        // ls.add(3);
        // ls.add(6);
        // ls.add(1);
        // ls.add(2);
        // ls.add(5);
        // ls.sort(new MyComparator());
        // // with the help of comparator by comparing sort the list in descending order(O2-O1) & ascending order(O1-O2)
        // System.out.println(ls);
    }
}
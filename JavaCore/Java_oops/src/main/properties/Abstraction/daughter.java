package src.main.properties.Abstraction;

class Daughter extends Parent {
   Daughter(int income){
       super(income);
   }
  @Override
  void career(String name) {
    System.out.println("I am going to be "+name);
  }
  @Override
  void partner(String name, int age) {
    System.out.println("I want to marry "+name+" and his age is "+age);
  }  
}

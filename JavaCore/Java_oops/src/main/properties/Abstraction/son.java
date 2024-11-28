package src.main.properties.Abstraction;
 class Son extends Parent {
    
    Son(int income){
        // this.income = income;
        super(income);
    }
    @Override
    void career(String name) {
        System.out.println("I am going to be "+name);
    }

    @Override
    void partner(String name, int age) {
        System.out.println("I want to marry "+name+" and her age is "+age);
    }
}
//Here both partner and career are abstract method which means that we have to create the bodies of those method in the child class and run by using the method overrriding 
public class Students implements Comparable<Students> {
    String name;
    Integer RollNo;

    public Student( String name , Integer RollNo){
        this.name = name;
        this.RollNo = RollNo;
    }

    public String getName(){
        return name;
    }

    public void setName(String name){
        this.name = name;
    }
    
    public Integer getRollNo(){
        return RollNo;
    }

    public void setRollNo(Integer RollNo){
        this.RollNo = RollNo;
    }
}

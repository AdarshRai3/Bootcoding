import java.util.*;
public class Person{
    
    Integer id; 
    String name;
    
    public Person(Integer id , String name ){
        
        this.id = id;
        this.name = name;
        
    }

    public Integer getId(){
        return id;
    }

    public String getName(){
        return name;
    }

    public Integer setId( Integer id ){
       this.id = id;
       return id;
    }
   
    @Override 
    public String toString(){
        return "Id :"+id+",  Name :"+name;
    }

    @Override
    public boolean equals(Object obj){
        if(this == obj){
            return true;
        }
        if(obj == null || getClass() != obj.getClass()){
            return false;
        }
        Person other = (Person)obj;
        return id == other.getId() && Objects.equals(name, other.getName());
    }

    @Override
    public int hashCode(){
      return Objects.hash(id,name);
    }
}

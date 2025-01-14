public class LinkedHashMap {
    public static void main(String[] args){
        //LinkedHashMap : Insertion order(Natural Order) will be preserved
        LinkedHashMap<Integer,String> lhs = new LinkedHashMap<>();
        
        lhs.put(1,"Ram");
        lhs.put(2,"Laxman");
        lhs.put(3,"Hari");

        for(Map.Entry<Integer,String> e:lhs.entrySet()){
            System.out.println(e.getKey()+":"+e.getValue());
        }
    }
}

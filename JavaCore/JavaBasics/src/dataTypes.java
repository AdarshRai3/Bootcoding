package JavaCore.JavaBasics.src;
import java.util.*;
public class dataTypes {
    public static void main(String[] args){
        byte a = 10;//1 byte
        short b = 10;//2byte
        int c = 10;//4byte
        long d = 10;//8byte
        float e = 10.0f;//4byte
        double f = 10.0;//8byte
        boolean g = true;//1byte
        char h = 'a';//2byte
       System.out.println(a+"\n"+b+"\n"+c+"\n"+d+"\n"+e+"\n"+f+"\n"+g+"\n"+h);
       String name = "Aditya";
       System.out.println(name);
       int[] arr = {1,2,3,4,5};
       for(int i : arr){
        System.out.println(i);
       }
        long k = 1000;
        int l =(int)k;//this is narrowing of data type
        System.out.println(l);
        short m=12;
        long n=m;//this is widening of data type
        System.out.println(n);
    }
    
}
// there are two types of data types in java 
//Primative Datatypes:8 types:int,long,short,byte,float,double,boolean,char
//Non-primative Datatypes:String,Array,Class,Interface,Enum,Null
//There is another important concept that we have to learn here that is widening and narrowing of data types which is also known as type casting.

package JavaCore.JavaBasics.src;

import java.util.*;

public class scantask {

    private static void fun(int a , int b){
        int sum = a+b;
        System.out.println(sum);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        fun(a,b);
        sc.close();
    }
}
package JavaCore.JavaBasics.src;

public class operators {

    public static void main(String[] args) {
        // Arithmetic Operators
        int a = 10, b = 5;
        System.out.println("Arithmetic Operators:");
        System.out.println("a + b = " + (a + b));
        System.out.println("a - b = " + (a - b));
        System.out.println("a * b = " + (a * b));
        System.out.println("a / b = " + (a / b));
        System.out.println("a % b = " + (a % b));

        // Unary Operators
        System.out.println("\nUnary Operators:");
        System.out.println("++a = " + (++a));
        System.out.println("--b = " + (--b));

        // Relational Operators
        System.out.println("\nRelational Operators:");
        System.out.println("a == b is " + (a == b));
        System.out.println("a != b is " + (a != b));
        System.out.println("a > b is " + (a > b));
        System.out.println("a < b is " + (a < b));
        System.out.println("a >= b is " + (a >= b));
        System.out.println("a <= b is " + (a <= b));

        // Logical Operators
        boolean x = true, y = false;
        System.out.println("\nLogical Operators:");
        System.out.println("x && y is " + (x && y));
        System.out.println("x || y is " + (x || y));
        System.out.println("!x is " + (!x));

        // Bitwise Operators
        System.out.println("\nBitwise Operators:");
        System.out.println("a & b = " + (a & b));
        System.out.println("a | b = " + (a | b));
        System.out.println("a ^ b = " + (a ^ b));
        System.out.println("~a = " + (~a));
        System.out.println("a << 2 = " + (a << 2));
        System.out.println("a >> 2 = " + (a >> 2));
        System.out.println("a >>> 2 = " + (a >>> 2));

        // Assignment Operators
        System.out.println("\nAssignment Operators:");
        int c = a;
        System.out.println("c = a: " + c);
        c += b;
        System.out.println("c += b: " + c);
        c -= b;
        System.out.println("c -= b: " + c);
        c *= b;
        System.out.println("c *= b: " + c);
        c /= b;
        System.out.println("c /= b: " + c);
        c %= b;
        System.out.println("c %= b: " + c);

        // Conditional (Ternary) Operator
        System.out.println("\nConditional Operator:");
        String result = (a > b) ? "a is greater" : "b is greater";
        System.out.println(result);

        // instanceof Operator
        System.out.println("\ninstanceof Operator:");
        String str = "Hello";
        System.out.println("str instanceof String: " + (str instanceof String));
    }

}

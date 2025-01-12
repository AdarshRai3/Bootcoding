import java.util.ArrayList;
import java.util.LinkedList;
import java.utils.*;
public class Stack {
    public static void main(String[] args){
        Stack<Integer> stack = new Stack<>();
        // internally stack implements vector class and uses the LIFO principle to store the elements in the stack.
        stack.push(1);//to add an element
        stack.push(3);//to add an element
        stack.search(1);//to search an element
        stack.pop(); //to remove the topmost element
        stack.peek(); //to see the topmost element
        stack.search(1);//to search an element
        //Since internally it impleaments stack therefore it is thread safe and synchronized means it can be used in multithreaded environment
        //if the environment is multithreaded then it has an overhead due to locking and unlocking of the thread
        //for single threaded environment we prefer to use the linkedlist and impleaments the stack interface using linked list 

        LinkedList<Integer> ls = new LinkedList<>();
        ls.addFirst(1);//stack push() method in linkedlist
        ls.getLast();// stack peek() method in linkedlist
        ls.removeLast();//stack pop() method in linkedlist
        ls.size();

        ArrayList<Integer> arr = new ArrayList<>();
        arr.get(arr.size()-1);//peek() method of stack
        arr.remove(arr.size()-1);//pop() method of stack

    }
}

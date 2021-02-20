import java.util.Stack;


public class StackSorting {
    static void sortedInsertion(Stack<Integer> s, int element){
        if (s.isEmpty() || element >= s.peek()){
            s.push(element);
            return;
        }
        int temp = s.pop();
        sortedInsertion(s, element);
        s.push(temp);
    }
    static void sortStack(Stack<Integer> s){
        if (!s.isEmpty()){
            int temp = s.pop();
            sortStack(s);
            sortedInsertion(s, temp);
        }
    }
    public static void main(String[] args) {
        Stack<Integer> s = new Stack<>();
        s.push(35);
        s.push(5);
        s.push(18);
        s.push(17);
        s.push(4);

        sortStack(s);
    }
}

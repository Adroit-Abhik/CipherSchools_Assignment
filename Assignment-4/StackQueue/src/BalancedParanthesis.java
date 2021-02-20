import java.util.Stack;
import java.util.Scanner;

public class BalancedParanthesis {
    static boolean match(char a, char b){
        return ((a == ')' && b == '(') || (a == '}' && b == '{')
        || (a == ']' && b == '['));
    }
    static boolean isBalanced(String exp){
        Stack<Character> s = new Stack<Character>();
        for(int i=0; i<exp.length(); i++){
            if( exp.charAt(i) == '(' || exp.charAt(i) == '{' || exp.charAt(i) == '['){
                s.push(exp.charAt(i));
            }
            else{
                if (s.isEmpty())
                    return false;
                else if (!match(exp.charAt(i), s.peek()))
                    return false;
                else
                    s.pop();
            }
        }
        return s.isEmpty();
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String exp = sc.next();
        System.out.println(isBalanced(exp));
    }
}

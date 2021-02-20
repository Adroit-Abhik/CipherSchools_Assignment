import java.util.Stack;
import java.lang.*;

class UserStack extends Stack<Integer>{
    Stack<Integer> min = new Stack<>();
    void push(int x){
        if (isEmpty()){
            super.push(x);
            min.push(x);
        }
        else{
            super.push(x);
            int y = min.peek();
            if (x < y)
                min.push(x);
            else
                min.push(y);
        }

    }

    int popEl(){
        int x = super.pop();
        min.pop();
        return x;
    }

    int getMin(){
        int x = min.peek();
        return x;
    }
}

public class StackWithGetMin {
    public static void main(String[] args) {
        UserStack s = new UserStack();
        s.push(10);
        s.push(20);
        s.push(15);
        System.out.println(s.getMin());
        s.push(8);
        System.out.println(s.getMin());
        s.push(20);
    }
}

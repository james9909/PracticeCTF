package machinecode;

public class Machinecode {

    public static void main(String[] args) {
        for(int i=0; i<99; i++) {
            if (i%3==0) {
                System.out.println(args[0]);
            }
        }
    }
}

import java.util.Scanner;

public class P01 {
    public static void main (String[] args) {
        Scanner x = new Scanner(System.in);
        int total = x.nextInt();
        x.nextLine();
        for (int i = 1; i <= total; i++) {
            String name = x.nextLine();
            System.out.println("Hello, " + name +"!" );
        }
    }
} 

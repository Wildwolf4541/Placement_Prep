package dsa.Java;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        System.out.println("Hello World");

        // Input
        Scanner sc = new Scanner(System.in);
        System.out.println("Input Your Age: ");
        int num = sc.nextInt();
        System.out.println(num);

        // Variables
        String sname = "Aman";
        String friend = new String("Akhil");
        int age = 30;
        float pi = 3.14F;
        long phone = 12345678900L;
        char letter = '@';
        boolean isAdult = true;

        final int ageeee = 30; // similar to const

        // String operations
        System.out.println(sname.length());
        System.out.println(sname + " and " + friend);
        System.out.println(sname.charAt(0));
        System.out.println(sname.replace('a', 'b'));
        System.out.println(sname.substring(0, 3)); // 0 included, 3 excluded

        // Math operations
        System.out.println(Math.random());
        System.out.println(Math.min(age, ageeee));

        // Arrays
        int[] marks = new int[4];

        marks[0] = 97;
        marks[1] = 98;
        marks[2] = 99;
        marks[3] = 100;

        // 2D Array
        int[][] finalmarks = {
            {99, 99, 99},
            {99, 100, 100}
        };

        System.out.println(marks.length);

        // Sort array
        Arrays.sort(marks);

        // Print sorted array
        System.out.println(Arrays.toString(marks));

        sc.close();
    }
}
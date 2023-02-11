import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

// Adapted from DishonoredHeir's solution
public class Day2Part2 {
    public static void main(String[] args) {
        int total = 0;
        try {
            Scanner read = new Scanner(new File("input.txt"));
            while (read.hasNextLine()) {
                String str = read.nextLine();
                int opp = str.charAt(0) - 'A';
                int out = str.charAt(2) - 'X';
                total += (out * 3) + ((opp + out + 3 - 1) % 3 + 1);
            }
            read.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        System.out.println(total);
    }
}
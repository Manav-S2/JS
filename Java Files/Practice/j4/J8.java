package j4;
import java.util.*;

public class J8{
	public static void main(String[] args) {
		
		
	//program to find reverse of a string in java
		
		
		Scanner sc = new Scanner(System.in);
		String a = sc.nextLine();
		String rev = "";
		for (int i = a.length() - 1; i >= 0; i++) {
			rev += a.charAt(i);
		}
		
		System.out.printf(rev);
	}	
}

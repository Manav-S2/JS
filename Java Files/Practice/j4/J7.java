////package j4;
////import java.util.Scanner;
////
////
////public class J7 {
////	
////
////    public static void main(String[] args) {
////   Scanner sc = new Scanner(System.in);
////   
////  add(0,8);
////add(2rs0,4);
////   
////    }
////
////   static int add(int a , int b) {
////	   
////	   System.out.println(a);
////	   return 4;
////	   
////   }
////   
////static String add(int a , int b) {
////	   
////	   System.out.println(a);
////	   return "df";
////	   
////   }
////   
////}
//
//
//
//package j4;
//
//public class J7{
//	
//	public static void main(String[] args) {
//	int rows = 3; 
//	int cols = 4;
//	int [][] a = new int[rows][cols];
//
//	a[1][2] = 5;
//	
//System.out.println(a[1][2]);	
//	
//}
//}
//

package j4;
import java.util.Scanner;

public  class J7{
	public static void main (String[] args) {
		
// program to make two matrices using no of rows and cold and values provided 
// by user then finding the sum of the matrices...
		
		Scanner sc  = new Scanner(System.in);
		
		
		
		System.out.print("Enter the no of rows: ");
		int rows = sc.nextInt();
	
		System.out.print("Enter the no of cols: ");
		int cols = sc.nextInt();
		
		int[][] matrix1 = new int[rows][cols];
		int[][] matrix2 = new int[rows][cols];
		for (int i = 0; i < rows; i++) {
			for (int j =0; j< cols; j++) {
				matrix1[i][j] = sc.nextInt();
			}
		}
		
		for (int i = 0; i < rows; i++) {
			for (int j =0; j< cols; j++) {
				matrix2[i][j] = sc.nextInt();
			}
		}
		
		
		
		int[][] sumMatrix = new int[rows][cols];
		
		for (int i = 0; i < rows; i++) {
			for (int j = 0; j < cols; j++) {
				sumMatrix[i][j] = matrix1[i][j] + matrix2[i][j];
			}
		}
		
		
		for (int[] i: sumMatrix) {
			for (int j : i) {
				System.out.println(j + " ");
			}
			System.out.println();
		}
	
	
				}
}




















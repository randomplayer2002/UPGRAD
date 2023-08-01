import java.util.Arrays;
import java.io.*;
import java.util.*;
import java.util.Scanner;
class Source{
    public static boolean  isHeap(int[] arr,  int n){

    // Start from the root and go up to the last internal node
    
    for (int i=0; i<=(n-2)/2; i++){
        // If left child is greater, return false
        if ((2*i + 2)<n && arr[2*i +1] > arr[i])
                return false;
         // If right child is greater, return false
        if ((2*i + 2)<n && arr[2*i+2] > arr[i])
                return false;
    }
    return true;
}
public static int[] getArrayInput(int size, Scanner scanner) {
       int array[] = new int[size];
       for (int i = 0; i < size; i++) {
           array[i] = scanner.nextInt();
       }
       return array;
   }

	public static void main (String[] args) {
	 Scanner scanner = new Scanner(System.in);
       int sizeArray1 = scanner.nextInt();
       int arr[] = getArrayInput(sizeArray1, scanner);
	    int n = arr.length;
	    String x = isHeap(arr, n)? "YES": "NO";
 
		System.out.println(x);
	}	
}

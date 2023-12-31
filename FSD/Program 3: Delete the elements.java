import java.util.*;

public class Source {
    public static void main(String args[]) {
        Queue<Integer> queue = new LinkedList<Integer>();
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        while (n-- > 0)
            queue.add(s.nextInt());
        deleteSecondHalf(queue);
    }

    // Method to delete the second half of the elements and print the remaining elements
    static void deleteSecondHalf(Queue<Integer> queue) {
        int n = queue.size();
        int temp = n - n / 2;
        // Removing the first ceil(n/2) elements of the queue and adding back to the same queue
        for (int i = 0; i < temp; i++)
            queue.add(queue.remove());
        // Removing the end floor(n/2) elements of the original queue
        for (int i = 0; i < n / 2; i++)
            queue.remove();
        // Printing the remaining elements
        System.out.println(queue);
    }
}

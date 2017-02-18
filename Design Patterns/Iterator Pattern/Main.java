
public class Main {

	public static void main(String[] args) {
		LinkedList<Integer> list = new LinkedList<Integer>();

		list.addToEnd(1);
		list.addToEnd(3);
		list.addToEnd(5);
		list.addToEnd(7);
		list.addToEnd(9);
		list.addToFront(2);
		list.addToFront(4);
		list.addToFront(6);
		list.addToFront(8);

		for (Iterator<Integer> iter = list.getIterator(); iter.hasNext();) {
			System.out.print(iter.next() + " ");
		}
		System.out.println("\nLength: " + list.size());

		list.removeFromFront();
		list.removeFromFront();
		list.removeFromFront();
		list.removeFromFront();
		list.removeFromFront();

		for (Iterator<Integer> iter = list.getIterator(); iter.hasNext();) {
			System.out.print(iter.next() + " ");
		}
		System.out.println("\nLength: " + list.size());

		Iterator<Integer> iter = list.find(5);
		for (; iter.hasNext();) {
			System.out.print(iter.next() + " ");
		}
		System.out.println("\nLength: " + list.size());

	}
}

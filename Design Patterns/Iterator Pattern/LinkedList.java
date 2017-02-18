
public class LinkedList<T> implements Container {

	private Node list;
	private Node end;
	private int length;

	@Override
	public Iterator<T> getIterator() {
		return new NodeIterator();
	}

	public void addToFront(T data) {
		length++;
		if (list == null) {
			list = new Node(data);
			end = list;
		} else {
			Node n = new Node(data);
			n.next = list;
			list = n;
		}
	}

	public void addToEnd(T data) {
		length++;
		if (end == null) {
			end = new Node(data);
			list = end;
		} else {
			end.next = new Node(data);
			end = end.next;
		}
	}

	public void removeFromFront() {
		if (list != null) {
			length--;
			list = list.next;
		}
	}

	// Returns an iterator to the element after the first matching item
	public Iterator<T> find(T item) {
		Iterator<T> iter = this.getIterator();
		while (iter.hasNext()) {
			if (item.equals(iter.next())) {
				return iter;
			}
		}
		return null;
	}

	public int size() {
		return length;
	}

	private class Node {
		private T data;
		private Node next;

		public Node(T data) {
			this.data = data;
		}
	}

	private class NodeIterator implements Iterator<T> {

		private Node current;

		public NodeIterator() {
			current = list;
		}

		@Override
		public boolean hasNext() {
			return current != null;
		}

		@Override
		public T next() {
			if (this.hasNext()) {
				T temp = current.data;
				current = current.next;
				return temp;
			}
			return null;
		}

	}

}

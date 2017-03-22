import java.util.ArrayList;
import java.util.List;

public class CareTaker {
	List<Memento> mementos = new ArrayList<>();

	public void add(Memento source) {
		mementos.add(source);
	}

	public Memento pop() {
		if (!mementos.isEmpty()) {
			Memento temp = mementos.get(mementos.size() - 1);
			mementos.remove(mementos.size() - 1);
			return temp;
		}
		return null;
	}

}

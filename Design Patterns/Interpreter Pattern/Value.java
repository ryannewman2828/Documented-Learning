
public class Value implements Expression{

	private int value;
	
	public Value(int value) {
		this.value = value;
	}

	@Override
	public int interpret() {
		return value;
	}

	@Override
	public void set(String name, int value) {
		// Do nothing
	}

	@Override
	public String print() {
		return value + "";
	}

}


public class Variable implements Expression {

	private String name;
	private int value = 0;

	public Variable(String name) {
		this.name = name;
	}

	@Override
	public int interpret() {
		return value;
	}

	@Override
	public void set(String name, int value) {
		if (this.name.equals(name)) {
			this.value = value;
		}
	}

	@Override
	public String print() {
		return name;
	}

}

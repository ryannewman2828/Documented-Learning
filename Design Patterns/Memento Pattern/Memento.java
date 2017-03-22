
public class Memento {

	private String equation;
	private String result;

	public Memento(String equation, String result) {
		this.equation = equation;
		this.result = result;
	}

	public String getEquation() {
		return equation;
	}

	public String getResult() {
		return result;
	}
}

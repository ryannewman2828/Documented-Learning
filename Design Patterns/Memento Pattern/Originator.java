
public class Originator {

	private String equation;
	private String result;

	public void setEquation(String equation) {
		this.equation = equation;
	}

	public void setResult(String result) {
		this.result = result;
	}

	public String getEquation() {
		return equation;
	}

	public String getResult() {
		return result;
	}

	public Memento saveCalculation() {
		return new Memento(equation, result);
	}

	public void restore(Memento source) {
		equation = source.getEquation();
		result = source.getResult();
	}

}

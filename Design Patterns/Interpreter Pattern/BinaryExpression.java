
public class BinaryExpression implements Expression {

	private String operand;
	private Expression expr1;
	private Expression expr2;
	
	public BinaryExpression(String operand, Expression expr1, Expression expr2) {
		this.operand = operand;
		this.expr1 = expr1;
		this.expr2 = expr2;
	}

	@Override
	public int interpret() {
		switch (operand) {
		case "+":
			return expr2.interpret() + expr1.interpret();
		case "-":
			return expr2.interpret() - expr1.interpret();
		case "*":
			return expr2.interpret() * expr1.interpret();
		case "/":
			return expr2.interpret() / expr1.interpret();
		case "%":
			return expr2.interpret() % expr1.interpret();
		case "&&":
			return (expr2.interpret() != 0 && expr1.interpret() != 0) ? 1 : 0;
		case "||":
			return (expr2.interpret() != 0 || expr1.interpret() != 0) ? 1 : 0;
		default:
			return 0;
		}
	}

	@Override
	public void set(String name, int value) {
		expr1.set(name, value);
		expr2.set(name, value);
	}

	@Override
	public String print() {
		return "(" + expr2.print() + " " + operand + " " + expr1.print() + ")";
	}

}

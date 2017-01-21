
public class UnaryExpression implements Expression {

	private String operand;
	private Expression expr;
	
	public UnaryExpression(String operand, Expression expr) {
		this.operand = operand;
		this.expr = expr;
	}

	@Override
	public int interpret() {
		switch (operand) {
		case "!":
			return (expr.interpret() == 0) ? 1 : 0;
		default:
			return 0;
		}
	}

	@Override
	public void set(String name, int value) {
		expr.set(name, value);
	}

	@Override
	public String print() {
		return operand + "(" + expr.print() + ")";
	}

}

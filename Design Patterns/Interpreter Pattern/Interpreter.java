import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Scanner;

public class Interpreter {
	public static void main(String[] args) throws FileNotFoundException {
		
		File file = new File("src/input.txt");
		
		Scanner sc = new Scanner(file);
		Deque<Expression> stack = new ArrayDeque<>();
		Expression expr;

		while (sc.hasNext()) {
			String line = sc.next();
			if (line.equals("+") || line.equals("-") || line.equals("*") || line.equals("/") || line.equals("%")
					|| line.equals("||") || line.equals("&&")) {
				stack.push(new BinaryExpression(line, stack.pop(), stack.pop()));
			} else if (line.equals("!")) {
				stack.push(new UnaryExpression(line, stack.pop()));
			} else if (isInteger(line)) {
				stack.push(new Value(Integer.parseInt(line)));
			} else {
				stack.push(new Variable(line));
			}
		}

		expr = stack.pop();
		System.out.println(expr.print());
		sc.close();
		file = new File("src/instruction.txt");
		sc = new Scanner(file);

		while (sc.hasNext()) {
			String line = sc.next();
			if (line.equals("eval")) {
				System.out.println(expr.interpret());
			} else if (line.equals("set")) {
				String a, b;
				a = sc.next();
				b = sc.next();
				expr.set(a, Integer.parseInt(b));
				System.out.println("Variable " + a + " has been set");
			}
		}
		sc.close();
	}

	public static boolean isInteger(String s) {
		try {
			Integer.parseInt(s);
		} catch (NumberFormatException e) {
			return false;
		} catch (NullPointerException e) {
			return false;
		}
		return true;
	}
}
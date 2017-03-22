import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.util.*;

public class JavaCalculator extends JFrame {
	private Originator originator;
	private CareTaker careTaker;

	private JButton[] numButtons = new JButton[10];
	private JButton jbtAdd;
	private JButton jbtSubtract;
	private JButton jbtMultiply;
	private JButton jbtDivide;
	private JButton jbtSolve;
	private JButton jbtClear;
	private JButton jbtRevert;
	private JTextField jtfResult;
	private JTextField jtfEqn;
	private int curNum;
	private int curTotal;
	private String prevSymbol;

	private String display = "";
	private String equation = "";

	public JavaCalculator() {
		curNum = 0;
		prevSymbol = "";
		JPanel p1 = new JPanel();
		p1.setLayout(new GridLayout(4, 3));

		for (int i = 1; i < numButtons.length; i++) {
			numButtons[i] = new JButton(i + "");
			p1.add(numButtons[i]);
		}
		numButtons[0] = new JButton("0");
		p1.add(numButtons[0]);
		jbtClear = new JButton("C");
		p1.add(jbtClear);
		jbtRevert = new JButton("Z");
		p1.add(jbtRevert);

		JPanel p2 = new JPanel();
		p2.setLayout(new FlowLayout());
		jtfResult = new JTextField(20);
		jtfResult.setHorizontalAlignment(JTextField.RIGHT);
		jtfResult.setEditable(false);
		p2.add(jtfResult);
		jtfEqn = new JTextField(20);
		jtfEqn.setHorizontalAlignment(JTextField.LEFT);
		jtfEqn.setEditable(false);
		p2.add(jtfEqn);

		JPanel p3 = new JPanel();
		p3.setLayout(new GridLayout(5, 1));
		jbtAdd = new JButton("+");
		p3.add(jbtAdd);
		jbtSubtract = new JButton("-");
		p3.add(jbtSubtract);
		jbtMultiply = new JButton("*");
		p3.add(jbtMultiply);
		jbtDivide = new JButton("/");
		p3.add(jbtDivide);
		jbtSolve = new JButton("=");
		p3.add(jbtSolve);

		JPanel p = new JPanel();
		p.setLayout(new GridLayout());
		p.add(p2, BorderLayout.NORTH);
		p.add(p1, BorderLayout.SOUTH);
		p.add(p3, BorderLayout.EAST);

		add(p);

		for (int i = 0; i < numButtons.length; i++) {
			numButtons[i].addActionListener(new NumListener(i));
		}

		jbtAdd.addActionListener(new MiscListener("+"));
		jbtSubtract.addActionListener(new MiscListener("-"));
		jbtMultiply.addActionListener(new MiscListener("*"));
		jbtDivide.addActionListener(new MiscListener("/"));
		jbtSolve.addActionListener(new MiscListener("="));
		jbtClear.addActionListener(new MiscListener("c"));
		jbtRevert.addActionListener(new MiscListener("z"));

		originator = new Originator();
		careTaker = new CareTaker();

	}

	class NumListener implements ActionListener {
		private int num;

		public NumListener(int num) {
			this.num = num;
		}

		@Override
		public void actionPerformed(ActionEvent e) {
			curNum *= 10;
			curNum += num;
			display = jtfResult.getText();
			jtfResult.setText(display + num);
		}
	}

	class MiscListener implements ActionListener {
		private String symbol;

		public MiscListener(String symbol) {
			this.symbol = symbol;
		}

		@Override
		public void actionPerformed(ActionEvent e) {
			if (symbol.equals("=")) {
				switch (prevSymbol) {
				case "+":
					curTotal += curNum;
					break;
				case "-":
					curTotal -= curNum;
					break;
				case "*":
					curTotal *= curNum;
					break;
				case "/":
					curTotal /= curNum;
					break;
				default:
					break;
				}
				originator.setEquation(jtfResult.getText());
				jtfEqn.setText(curTotal + "");
				originator.setResult(jtfEqn.getText());
				jtfResult.setText("");
				curNum = 0;
				curTotal = 0;
				prevSymbol = "";
				careTaker.add(originator.saveCalculation());
			} else if (symbol.equals("c")) {
				jtfResult.setText("");
				jtfEqn.setText("");
				curNum = 0;
				curTotal = 0;
				prevSymbol = "";
			} else if (symbol.equals("z")) {
				originator.restore(careTaker.pop());
				jtfResult.setText(originator.getEquation());
				jtfEqn.setText(originator.getResult());
				curNum = 0;
				curTotal = Integer.parseInt(jtfEqn.getText());
				prevSymbol = "z";
			} else {
				display = jtfResult.getText();
				jtfResult.setText(display + " " + symbol + " ");
				switch (prevSymbol) {
				case "+":
					curTotal += curNum;
					break;
				case "-":
					curTotal -= curNum;
					break;
				case "*":
					curTotal *= curNum;
					break;
				case "/":
					curTotal /= curNum;
					break;
				case "z":
					break;
				default:
					curTotal = curNum;
					break;
				}
				curNum = 0;
				prevSymbol = symbol;
			}
		}

	}

	public static void main(String[] args) {
		JavaCalculator calc = new JavaCalculator();
		calc.pack();
		calc.setLocationRelativeTo(null);
		calc.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		calc.setVisible(true);
	}

}

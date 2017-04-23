import java.awt.*;
import java.awt.event.*;

import javax.script.ScriptEngine;
import javax.script.ScriptEngineManager;
import javax.script.ScriptException;
import javax.swing.*;

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
	private JTextField jtfEquation;
	private JTextField jtfResult;
	private String equation;

	public JavaCalculator() {
		equation = "";
		JPanel p1 = new JPanel();
		JPanel p2 = new JPanel();
		JPanel p3 = new JPanel();
		
		// Initialize the middle column of buttons
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

		// Initialize the text fields
		p2.setLayout(new FlowLayout());
		jtfEquation = new JTextField(20);
		jtfEquation.setHorizontalAlignment(JTextField.RIGHT);
		jtfEquation.setEditable(false);
		p2.add(jtfEquation);
		jtfResult = new JTextField(20);
		jtfResult.setHorizontalAlignment(JTextField.LEFT);
		jtfResult.setEditable(false);
		p2.add(jtfResult);

		// Initialize the right column of buttons
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

		
		// Setup the listeners
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

		// Initialize memento objects
		originator = new Originator();
		careTaker = new CareTaker();

	}

	private String interpret() {
		ScriptEngineManager mgr = new ScriptEngineManager();
		ScriptEngine engine = mgr.getEngineByName("JavaScript");
		try {
			return engine.eval(equation).toString();
		} catch (ScriptException e) {
			e.printStackTrace();
			return null;
		}
	}

	class NumListener implements ActionListener {
		private int num;

		public NumListener(int num) {
			this.num = num;
		}

		@Override
		public void actionPerformed(ActionEvent e) {
			equation += num;
			jtfEquation.setText(equation);
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
				if (!equation.equals("")) {
					originator.setEquation(equation);
					jtfResult.setText(interpret());
					originator.setResult(jtfResult.getText());
					jtfEquation.setText("");
					equation = "";
					careTaker.add(originator.saveCalculation());
				}
			} else if (symbol.equals("c")) {
				jtfEquation.setText("");
				jtfResult.setText("");
				equation = "";
			} else if (symbol.equals("z")) {
				originator.restore(careTaker.pop());
				equation = originator.getEquation();
				jtfEquation.setText(equation);
				jtfResult.setText(originator.getResult());
			} else {
				equation += " " + symbol + " ";
				jtfEquation.setText(equation);
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

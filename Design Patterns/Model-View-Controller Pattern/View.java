import java.awt.Color;
import java.awt.Container;
import java.awt.Dimension;
import java.awt.Graphics;

import javax.swing.JFrame;
import javax.swing.JPanel;

public class View extends JFrame implements Observer {
	public static final int CANVAS_WIDTH = 1280;
	public static final int CANVAS_HEIGHT = 960;
	private int blockWidth;
	private int blockHeight;
	private int horizontalDisp;
	private int verticalDisp;
	private Color colour;

	private DrawCanvas canvas;

	public View() {
		canvas = new DrawCanvas();
		canvas.setPreferredSize(new Dimension(CANVAS_WIDTH, CANVAS_HEIGHT));

		Container cp = getContentPane();
		cp.add(canvas);

		setDefaultCloseOperation(EXIT_ON_CLOSE);
		pack();
		setTitle("Model-View-Controller");
		setVisible(true);
	}

	private class DrawCanvas extends JPanel {

		@Override
		public void paintComponent(Graphics g) {
			super.paintComponent(g);
			setBackground(Color.BLACK);
			g.setColor(colour);
			g.fillRect(horizontalDisp, verticalDisp, blockWidth, blockHeight);
		}
	}

	private void print() {
		canvas.paintComponent(getGraphics());
	}

	@Override
	public void notify(UpdateInfo info) {
		blockWidth = info.blockWidth;
		blockHeight = info.blockHeight;
		horizontalDisp = info.horizontalDisp;
		verticalDisp = info.verticalDisp;
		colour = info.colour;
		print();
	}
}

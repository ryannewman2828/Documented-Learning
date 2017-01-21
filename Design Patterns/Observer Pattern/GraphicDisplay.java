import java.awt.*; 
import java.util.ArrayList;
import java.util.List;

import javax.swing.*;


public class GraphicDisplay extends JFrame implements Observer {
	public static final int CANVAS_WIDTH = 1280;
	public static final int CANVAS_HEIGHT = 960;
	private int blockWidth;
	private int blockHeight;

	private DrawCanvas canvas;

	private List<List<Boolean>> theDisplay;
	private final int gridSize;

	public GraphicDisplay(int n) {

		theDisplay = new ArrayList<>();
		gridSize = n;
		blockWidth = CANVAS_WIDTH / n;
		blockHeight = CANVAS_HEIGHT / n;
		for (int i = 0; i < gridSize; i++) {
			theDisplay.add(new ArrayList<>());
			for (int j = 0; j < gridSize; j++) {
				theDisplay.get(i).add(false);
			}
		}
		
		canvas = new DrawCanvas();
		canvas.setPreferredSize(new Dimension(CANVAS_WIDTH, CANVAS_HEIGHT));

		Container cp = getContentPane();
		cp.add(canvas);

		setDefaultCloseOperation(EXIT_ON_CLOSE);
		pack();
		setTitle("Observer Pattern");
		setVisible(true);
	}

	public void print(){
		canvas.paintComponent(getGraphics());
	}
	
	private class DrawCanvas extends JPanel {

		@Override
		public void paintComponent(Graphics g) {
			super.paintComponent(g);
			setBackground(Color.BLACK);
			
			g.setColor(Color.WHITE);
			for (int i = 0; i < gridSize; i++) {
				for (int j = 0; j < gridSize; j++) {
					if (theDisplay.get(i).get(j)) {
						g.fillRect(j * blockWidth, i * blockHeight, blockWidth, blockHeight);
					}
				}
			}
		}
	}

	@Override
	public void notify(Subject whoNotified) {
		if(whoNotified.getInfo().active){
			theDisplay.get(whoNotified.getInfo().row).set(whoNotified.getInfo().col, true);
		} else {
			theDisplay.get(whoNotified.getInfo().row).set(whoNotified.getInfo().col, false);
		}
	}
}
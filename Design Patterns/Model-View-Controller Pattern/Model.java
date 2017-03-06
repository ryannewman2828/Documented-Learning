import java.awt.Color;
import java.util.ArrayList;
import java.util.List;

public class Model {
	private final int SCALE = 10;
	public List<Observer> views;
	private int blockWidth;
	private int blockHeight;
	private int horizontalDisp;
	private int verticalDisp;
	private int colourNum;
	private Color colour;

	public Model() {
		views = new ArrayList<>();
		blockWidth = 50;
		blockHeight = 50;
		horizontalDisp = 100;
		verticalDisp = 100;
		colour = Color.WHITE;
	}

	public void verticalMove(int direction) {
		verticalDisp += SCALE * direction;
		notifyViews();
	}

	public void horizontalMove(int direction) {
		horizontalDisp += SCALE * direction;
		notifyViews();
	}

	public void scaleHeight(int direction) {
		if (blockHeight > SCALE)
			blockHeight += SCALE * direction;
		notifyViews();
	}

	public void scaleWidth(int direction) {
		if (blockWidth > SCALE)
			blockWidth += SCALE * direction;
		notifyViews();
	}

	public void toggleColour() {
		colourNum++;
		colourNum %= 4;
		switch (colourNum) {
		case 0:
			colour = Color.WHITE;
			break;
		case 1:
			colour = Color.BLUE;
			break;
		case 2:
			colour = Color.RED;
			break;
		case 3:
			colour = Color.GREEN;
			break;
		default:
			break;
		}
		notifyViews();
	}

	public void attach(Observer view) {
		views.add(view);
		notifyViews(); // Init the views
	}

	private void notifyViews() {
		for (Observer v : views) {
			v.notify(new UpdateInfo(blockWidth, blockHeight, horizontalDisp, verticalDisp, colour));
		}
	}

}

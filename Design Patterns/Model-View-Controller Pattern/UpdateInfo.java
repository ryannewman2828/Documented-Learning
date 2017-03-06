import java.awt.Color;

// Class to easily and quickly transfer variables
public class UpdateInfo {
	public int blockWidth;
	public int blockHeight;
	public int horizontalDisp;
	public int verticalDisp;
	public Color colour;

	public UpdateInfo(int bw, int bh, int hd, int vd, Color c) {
		blockWidth = bw;
		blockHeight = bh;
		horizontalDisp = hd;
		verticalDisp = vd;
		colour = c;
	}
}

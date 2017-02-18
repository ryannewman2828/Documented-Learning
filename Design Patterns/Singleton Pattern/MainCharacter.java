
public class MainCharacter {

	private static MainCharacter instance = new MainCharacter();

	private int x;
	private int y;
	
	private MainCharacter() {
		x = 0;
		y = 0;
	}

	public static MainCharacter getCharacterInstance() {
		return instance;
	}

	public int getX() {
		return x;
	}

	public int getY() {
		return y;
	}

	public void move(int x, int y) {
		this.x = x;
		this.y = y;
	}

}

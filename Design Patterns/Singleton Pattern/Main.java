
public class Main {

	public static void main(String[] args) {
		MainCharacter mainCharacter = MainCharacter.getCharacterInstance();
		
		mainCharacter.move(100, 100);
		System.out.println("X: " + mainCharacter.getX() + ", Y: " + mainCharacter.getY());
		
		MainCharacter mainCharacter2 = MainCharacter.getCharacterInstance();
		mainCharacter2.move(200, 200); // Moves the second instance
		
		// Prints from the first instance
		System.out.println("X: " + mainCharacter.getX() + ", Y: " + mainCharacter.getY());
	}

}

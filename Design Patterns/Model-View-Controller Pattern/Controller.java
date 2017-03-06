import java.util.Scanner;

public class Controller {

	private Scanner sc;
	private View view;
	private Model model;

	public Controller() {
		sc = new Scanner(System.in);
		view = new View();
		model = new Model();
		model.attach(view);
	}

	public void gatherInput() {
		while (sc.hasNextLine()) {
			String input = sc.next();
			switch (input) {
			case "up":
				model.verticalMove(-1);
				break;
			case "down":
				model.verticalMove(1);
				break;
			case "left":
				model.horizontalMove(-1);
				break;
			case "right":
				model.horizontalMove(1);
				break;
			case "grow":
				model.scaleHeight(1);
				break;
			case "shrink":
				model.scaleHeight(-1);
				break;
			case "fat":
				model.scaleWidth(1);
				break;
			case "skinny":
				model.scaleWidth(-1);
				break;
			case "colour":
				model.toggleColour();
				break;
			default:
				break;
			}
		}
	}

}

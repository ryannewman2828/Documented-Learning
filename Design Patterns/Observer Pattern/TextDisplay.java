import java.util.ArrayList;
import java.util.List;

public class TextDisplay implements Observer{

	private List<List<Character>> theDisplay;
	private final int gridSize;
	
	public TextDisplay(int n){
		theDisplay = new ArrayList<>();
		gridSize = n;
		for (int i = 0; i < gridSize; i++) {
			theDisplay.add(new ArrayList<>());
			for (int j = 0; j < gridSize; j++) {
				theDisplay.get(i).add('_');
			}
		}
	}
	
	public void print(){
		for (int i = 0; i < gridSize; i++) {
			for (int j = 0; j < gridSize; j++) {
				System.out.print(theDisplay.get(i).get(j));
			}
			System.out.println();
		}
	}

	@Override
	public void notify(Subject whoNotified) {
		if(whoNotified.getInfo().isOn){
			theDisplay.get(whoNotified.getInfo().row).set(whoNotified.getInfo().col, 'X');
		} else {
			theDisplay.get(whoNotified.getInfo().row).set(whoNotified.getInfo().col, '_');
		}
	}

	@Override
	public Subscription subType() {
		return Subscription.All;
	}

}

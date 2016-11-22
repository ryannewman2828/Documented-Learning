import java.util.ArrayList;
import java.util.List;

public class Grid {

	private List<List<Cell>> theGrid;
	private int gridSize;
	private TextDisplay td;
	private boolean active;
	
	public Grid() {
		active = false;
		theGrid = new ArrayList<>();
	}
	
	public boolean isWon(){
		for (int i = 0; i < gridSize; i++) {
			for (int j = 0; j < gridSize; j++) {
				if(theGrid.get(i).get(j).getState()){ 
					return false;
				}
			}
		}
		return true;
	}
	
	public void init(int n){
		if(active){
			clearGrid();
		}
		active = true;
		gridSize = n;
		for (int i = 0; i < gridSize; i++) {
			theGrid.add(new ArrayList<>());
			for (int j = 0; j < gridSize; j++) {
				theGrid.get(i).add(new Cell());
				theGrid.get(i).get(j).setCoords(i, j);
			}
		}
		td = new TextDisplay(n);
		for (int i = 0; i < gridSize; i++) {
			for (int j = 0; j < gridSize; j++) {
				theGrid.get(i).get(j).attach(td);
				if(j > 0){
					theGrid.get(i).get(j).attach(theGrid.get(i).get(j - 1));
				}
				if(j < gridSize - 1){
					theGrid.get(i).get(j).attach(theGrid.get(i).get(j + 1));
				}
				if(i > 0){
					theGrid.get(i).get(j).attach(theGrid.get(i - 1).get(j));
				}
				if(i < gridSize - 1){
					theGrid.get(i).get(j).attach(theGrid.get(i + 1).get(j));
				}
			}
		}
	}
	
	public void turnOn(int row, int col){
		theGrid.get(row).get(col).setOn();
	}
	
	public void toggle(int row, int col){
		theGrid.get(row).get(col).toggle();
	}
	
	public void init(int row, int col){
		turnOn(row, col);
	}
	
	public void print(){
		td.print();
	}
	
	private void clearGrid(){
		theGrid.clear();
	}
	
}
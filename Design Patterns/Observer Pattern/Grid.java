import java.util.ArrayList;
import java.util.List;

public class Grid {

	private List<List<Cell>> theGrid;
	private List<Cell> watching;
	private int gridSize;
	private TextDisplay td;
	
	public Grid() {
		theGrid = new ArrayList<>();
		watching = new ArrayList<>();
	}
	
	public void init(int n){
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
				if(j - 1 >= 0){
					if(i - 1 >= 0){
						theGrid.get(i).get(j).attach(theGrid.get(i - 1).get(j - 1));
					}
					if(i + 1 < theGrid.get(j).size()){
						theGrid.get(i).get(j).attach(theGrid.get(i + 1).get(j - 1));
					}
					theGrid.get(i).get(j).attach(theGrid.get(i).get(j - 1));
				}
				if(j + 1 < theGrid.size()){
					if(i - 1 >= 0){
						theGrid.get(i).get(j).attach(theGrid.get(i - 1).get(j + 1));
					}
					if(i + 1 < theGrid.get(j).size()){
						theGrid.get(i).get(j).attach(theGrid.get(i + 1).get(j + 1));
					}
					theGrid.get(i).get(j).attach(theGrid.get(i).get(j + 1));
				}
				if(i - 1 >= 0){
					theGrid.get(i).get(j).attach(theGrid.get(i - 1).get(j));
				}
				if(i + 1 < theGrid.get(j).size()){
					theGrid.get(i).get(j).attach(theGrid.get(i + 1).get(j));
				}
			}
		}
	}
	
	public void step(){
		for (Cell w : watching){
			w.step();
		}
		int size = watching.size();
		for (int i = 0; i < size; i++) {
			updateWatching(watching.get(i));
		}
		watching.removeIf(e -> e.noNeighbours());
		finalize();
	}
	
	public void finalize(){
		for (Cell w: watching){
			w.finalize();
		}
	}
	
	public void turnOn(int row, int col){
		theGrid.get(row).get(col).setOn();
		watching.add(theGrid.get(row).get(col));
		updateWatching(theGrid.get(row).get(col));
	}
	
	public void toggle(int row, int col){
		theGrid.get(row).get(col).toggle();
		watching.add(theGrid.get(row).get(col));
		updateWatching(theGrid.get(row).get(col));
	}
	
	public void print(){
		td.print();
	}
	
	private void updateWatching(Cell c){
		int row = c.getInfo().row;
		int col = c.getInfo().col;
		if(row - 1 >= 0){
			if(col - 1 >= 0){
				if(!(theGrid.get(row - 1).get(col - 1).noNeighbours() || watching.contains(theGrid.get(row - 1).get(col - 1)))){
					watching.add(theGrid.get(row - 1).get(col - 1));
				}
			}
			if(col + 1 < theGrid.get(row).size()){
				if(!(theGrid.get(row - 1).get(col + 1).noNeighbours() || watching.contains(theGrid.get(row - 1).get(col + 1)))){
					watching.add(theGrid.get(row - 1).get(col + 1));
				}
			}
			if(!(theGrid.get(row - 1).get(col).noNeighbours() || watching.contains(theGrid.get(row - 1).get(col)))){
				watching.add(theGrid.get(row - 1).get(col));
			}
		}
		if(row + 1 < theGrid.size()){
			if(col - 1 >= 0){
				if(!(theGrid.get(row + 1).get(col - 1).noNeighbours() || watching.contains(theGrid.get(row + 1).get(col - 1)))){
					watching.add(theGrid.get(row + 1).get(col - 1));
				}
			}
			if(col + 1 < theGrid.get(row).size()){
				if(!(theGrid.get(row + 1).get(col + 1).noNeighbours() || watching.contains(theGrid.get(row + 1).get(col + 1)))){
					watching.add(theGrid.get(row + 1).get(col + 1));
				}
			}
			if(!(theGrid.get(row + 1).get(col).noNeighbours() || watching.contains(theGrid.get(row + 1).get(col)))){
				watching.add(theGrid.get(row + 1).get(col));
			}
		}
		if(col - 1 >= 0){
			if(!(theGrid.get(row).get(col - 1).noNeighbours() || watching.contains(theGrid.get(row).get(col - 1)))){
				watching.add(theGrid.get(row).get(col - 1));
			}
		}
		if(col + 1 < theGrid.get(row).size()){
			if(!(theGrid.get(row).get(col + 1).noNeighbours() || watching.contains(theGrid.get(row).get(col + 1)))){
				watching.add(theGrid.get(row).get(col + 1));
			}
		}
	}
}
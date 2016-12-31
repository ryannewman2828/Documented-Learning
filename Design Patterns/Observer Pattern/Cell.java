public class Cell extends Subject implements Observer {
	
	private int row, col;
	private byte onNeighbours;
	private boolean active;
	
	private byte tempNeighbours;
	
	public Cell(){
		super();
		row = 0;
		col = 0;
		active = false;
	}

	public boolean getState(){
		return active;
	}
	
	public void setOn(){
		active = true;
		notifyObservers();
	}
	
	public void toggle(){
		active = !active;
		notifyObservers();
	}
	
	public void setCoords(int row, int col){
		this.row = row;
		this.col = col;
	}
	
	public void step(){
		if (active){
			if(onNeighbours != 2 && onNeighbours != 3){
				toggle();
			}
		} else {
			if(onNeighbours == 3){
				toggle();
			}
		}
	}
	
	public void finalize(){
		onNeighbours = tempNeighbours;
	}
	
	public boolean noNeighbours(){
		return tempNeighbours == 0;
	}
	
	@Override
	public void notify(Subject whoNotified) {
		if(whoNotified.getInfo().active){
			tempNeighbours++;
		} else {
			tempNeighbours--;
		}
	}
	
	@Override
	public Info getInfo() {
		return new Info(row, col, active);
	}
}

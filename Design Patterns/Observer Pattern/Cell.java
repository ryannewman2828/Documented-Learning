public class Cell extends Subject implements Observer {
	
	private int row, col;
	private boolean isOn;
	
	public Cell(){
		super();
		row = 0;
		col = 0;
		isOn = false;
	}

	public boolean getState(){
		return isOn;
	}
	
	public void setOn(){
		isOn = true;
		notifyObservers(Subscription.All);
	}
	
	public void toggle(){
		isOn = !isOn;
		notifyObservers(Subscription.SwitchOnly);
		notifyObservers(Subscription.All);
	}
	
	public void setCoords(int row, int col){
		this.row = row;
		this.col = col;
	}
	
	@Override
	public void notify(Subject whoNotified) {
		isOn = !isOn;
		notifyObservers(Subscription.All);
	}
	
	@Override
	public Subscription subType() {
		return Subscription.SwitchOnly;
	}

	@Override
	public Info getInfo() {
		return new Info(row, col, isOn);
	}
}

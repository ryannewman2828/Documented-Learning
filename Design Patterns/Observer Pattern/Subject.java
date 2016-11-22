import java.util.ArrayList;
import java.util.List;

public abstract class Subject {
	
	private List<Observer> observers;
	
	public Subject(){
		observers = new ArrayList<>();
	}
	
	public abstract Info getInfo();
	
	public void attach(Observer o){
		observers.add(o);
	}
	
	public void notifyObservers(Subscription t){
		for(Observer o: observers){
			if(o.subType() == t){
				o.notify(this);
			}
		}
	}
}

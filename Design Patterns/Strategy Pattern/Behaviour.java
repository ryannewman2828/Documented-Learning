import robocode.*;

public interface Behaviour {
	public void moveCommand();
	public void attackCommand(ScannedRobotEvent e);
	public void bulletHitCommand();
	public void wallHitCommand();
	public void robotHitCommand(HitRobotEvent e);
}

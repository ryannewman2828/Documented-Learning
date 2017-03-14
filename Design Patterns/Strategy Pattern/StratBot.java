import java.util.ArrayList;
import java.util.List;

import robocode.*;

public class StratBot extends AdvancedRobot {

	private List<Behaviour> strategies = new ArrayList<>();
	private int index;

	public void run() {
		index = 0;
		strategies.add(new OffensiveBehaviour(this));
		strategies.add(new DefensiveBehaviour(this));
		strategies.add(new FleeBehaviour(this));

		// Robot main loop
		while (true) {
			strategies.get(index).moveCommand();
			if (getEnergy() <= 25) {
				index = 2; // Enter Fleeing mode
			} else if (getOthers() > 10) {
				index = 1; // Enter Defensive mode
			} else {
				index = 0; // Enter Offensive mode
			}
		}
	}

	public void onScannedRobot(ScannedRobotEvent e) {
		strategies.get(index).attackCommand(e);
	}

	public void onHitByBullet(HitByBulletEvent e) {
		strategies.get(index).bulletHitCommand();
	}

	public void onHitWall(HitWallEvent e) {
		strategies.get(index).wallHitCommand();
	}

	public void onHitRobot(HitRobotEvent e) {
		strategies.get(index).robotHitCommand(e);
	}
}

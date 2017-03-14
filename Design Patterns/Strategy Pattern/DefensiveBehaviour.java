import robocode.*;

public class DefensiveBehaviour implements Behaviour {

	private AdvancedRobot robot;
	private double moveAmount;
	private boolean peek;

	public DefensiveBehaviour(AdvancedRobot robot) {
		this.robot = robot;
		moveAmount = Math.max(robot.getBattleFieldWidth(), robot.getBattleFieldHeight());
		peek = false;
	}

	@Override
	public void moveCommand() {
		peek = true;
		robot.ahead(moveAmount);
		peek = false;
		robot.turnRight(90);
	}

	@Override
	public void attackCommand(ScannedRobotEvent e) {
		robot.fire(2);
		if (peek) {
			robot.scan();
		}
	}

	@Override
	public void bulletHitCommand() {
		// Do Nothing
	}

	@Override
	public void wallHitCommand() {
		// Do Nothing
	}

	@Override
	public void robotHitCommand(HitRobotEvent e) {
		if (e.getBearing() > -90 && e.getBearing() < 90) {
			robot.back(100);
		} else {
			robot.ahead(100);
		}
	}

}

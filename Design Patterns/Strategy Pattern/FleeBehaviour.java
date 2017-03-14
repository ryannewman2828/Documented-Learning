import robocode.*;

public class FleeBehaviour implements Behaviour {

	private AdvancedRobot robot;
	private boolean movingForward;

	public FleeBehaviour(AdvancedRobot robot) {
		this.robot = robot;
	}

	@Override
	public void moveCommand() {
		robot.setAhead(40000);
		movingForward = true;
		robot.setTurnRight(90);
		robot.waitFor(new TurnCompleteCondition(robot));
		robot.setTurnLeft(180);
		robot.waitFor(new TurnCompleteCondition(robot));
		robot.setTurnRight(180);
		robot.waitFor(new TurnCompleteCondition(robot));
	}

	@Override
	public void attackCommand(ScannedRobotEvent e) {
		// Never attack in this strategy
	}

	@Override
	public void bulletHitCommand() {
		// Do nothing
	}

	@Override
	public void wallHitCommand() {
		reverseDirection();
	}

	@Override
	public void robotHitCommand(HitRobotEvent e) {
		if (e.isMyFault()) {
			reverseDirection();
		}
	}

	private void reverseDirection() {
		if (movingForward) {
			robot.setBack(40000);
			movingForward = false;
		} else {
			robot.setAhead(40000);
			movingForward = true;
		}
	}

}

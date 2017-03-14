import robocode.*;
import static robocode.util.Utils.normalRelativeAngleDegrees;

public class OffensiveBehaviour implements Behaviour {

	private AdvancedRobot robot;
	private String trackName;
	double gunTurnAmt;
	int count;

	public OffensiveBehaviour(AdvancedRobot robot) {
		this.robot = robot;
		trackName = null;
		robot.setAdjustGunForRobotTurn(true);
		gunTurnAmt = 10;
		count = 0;
	}

	@Override
	public void moveCommand() {
		robot.turnGunRight(gunTurnAmt);
		count++;
		if (count > 2) {
			gunTurnAmt = -10;
		}
		if (count > 5) {
			gunTurnAmt = 10;
		}
		if (count > 11) {
			trackName = null;
		}
	}

	@Override
	public void attackCommand(ScannedRobotEvent e) {
		if (trackName != null && !e.getName().equals(trackName)) {
			return;
		}

		if (trackName == null) {
			trackName = e.getName();
		}
		count = 0;
		if (e.getDistance() > 150) {
			gunTurnAmt = normalRelativeAngleDegrees(e.getBearing() + (robot.getHeading() - robot.getRadarHeading()));

			robot.turnGunRight(gunTurnAmt);
			robot.turnRight(e.getBearing());
			robot.ahead(e.getDistance() - 140);
			return;
		}

		gunTurnAmt = normalRelativeAngleDegrees(e.getBearing() + (robot.getHeading() - robot.getRadarHeading()));
		robot.turnGunRight(gunTurnAmt);
		robot.fire(3);
		if (e.getDistance() < 100) {
			if (e.getBearing() > -90 && e.getBearing() <= 90) {
				robot.back(40);
			} else {
				robot.ahead(40);
			}
		}
		robot.scan();
	}

	@Override
	public void bulletHitCommand() {
		// Ignore it

	}

	@Override
	public void wallHitCommand() {
		// Shounldn't happen here
	}

	@Override
	public void robotHitCommand(HitRobotEvent e) {
		trackName = e.getName();
		gunTurnAmt = normalRelativeAngleDegrees(e.getBearing() + (robot.getHeading() - robot.getRadarHeading()));
		robot.turnGunRight(gunTurnAmt);
		robot.fire(3);
		robot.back(50);

	}
}

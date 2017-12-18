public class JumpState implements State {

    private int jumpFrames;

    public JumpState() {
        jumpFrames = 60;
    }

    @Override
    public State handleInput(Player player, Inputs input) {
        if (jumpFrames == 0) {
            return new NeutralState();
        }

        return this;
    }

    @Override
    public void update() {
        System.out.println("Jumping for " + jumpFrames + " more frames");
        jumpFrames--;
    }
}

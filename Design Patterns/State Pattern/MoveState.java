public class MoveState implements State {

    @Override
    public State handleInput(Player player, Inputs input) {
        if (input == Inputs.JUMP) {
            return new JumpState();
        }

        if (input == Inputs.DUCK) {
            return new DuckState();
        }

        if (input == Inputs.MOVE) {
            return this;
        }

        return new NeutralState();
    }

    @Override
    public void update() {
        System.out.println("Moving");
    }
}

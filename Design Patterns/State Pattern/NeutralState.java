public class NeutralState implements State {

    @Override
    public State handleInput(Player player, Inputs input) {
        if (input == Inputs.JUMP) {
            return new JumpState();
        }

        if (input == Inputs.DUCK) {
            return new DuckState();
        }

        if (input == Inputs.MOVE) {
            return new MoveState();
        }

        return this;
    }

    @Override
    public void update() {
        System.out.println("Doing Nothing");
    }
}

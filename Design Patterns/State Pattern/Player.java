public class Player {

    private State currentState;

    public Player() {
        currentState = new NeutralState();
    }

    public void update(Inputs input) {
        currentState = currentState.handleInput(this, input);
        currentState.update();
    }
}

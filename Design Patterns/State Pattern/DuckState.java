public class DuckState implements State {
    private int duckFrames;

    public DuckState(){
        duckFrames = 5;
    }

    @Override
    public State handleInput(Player player, Inputs input) {
        if (duckFrames == 0) {
            return new NeutralState();
        }

        return this;
    }

    @Override
    public void update() {
        System.out.println("Ducking for " + duckFrames + " more frames");
        duckFrames--;
    }
}

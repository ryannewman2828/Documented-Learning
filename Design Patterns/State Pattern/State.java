public interface State {
    State handleInput(Player player, Inputs input);
    void update();
}

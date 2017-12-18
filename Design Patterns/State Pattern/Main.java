import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String cmd;
        Player player = new Player();
        boolean iterate = true;
        while (iterate) {
            System.out.print("Enter a command: ");
            cmd = sc.nextLine();
            if ("move".equals(cmd)) {
                player.update(Inputs.MOVE);
            } else if ("duck".equals(cmd)) {
                player.update(Inputs.DUCK);
            } else if ("jump".equals(cmd)) {
                player.update(Inputs.JUMP);
            } else if ("exit".equals(cmd)) {
                iterate = false;
            } else {
                player.update(null);
            }
        }
    }
}

import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String cmd;
		Grid g = new Grid();
		int moves = 0;
		while(true){
			cmd = sc.next();
			if("new".equals(cmd)){
				int n = sc.nextInt();
				g.init(n);
			} else if("init".equals(cmd)){
				int a, b;
				a = sc.nextInt();
				b = sc.nextInt();
				while(a != -1 && b != -1){
					g.init(a, b);
					a = sc.nextInt();
					b = sc.nextInt();
				}
				g.print();
			} else if("game".equals(cmd)){
				moves = sc.nextInt();
				System.out.println(moves + " moves left");
				if(moves == 0){
					System.out.println(g.isWon() ? "Won" : "Lost");
				}
			} else if("switch".equals(cmd)){
				int r = 0, c = 0;
				r = sc.nextInt();
				c = sc.nextInt();
				g.toggle(r, c);
				moves--;
				g.print();
				System.out.println(moves + (moves == 1 ? " move left" : " moves left"));
				if(g.isWon()){
					System.out.println("Won");
					break;
				}
				if(moves == 0){
					System.out.println(g.isWon() ? "Won" : "Lost");
					break;
				}
			}
		}
	}
}

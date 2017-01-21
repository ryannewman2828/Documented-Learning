import java.util.Scanner;

public class Main {
	public static void main(String[] args) throws InterruptedException {
		Scanner sc = new Scanner(System.in);
		System.out.println("Game has started");
		String cmd;
		Grid g = new Grid();
		long time = 0;
		while(true){
			cmd = sc.next();
			if("new".equals(cmd)){
				int n = sc.nextInt();
				g.init(n);
				System.out.println("New Grid created");
			} else if("init".equals(cmd)){
				int a, b;
				a = sc.nextInt();
				b = sc.nextInt();
				while(a != -1 && b != -1){
					g.turnOn(a, b);
					a = sc.nextInt();
					b = sc.nextInt();
				}
				g.print();
			} else if("step".equals(cmd)){
				g.finalize();
				int n = sc.nextInt();
				for (int i = 0; i < n; i++) {
					g.step();
					g.print();
					Thread.sleep(time);
				}
			} else if("time".equals(cmd)){
				time = sc.nextLong();
			}
		}
	}
}

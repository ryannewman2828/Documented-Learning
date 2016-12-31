import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String cmd;
		Grid g = new Grid();
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
				g.step();
				g.print();
			}
		}
	}
}

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Interpreter {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		if(args.length == 1){ // file specified
			// set up to read from file
		} else if (args.length != 0) {
			System.out.println("Incorrect Usage");
			System.exit(1);
		}
		
		List<Expression> stack = new ArrayList<>();
		
		while(sc.hasNextLine()){
			
		}
	}
}

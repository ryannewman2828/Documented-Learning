import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		System.out.print("Enter a country: ");
		Scanner sc = new Scanner(System.in);
		
		String input = sc.nextLine();
		
        Currency rupee = CurrencyFactory.createCurrency(input);
        System.out.println(rupee.getSymbol());
	}
}

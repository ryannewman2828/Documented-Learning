import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) throws FileNotFoundException {
		File file = new File("src/input.txt");
		Scanner sc = new Scanner(file);
		List<String> words = new ArrayList<>();
		while (sc.hasNext()) {
			words.add(sc.nextLine());
		}
		sc.close();

		Processor processor = new Echo(words);

		file = new File("src/commands.txt");
		sc = new Scanner(file);

		while (sc.hasNext()) {
			String command = sc.next();
			switch (command) {
			case "allcaps":
				processor = new AllCaps(processor);
				break;
			case "double":
				processor = new Double(processor);
				break;
			case "reverse":
				processor = new Reverse(processor);
				break;
			case "drop":
				int n = sc.nextInt();
				processor = new Drop(processor, n);
				break;
			case "replace":
				String regex = sc.next();
				String replace = sc.next();
				processor = new Replace(processor, regex, replace);
				break;
			case "grep":
				regex = sc.next();
				processor = new Grep(processor, regex);
				break;
			default:
				break;
			}
		}
		sc.close();

		while (processor.next()) {
			String word = processor.getWord();
			if (!word.equals("")) {
				System.out.println(word);
			}
		}
	}
}

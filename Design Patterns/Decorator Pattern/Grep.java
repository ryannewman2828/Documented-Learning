import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Grep extends Decorator {

	private Pattern p;

	public Grep(Processor textProcessor, String regex) {
		super(textProcessor);
		p = Pattern.compile(regex);
	}

	@Override
	public String getWord() {
		String word = textProcessor.getWord();
		Matcher m = p.matcher(word);
		return m.find() ? m.group(0) : "";
	}

	@Override
	public boolean next() {
		return textProcessor.next();
	}

}

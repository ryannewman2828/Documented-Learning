import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Replace extends Decorator {

	private Pattern p;
	private String replace;

	public Replace(Processor textProcessor, String regex, String replace) {
		super(textProcessor);
		p = Pattern.compile(regex);
		this.replace = replace;
	}

	@Override
	public String getWord() {
		Matcher m = p.matcher(textProcessor.getWord());
		return m.replaceFirst(replace);
	}

	@Override
	public boolean next() {
		return textProcessor.next();
	}

}

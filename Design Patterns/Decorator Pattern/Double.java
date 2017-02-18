
public class Double extends Decorator {

	private boolean doub;
	private String word;

	public Double(Processor textProcessor) {
		super(textProcessor);
		doub = false;
	}

	@Override
	public String getWord() {
		doub = !doub;
		if (doub) {
			word = textProcessor.getWord();
		}
		return word;
	}

	@Override
	public boolean next() {
		return textProcessor.next() || doub;
	}

}

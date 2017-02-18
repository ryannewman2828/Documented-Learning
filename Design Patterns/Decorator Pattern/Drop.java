
public class Drop extends Decorator {

	private int amount;

	public Drop(Processor textProcessor, int amount) {
		super(textProcessor);
		this.amount = amount;
	}

	@Override
	public String getWord() {
		String word = textProcessor.getWord();
		if (word.length() > amount) {
			return word.substring(amount - 1);
		} else {
			return "";
		}
	}

	@Override
	public boolean next() {
		return textProcessor.next();
	}

}

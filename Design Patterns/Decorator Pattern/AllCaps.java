
public class AllCaps extends Decorator {

	public AllCaps(Processor textProcessor) {
		super(textProcessor);
	}

	@Override
	public String getWord() {
		return textProcessor.getWord().toUpperCase();
	}

	@Override
	public boolean next() {
		return textProcessor.next();
	}

}

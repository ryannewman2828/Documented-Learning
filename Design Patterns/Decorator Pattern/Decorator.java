
public abstract class Decorator implements Processor {
	protected Processor textProcessor;

	public Decorator(Processor textProcessor) {
		this.textProcessor = textProcessor;
	}
}

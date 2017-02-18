
public class Reverse extends Decorator {

	public Reverse(Processor textProcessor) {
		super(textProcessor);
	}

	@Override
	public String getWord() {
		char[] chars = textProcessor.getWord().toCharArray();
		for (int i = 0; i < chars.length / 2; i++) {
			char temp = chars[i];
			chars[i] = chars[chars.length - i - 1];
			chars[chars.length - i - 1] = temp;
		}
		return String.copyValueOf(chars);
	}

	@Override
	public boolean next() {
		return textProcessor.next();
	}

}

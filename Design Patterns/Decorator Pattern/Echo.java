import java.util.ArrayDeque;
import java.util.Deque;
import java.util.List;

public class Echo implements Processor {

	private Deque<String> words;

	public Echo(List<String> words) {
		this.words = new ArrayDeque<>();
		this.words.addAll(words);
	}

	@Override
	public String getWord() {
		return words.poll();
	}

	@Override
	public boolean next() {
		return !words.isEmpty();
	}
}

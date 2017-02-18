import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Date;

public class Main {
	public static void main(String[] args) throws IOException {
		byte[] encodedContent = Files.readAllBytes(Paths.get("src/index.html"));
		String content = new String(encodedContent);
		Response response = new Response.ResponseBuilder("HTTP/1.1", 200, "OK", content)
				.contentLength(encodedContent.length).lastModified(new Date(2015, 3, 8))
				.server("Apache/1.3.3.7 (Unix) (Red-Hat/Linux)").acceptRanges("bytes").build();

		response.print();
	}
}

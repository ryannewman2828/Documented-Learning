import java.util.Date;

public class Response {
	private final String version;
	private final int statusCode;
	private final String reasonMessage;
	private final Date date;
	private final String contentType;
	private final String contentEncoding;
	private final int contentLength;
	private final Date lastModified;
	private final String server;
	private final String ETag;
	private final String acceptRanges;
	private final String connection;
	private final String content;

	public static class ResponseBuilder {

		// Required Parameters
		private final String version;
		private final int statusCode;
		private final String reasonMessage;
		private final String content;

		// Optional parameters - initialized to default values
		private Date date = new Date();
		private String contentType = "text/html; charset=UTF-8";
		private String contentEncoding = "UTF-8";
		private int contentLength = 0;
		private Date lastModified = new Date();
		private String server = "";
		private String ETag = "";
		private String acceptRanges = "";
		private String connection = "close";

		public ResponseBuilder(String version, int statusCode, String reasonMessage, String content) {
			this.version = version;
			this.statusCode = statusCode;
			this.reasonMessage = reasonMessage;
			this.content = content;
		}

		public ResponseBuilder date(Date date) {
			this.date = date;
			return this;
		}

		public ResponseBuilder contentType(String contentType) {
			this.contentType = contentType;
			return this;
		}

		public ResponseBuilder contentEncoding(String contentEncoding) {
			this.contentEncoding = contentEncoding;
			return this;
		}

		public ResponseBuilder contentLength(int contentLength) {
			this.contentLength = contentLength;
			return this;
		}

		public ResponseBuilder lastModified(Date lastModified) {
			this.lastModified = lastModified;
			return this;
		}

		public ResponseBuilder server(String server) {
			this.server = server;
			return this;
		}

		public ResponseBuilder ETag(String ETag) {
			this.ETag = ETag;
			return this;
		}

		public ResponseBuilder acceptRanges(String acceptRanges) {
			this.acceptRanges = acceptRanges;
			return this;
		}

		public ResponseBuilder connection(String connection) {
			this.connection = connection;
			return this;
		}

		public Response build() {
			return new Response(this);
		}
	}

	private Response(ResponseBuilder builder) {
		version = builder.version;
		statusCode = builder.statusCode;
		reasonMessage = builder.reasonMessage;
		date = builder.date;
		contentType = builder.contentType;
		contentEncoding = builder.contentEncoding;
		contentLength = builder.contentLength;
		lastModified = builder.lastModified;
		server = builder.server;
		ETag = builder.ETag;
		acceptRanges = builder.acceptRanges;
		connection = builder.connection;
		content = builder.content;
	}

	public void print() {
		System.out.println(version + " " + statusCode + " " + reasonMessage);
		System.out.println("Date: " + date.toString());
		System.out.println("Content-Type: " + contentType);
		System.out.println("Content-Encoding: " + contentEncoding);
		System.out.println("Content-Length: " + contentLength);
		System.out.println("Last-Modified: " + lastModified.toString());
		if (!server.equals("")) {
			System.out.println("Server: " + server);
		}
		if (!ETag.equals("")) {
			System.out.println("ETag: " + ETag);
		}
		if (!acceptRanges.equals("")) {
			System.out.println("Accept-Ranges: " + acceptRanges);
		}
		System.out.println("Connection: " + connection);
		System.out.println();
		System.out.println(content);
	}
}

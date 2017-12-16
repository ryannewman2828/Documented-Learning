public class CurrencyFactory {
	public static Currency createCurrency(String country) {
		switch(country.toLowerCase()) {
		case "india":
			return new Rupee();
		case "singapore":
			return new SGDDollar();
		case "us":
			return new USDollar();
		case "canada":
			return new CADDollar();
		default:
			throw new IllegalArgumentException("Currency Not Supported");
		}
	}
}

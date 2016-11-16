public interface Observer {
	public void notify(Subject whoNotified);
	public Subscription subType();
}

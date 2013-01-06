class HmmListener extends Listener {
	private FeatureExtractor extractor;
	
	public HmmListener (FeatureExtractor fe) {
		this.extractor = fe;
	}
	
	public void onInit(Controller controller) {
		System.out.println("Initialized");
	}
	
	public void onConnect(Controller controller) {
	    System.out.println("Connected");
	}
	
	public void onDisconnect(Controller controller) {
	    System.out.println("Disconnected");
	}
	
	public void onFrame(Controller controller) {
	    // Get the most recent frame and report some basic information
	    Frame frame = controller.frame();
	    extractor.loadFrame(frame);
	}
}

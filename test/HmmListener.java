import java.util.ArrayList;

class HmmListener extends Listener {
	private FeatureExtractor extractor;
	private int windowSize;
	private ArrayList<Frame> frames;
	private LeapHmm hmmController;
	
	public HmmListener (LeapHmm hmmController) {
		this.extractor = hmmController.fe;
		this.frames = new ArrayList<Frame>();
		this.hmmController = hmmController;
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
	    hmmController.predict();
	}
	
}

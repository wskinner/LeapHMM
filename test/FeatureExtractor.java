import java.util.ArrayList;

import be.ac.ulg.montefiore.run.jahmm.ObservationVector;

abstract class FeatureExtractor {
	/*
	 * Handle conversions between raw Leap data and jahmm.Observations.
	 * Subclass this class to implement different types of feature 
	 * extraction.
	 */
	
	protected ArrayList<ArrayList<ArrayList<Double>>> featureSequences;
	protected ArrayList<Frame> frameSequences;
	protected int dimension;
	
	public FeatureExtractor() {
		
	}
	
	/*
	 * Import a chunk of data from a file. Useful for training.
	 */
	public void loadData(String filename) {
		
	}

	/*
	 * Import an array of leap data (might be passed in from a sliding window).
	 */
	public void loadData(Frame[] frames) {
		
	}

	/*
	 * Import a single Frame of data.
	 */
	public void loadFrame(Frame frame) {
		
	}
	
	/*
	 * Return the features constructed from the n oldest frames.
	 */
	public Object getFeatures(int n) {
		return null;
	}
	
	/*
	 * Return the features constructed from all the frames.
	 */
	public ArrayList<ArrayList<ObservationVector>> getFeatures() {
		return null;
	}

	/*
	 * Return a vector of windowSize features.
	 */
	public ArrayList<? extends ObservationVector> getRealtimeFeatures() {
		return null;
	}

	/*
	 * Called after a gesture was recognized.
	 * The prediction will not use any of the frames that 
	 * the just-predicted gesture used.
	 */
	public void emptyBuffer() {
		
	}
	
	
}
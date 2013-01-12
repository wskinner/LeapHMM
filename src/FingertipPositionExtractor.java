import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Timer;
import java.util.TimerTask;

import be.ac.ulg.montefiore.run.jahmm.ObservationVector;


public class FingertipPositionExtractor extends FeatureExtractor {
	/*
	 * Simple feature extractor which extracts fingertip position from
	 * Leap Frames.
	 */
	
	private int nFingers;
	private int windowSize;
	
	public FingertipPositionExtractor(int nFingers, int windowSize, int minSequenceLength) {
		this.featureSequences = new ArrayList<ArrayList<ArrayList<Double>>>();
		this.frameSequences = new ArrayList<Frame>();
		this.dimension = 3;
		this.nFingers = nFingers;
		this.windowSize = windowSize;
		this.ready = false;
		this.minSequenceLength = minSequenceLength;
	}
	
	/*
	 * Uses just-in-time feature construction. This is unnecessary
	 * for the current simple features and hopefully won't impose too much
	 * of a performance burden.
	 */
	public ArrayList<ObservationVector> getRealtimeFeatures() {
		ArrayList<ObservationVector> observedFeatures = new ArrayList<ObservationVector>();
		for (Frame f : frameSequences) {
			ObservationVector obV = makeFeatures(f);
			if (obV != null) {
				observedFeatures.add(obV);
			}
		}
		ready = false;
		return observedFeatures;
	}
	
	private boolean canMakeFeatures(Frame f) {
		if (f.hands().isEmpty()) {
			return false;
		}
		if (f.hands().get(0).fingers().isEmpty()) {
			return false;
		}
		return true;
	}
	
	private ObservationVector makeFeatures(Frame f) {
		if (!canMakeFeatures(f)) {
			return null;
		}
		double[] fingerPos = new double[dimension];
		Vector fingerVect = f.hands().get(0).fingers().get(0).tip().getPosition();
		fingerPos[0] = fingerVect.getX();
		fingerPos[1] = fingerVect.getY();
		return new ObservationVector(fingerPos);
	}

	/*
	 * Return a List of ObservationVector containing features.
	 * After this method is called, featureSequences will be empty.
	 * Assumes featureSequences has already been filled (e.g. by calling loadData().
	 */
	public ArrayList<ArrayList<ObservationVector>> getFeatures() {
		ArrayList<ArrayList<ObservationVector>> sequences = new ArrayList<ArrayList<ObservationVector>>();
		for (ArrayList<ArrayList<Double>> observation : featureSequences) {
			sequences.add(buildFeatures(observation));
		}
		featureSequences = new ArrayList<ArrayList<ArrayList<Double>>>();
		return sequences;
	}

	private ArrayList<ObservationVector> buildFeatures(ArrayList<ArrayList<Double>> observation) {
		ArrayList<ObservationVector> featureList = new ArrayList<ObservationVector>();
		for (ArrayList<Double> frame : observation) {
			double[] fingerPos = new double[dimension];
			for (int i = 0; i<dimension; i++) {
				fingerPos[i] = frame.get(i).doubleValue();
			}
			featureList.add(new ObservationVector(fingerPos));
		}
		return featureList;
	}

	/*
	 * Given a string representing a line from a CSV file, construct an ArrayList
	 * of Doubles if necessary, and store it in the appropriate location in featureSequences.
	 */
	private void processLine(String line) {
		String[] cols = line.split(",");
		int index = Integer.parseInt(cols[0]);
		if (featureSequences.size() <= index) {
			while (featureSequences.size() <= index) {
				featureSequences.add(new ArrayList<ArrayList<Double>>());
			}
		}
		ArrayList<Double> data = new ArrayList<Double>();
		for (int i = 1; i<cols.length; i++) {
			data.add(Double.parseDouble(cols[i]));
		}
		if (data.size() != dimension) {
			throw new IndexOutOfBoundsException();
		}
		this.featureSequences.get(index).add(data);
	}

	/*
	 * (non-Javadoc)
	 * @see FeatureExtractor#loadData(java.lang.String)
	 */
	public void loadData (String filename) {
		BufferedReader br = null;
		try {
			String currentLine;
			br = new BufferedReader(new FileReader(filename));
			while ((currentLine = br.readLine()) != null) {
				processLine(currentLine);
			}
		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			try {
				if (br != null)br.close();
			} catch (IOException ex) {
				ex.printStackTrace();
			}
		}	
	}
	
	/*
	 * For use in real time. Meant to be called from the onFrame 
	 * method of a Leap Listener.
	 */
	public void loadFrame(Frame frame) {
		if (canMakeFeatures(frame)) {
			if (frameSequences.size() == windowSize) {
				frameSequences.remove(0);
			}
			frameSequences.add(frame);
			//System.out.println("Added frame. Currently there are " + frameSequences.size() + " frames out of a maximum " + minSequenceLength + " allowed.");
		}
		else if (frameSequences.size() >= minSequenceLength) {
			ready = true;
			//System.out.println("Frames ready. " + frameSequences.size() + " frames");
		}
	}
	
	/*
	 * Called after a gesture was recognized.
	 * The prediction will not use any of the frames that 
	 * the just-predicted gesture used.
	 */
	public void emptyBuffer() {
		frameSequences = new ArrayList<Frame>();
	}
}
import java.util.ArrayList;
import java.util.List;

import be.ac.ulg.montefiore.run.jahmm.*;
import be.ac.ulg.montefiore.run.jahmm.learn.*;

class LeapHmm {
	static int nStates = 8;
	static int dimension = 3;
	static String datapath = "/Users/willskinner/Dropbox/eclipse_workspace/LeapHMM/"; 
	public static void main(String[] args) {
		test(args);
	}

	/*
	 * Test the system on the given gestures.
	 */
	public static void test(String[] gestureNames) {
		Gesture[] gestures = new Gesture[gestureNames.length];
		for (int i = 0; i<gestures.length; i++) {
			gestures[i] = new Gesture(gestureNames[i], nStates, dimension);
		}
		Recognizer rec = new Recognizer(gestures, 0.75);
		
		ArrayList<ArrayList<ArrayList<ObservationVector>>> sequences = new ArrayList<ArrayList<ArrayList<ObservationVector>>>();
		FingertipPositionExtractor extractor = new FingertipPositionExtractor(1);
		for (String gName : gestureNames) {
			extractor.loadData(datapath + gName + "_train.csv");
			sequences.add(extractor.getFeatures());
		}
		for (ArrayList<ArrayList<ObservationVector>> obs : sequences) {
			for (int i = 0; i<obs.size(); i++) {
				ArrayList<ObservationVector> ges = obs.get(i);
				try {
					ges.get(0);
				}
				catch (Exception x) {
					System.out.println(obs);
				}
			}
		}
		rec.train(new int[0], sequences);
		
		for (String gName : gestureNames) {
			extractor.loadData(datapath + gName + "_test.csv");
			System.out.println("Verifying " + gName);
			int count = 0;
			int obsLength = 0;
			for (ArrayList<ObservationVector> obs : extractor.getFeatures()) {
				String result = rec.predict(obs);
				if (!result.equals(gName)) {
					count++;
				}
				obsLength++;
			}
			System.out.println("Correctly identified " + new Integer(obsLength - count).toString() +
							   " out of " + obsLength + " observations.");
		}
	}
}
class Gesture {
	/*
	    Matches one type of gesture, and provides methods to gain information
	    about the current status of the gesture. I.e. has it been matched, 
	    if so what is the confidence level, and so on.
	*/
	public boolean debug;
	private Hmm<ObservationVector> model;
	private BaumWelchLearner learner;
	private String name;
	private int nStates;
	private int dimension;
	
	public Gesture(String name, int nStates, int dimension) {
		this.debug = true;
		this.model = new Hmm<ObservationVector>(nStates, new OpdfMultiGaussianFactory(dimension));
		this.learner = new BaumWelchScaledLearner();
		this.name = name;
		this.nStates = nStates;
		this.dimension = dimension;
	}
	
	/*
	 * First guess the centroids of the states using K-Means. Then fit the HMM to the training data 
	 * Using Baum-Welch.
	 */
	public void train(ArrayList<ArrayList<ObservationVector>> sequences) {
		if (debug) {
			System.out.println("Training " + name);
		}
		KMeansLearner <ObservationVector> kml = new KMeansLearner <ObservationVector>(nStates, 
																					  new OpdfMultiGaussianFactory(dimension), 
																					  sequences); 
		model = learner.learn(kml.iterate(), sequences);
	}
	
	/*
	 * Return the maximum likelihood state sequenqe of the HMM, given the sequence
	 * of observations.
	 */
	public int[] predict(List<? extends ObservationVector> sequence) {
		return model.mostLikelyStateSequence(sequence);
	}
	
	/*
	 * Return the probability of the given observation sequence given the HMM.
	 */
	public double prob(List<? extends ObservationVector> sequence) {
		return model.probability(sequence);
	}

	public String getName() {
		return name;
	}

}

class Recognizer {
	/*
	 * 
	    Matches any number of gestures, which are internally represented as
	    Gestures. At every new observation, the Recognizer passes the
	    observation to each Gesture and, and then checks to see if any gesture
	    has been successfully observed with a high enough level of confidence.
	 */
	
	private Gesture[] gestures;
	private double threshold;
	
	public Recognizer(Gesture[] gestures, double threshold) {
		this.gestures = gestures;
		this.threshold = threshold;
	}

	/*
	 * For each gesture index in the given array, train that gesture's HMM with
	 * the corresponding observation sequences in sequences.
	 */
	public void train(int[] gestureIndices, ArrayList<ArrayList<ArrayList<ObservationVector>>> sequences) {
		if (gestureIndices.length == 0) {
			gestureIndices = new int[sequences.size()];
			for (int i = 0; i<gestureIndices.length; i++) {
				gestureIndices[i] = i;
			}
		}
		if (gestureIndices.length != sequences.size()) {
			throw new IndexOutOfBoundsException();
		}
		for (int i : gestureIndices) {
			gestures[i].train(sequences.get(i));
		}
	}
	
	/*
	 * Helper method for predict.
	 */
	private double[] getGestureProbs(List<? extends ObservationVector> sequence) {
		double[] gProbs = new double[gestures.length];
		for (int i = 0; i<gestures.length; i++) {
			gProbs[i] = gestures[i].prob(sequence);
		}
		return gProbs;
	}
	
	private ArrayList<int[]> getMaxLikelihoodStateSequences(ArrayList<? extends ObservationVector> sequence) {
		ArrayList<int[]> seqs = new ArrayList<int[]>();
		for (int i = 0; i<gestures.length; i++) {
			seqs.add(gestures[i].predict(sequence));
		}
		return seqs;
	}
	
	public String predict(ArrayList<? extends ObservationVector> sequence) {
		double[] gestureProbs = getGestureProbs(sequence);
		double max = 0.0;
		int maxIndex = 0;
		for (int i = 0; i<gestures.length; i++) {
			if (gestureProbs[i] > max) {
				max = gestureProbs[i];
				maxIndex = i;
			}
		}
		for (int[] ss : getMaxLikelihoodStateSequences(sequence)) {
			for (int i : ss) {
				System.out.print(i);
			}
			System.out.println();
		}
		return gestures[maxIndex].getName();
	}
}
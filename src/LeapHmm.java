import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import be.ac.ulg.montefiore.run.jahmm.*;
import be.ac.ulg.montefiore.run.jahmm.learn.*;
import be.ac.ulg.montefiore.run.jahmm.draw.*;

class LeapHmm {
	public FeatureExtractor fe;
	public Recognizer rec;
	public ArrayList<ArrayList<ArrayList<ObservationVector>>> trainingSequences;
	
	static boolean debug;
	static int nStates = 8;
	static int dimension = 3;
	static String datapath = "/Users/willskinner/Dropbox/eclipse_workspace/LeapHMM/"; 
	
	
	public static void main(String[] args) throws IOException {
		debug = false;
		LeapHmm testHmm = new LeapHmm();
		testHmm.initialize(args);
		test(args, testHmm);
		//draw(args);
	}

	/*
	 * Make a prediction based on the window of frames currently in 
	 * my FeatureExtractor. 
	 */
	public void predict() {
		
	}
	
	public static void testRealtime(String[] gestureNames, LeapHmm parent) {
		parent.fe = new FingertipPositionExtractor(1);
	    HmmListener listener = new HmmListener(parent, 122);
	    Controller controller = new Controller(listener);

	    // Keep this process running until Enter is pressed
	    System.out.println("Press Enter to quit...");
	    System.console().readLine();

	    // The controller must be disposed of before the listener
	    controller = null;
	}
	
	public static void draw(String[] gestureNames) throws IOException {
		Gesture[] gestures = new Gesture[gestureNames.length];
		for (int i = 0; i<gestures.length; i++) {
			gestures[i] = new Gesture(gestureNames[i], nStates, dimension, new int[2]);
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
		rec.draw();
	}
	
	public void initialize(String[] gestureNames) {	
		Gesture[] gestures = new Gesture[gestureNames.length];
		for (int i = 0; i<gestures.length; i++) {
			gestures[i] = new Gesture(gestureNames[i], nStates, dimension, new int[2]);
		}
		int[] lswipe_finals = new int[1];
		lswipe_finals[0] = 7;
		
		int[] rswipe_finals = new int[2];
		rswipe_finals[0] = 7;
		rswipe_finals[1] = 4;
		
		int[] circle_finals = new int[3];
		circle_finals[0] = 6;
		circle_finals[1] = 7;
		circle_finals[2] = 2;
		
		gestures[0].setFinalStates(lswipe_finals);
		gestures[1].setFinalStates(rswipe_finals);
		gestures[2].setFinalStates(circle_finals);
		
		rec = new Recognizer(gestures, 0.75);
		trainingSequences = new ArrayList<ArrayList<ArrayList<ObservationVector>>>();
		fe = new FingertipPositionExtractor(1);
		
	}

	/*
	 * Test the system on the given gestures.
	 * testHmm must be an initialized LeapHmm.
	 */
	public static void test(String[] gestureNames, LeapHmm testHmm) {
		for (String gName : gestureNames) {
			testHmm.fe.loadData(datapath + gName + "_train.csv");
			testHmm.trainingSequences.add(testHmm.fe.getFeatures());
		}
		for (ArrayList<ArrayList<ObservationVector>> obs : testHmm.trainingSequences) {
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
		testHmm.rec.train(new int[0], testHmm.trainingSequences);
		
		for (String gName : gestureNames) {
			testHmm.fe.loadData(datapath + gName + "_test.csv");
			System.out.println("Verifying " + gName);
			int count = 0;
			int obsLength = 0;
			for (ArrayList<ObservationVector> obs : testHmm.fe.getFeatures()) {
				String result = testHmm.rec.predict(obs);
				if (result == null) {
					count++;
				}
				else if (!result.equals(gName)) {
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
	private int[] finalStates;
	
	public Gesture(String name, int nStates, int dimension, int[] finalStates) {
		this.debug = true;
		this.model = new Hmm<ObservationVector>(nStates, new OpdfMultiGaussianFactory(dimension));
		this.learner = new BaumWelchScaledLearner();
		this.name = name;
		this.nStates = nStates;
		this.dimension = dimension;
		this.finalStates = finalStates;
	}
	
	public void setFinalStates(int[] newFinals) {
		finalStates = newFinals;
		
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
	 * Return the maximum likelihood state sequence of the HMM, given the sequence
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

	public void draw() throws IOException {
		(new GenericHmmDrawerDot()).write(model, name+".dot");
	}

	public boolean matched(List<? extends ObservationVector> sequence) {
		int[] mlss = predict(sequence);
		int lastState = mlss[mlss.length-1];
		for (int s : finalStates) {
			if (s == lastState) {
				return true;
			}
		}
		return false;
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

	/*
	 * Given a sequence of observations, return the 
	 * name of the maximum likelihood 
	 * gesture.
	 */
	public String predict(ArrayList<? extends ObservationVector> sequence) {
		
		ArrayList<Gesture> matchedGestures = new ArrayList<Gesture>();
		for (Gesture g : gestures) {
			if (g.matched(sequence)) {
				matchedGestures.add(g);
			}
		}
		if (matchedGestures.size() == 1) {
			return matchedGestures.get(0).getName();
		}
		else {
			if (LeapHmm.debug) {
				System.out.print("Matched: ");
				for (Gesture g : matchedGestures) {
					System.out.print(g.getName() + " ");
				}
				System.out.println();
				printSequence(sequence);
			}
			return null;
		}
	
		/*
		double[] gestureProbs = getGestureProbs(sequence);
		double max = 0.0;
		int maxIndex = 0;
		for (int i = 0; i<gestures.length; i++) {
			if (gestureProbs[i] > max) {
				max = gestureProbs[i];
				maxIndex = i;
			}
		}
		return gestures[maxIndex].getName();
		*/
	}
	
	private void printSequence(ArrayList<? extends ObservationVector> sequence) {
		int j = 0;
			for (int[] ss : getMaxLikelihoodStateSequences(sequence)) {
				System.out.print(gestures[j].getName() + ": ");
				for (int i : ss) {
					System.out.print(i);
				}
				System.out.println();
				j++;
			}
	}
	
	public void draw() throws IOException {
		for (Gesture g : gestures) {
			g.draw();
		}
	}
}
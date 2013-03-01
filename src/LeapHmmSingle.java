import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.StreamTokenizer;
import java.io.Writer;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map.Entry;

import be.ac.ulg.montefiore.run.jahmm.Hmm;
import be.ac.ulg.montefiore.run.jahmm.ObservationVector;
import be.ac.ulg.montefiore.run.jahmm.OpdfMultiGaussian;
import be.ac.ulg.montefiore.run.jahmm.OpdfMultiGaussianFactory;
import be.ac.ulg.montefiore.run.jahmm.draw.GenericHmmDrawerDot;
import be.ac.ulg.montefiore.run.jahmm.io.FileFormatException;
import be.ac.ulg.montefiore.run.jahmm.io.HmmReader;
import be.ac.ulg.montefiore.run.jahmm.io.HmmWriter;
import be.ac.ulg.montefiore.run.jahmm.io.OpdfMultiGaussianReader;
import be.ac.ulg.montefiore.run.jahmm.io.OpdfMultiGaussianWriter;
import be.ac.ulg.montefiore.run.jahmm.io.OpdfReader;
import be.ac.ulg.montefiore.run.jahmm.io.OpdfWriter;
import be.ac.ulg.montefiore.run.jahmm.learn.BaumWelchScaledLearner;
import be.ac.ulg.montefiore.run.jahmm.learn.KMeansLearner;
import java.io.IOException;
import java.io.StreamTokenizer;

import be.ac.ulg.montefiore.run.jahmm.OpdfMultiGaussian;
class LeapHmmSingle extends LeapHmm {
	public FeatureExtractor fe;
	public SingleHmmRecognizer rec;
	public ArrayList<ArrayList<ArrayList<ObservationVector>>> trainingSequences;
	private boolean ready = false;
	
	static boolean debug;
	static int nStates = 8;
	static int dimension = 3;
	static int windowSize = 100;
	static String datapath = "/Users/willskinner/Dropbox/eclipse_workspace/LeapHMM/data/"; 
	
	
	public static void main(String[] args) throws IOException {
		/*
		debug = false;
		*/
		/*
		LeapHmm testHmm = new LeapHmm();
		testHmm.initialize(args);
		test(args, testHmm);
		*/
		//draw(args);
		//listen(args, testHmm);
		int nStates = Integer.parseInt(args[args.length-1]);
		LeapHmmSingle testHmm = new LeapHmmSingle();
		String[] gestureNames = new String[args.length-1];
		for (int i = 0; i<args.length-1; i++) {
			gestureNames[i] = args[i];
		}
		testHmm.initialize(gestureNames, nStates);
		testHmm.test(gestureNames);
		testHmm.rec.draw();
		listen(gestureNames, testHmm);
	}
	
	/*
	 * Make a prediction based on the window of frames currently in 
	 * my FeatureExtractor. 
	 */
	public void predict() {
		if (fe.ready) {
			ArrayList<? extends ObservationVector> seq = fe.getRealtimeFeatures();
			String prediction = rec.predict(seq);
			System.out.print(prediction);
			System.out.println(" " + rec.getMinimalStateSequence(rec.model.mostLikelyStateSequence(seq)));
			fe.emptyBuffer();
			fe.ready = false;
		}
	}

	public static void listen(String[] gestureNames, LeapHmmSingle hmm) {
	    HmmListener listener = new HmmListener(hmm);
	    Controller controller = new Controller(listener);
/*
	    // Keep this process running until Enter is pressed
	    System.out.println("Press Enter to quit...");
	    System.console().readLine();

	    // The controller must be disposed of before the listener
	    controller = null;
	    */
	    while (true) {
	    	continue;
	    }
	}
	
	public static void draw(String[] gestureNames, LeapHmm testHmm) throws IOException {
		testHmm.initialize(gestureNames);
	}
	
	public void initialize(String[] gestureNames, int nStates) {	
		debug = true;
		rec = new SingleHmmRecognizer(nStates, 3);
		fe = new FingertipPositionExtractor(1, windowSize, rec.minFrames);
		trainingSequences = new ArrayList<ArrayList<ArrayList<ObservationVector>>>();
		for (String gName : gestureNames) {
			if (debug) {
				System.out.println("imported data from " + gName);
			}
			//fe.loadData(datapath + gName + "_train.csv");
			fe.loadData(datapath + gName + "_train.csv");
			trainingSequences.add(fe.getFeatures());
		}
		ArrayList<ArrayList<ObservationVector>> flatObservations = new ArrayList<ArrayList<ObservationVector>>();
		for (ArrayList<ArrayList<ObservationVector>> gesture : trainingSequences) {
			flatObservations.addAll(gesture);
		}
		rec.trainHmm(flatObservations);
		rec.learnGestures(trainingSequences, gestureNames);
		fe.minSequenceLength = rec.minFrames;
		System.out.println("The recognizer has a window size of " + rec.minFrames + " to " + windowSize + " frames.");
}
	
	public void test(String[] gestureNames) {
		ArrayList<ArrayList<ObservationVector>> testSequences = new ArrayList<ArrayList<ObservationVector>>();
		for (String gName : gestureNames) {
			fe.loadData(datapath + gName + "_test.csv");
			testSequences = fe.getFeatures();
			int wrongCount = 0;
			System.out.println("Verifying " + gName);
			for (ArrayList<ObservationVector> g : testSequences) {
				String prediction = rec.predict(g);
				if (prediction != null && !prediction.equals(gName)) {
					wrongCount++;
					System.out.println("Incorrectly identified " + rec.getMinimalStateSequence(rec.model.mostLikelyStateSequence(g)) + " as " + prediction);
				}
			}
			System.out.println("Correctly identified " + (testSequences.size()-wrongCount) + " out of " + testSequences.size() + " " + gName + "s");
		}
	}
	
}

class SingleHmmRecognizer {
	public int minFrames;
	private int nStates;
	private int dimension;
	private int minLength;
	public Hmm<ObservationVector> model;
	private HashMap<String, String> states;
	private int maxLength;
	
	public SingleHmmRecognizer(int nStates, int dimension) {
		this.nStates = nStates;
		this.dimension = dimension;
		this.states = new HashMap<String, String>();
		this.minLength = 1000;
		this.minFrames = 1000;
	}
	
	
	public void draw() {
		try {
			(new GenericHmmDrawerDot()).write(model, "LeapHmm.dot");
		} catch (IOException e) {
			e.printStackTrace();
		}
	}


	/*
	 * Given a list of observation sequences in any order,
	 * learn the HMM of the entire set of gestures.
	 */
	public void trainHmm(ArrayList<ArrayList<ObservationVector>> sequences) {
		if (LeapHmmSingle.debug) {
			System.out.println("Training the HMM...");
		}
		KMeansLearner <ObservationVector> kml = 
				new KMeansLearner <ObservationVector>(nStates, 
													  new OpdfMultiGaussianFactory(dimension), 
													  sequences); 
		BaumWelchScaledLearner learner = new BaumWelchScaledLearner();
		model = learner.learn(kml.iterate(), sequences);
		if (LeapHmmSingle.debug) {
			System.out.println("Done.");
		}
	}

	/*
	 * For each gesture, learn the most likely minimal state
	 * sequence associated with it.
	 */
	public void learnGestures(ArrayList<ArrayList<ArrayList<ObservationVector>>> gestureList, String[] gestureNames) {
		try {
			if (gestureList.size() != gestureNames.length) {
				throw new Exception("Value mismatch");
			}
			int gestureIndex = 0;
			for (ArrayList<ArrayList<ObservationVector>> gesture : gestureList) {
				String g = initializeGesture(gesture, gestureNames[gestureIndex]);
				System.out.println(gestureNames[gestureIndex] + ": " + g);
				gestureIndex++;
			}
			
		} 
		catch (Exception e) {
			e.printStackTrace();
		}
	}
	

	/*
	 * Return the "minimal state sequence" associated with a state sequence.
	 * For example, 000011112222333344444 maps to "01234".
	 */
	public String getMinimalStateSequence(int[] stateSeq) {
		StringBuilder minimalStateSequence = new StringBuilder();
		int lastState = -1;
		for (int i : stateSeq) {
			if (i != lastState) {
				minimalStateSequence.append((char) (i+65));
				lastState = i;
			}
		}
		return minimalStateSequence.toString();
	}
	/*
	 * Learn the most likely state sequence for a set of observations
	 * and store the mapping from stateSequence => gesture name in
	 * states.
	 */
	public String initializeGesture(ArrayList<ArrayList<ObservationVector>> sequences, String name) {
		HashMap<String, Integer> sequenceCounts = new HashMap<String, Integer>();
		StringBuilder result = new StringBuilder();
		for (ArrayList<ObservationVector> gesture : sequences) {
			if (gesture.size() < minFrames) {
				minFrames = gesture.size();
			}
			int[] mLSS = model.mostLikelyStateSequence(gesture);
			String minimalStateSequence = getMinimalStateSequence(mLSS);
			if (minimalStateSequence.length() == 1) {
				continue;
			}
			if (sequenceCounts.containsKey(minimalStateSequence)) {
				sequenceCounts.put(minimalStateSequence, sequenceCounts.get(minimalStateSequence) + 1);
			}
			else {
				sequenceCounts.put(minimalStateSequence, 1);
			}
		}
		int minLength = 1000;
		int maxLength = 0;
		int nObservations = sequences.size();
		for (String k : sequenceCounts.keySet()) {
			int count = sequenceCounts.get(k);
			if (k.length() < minLength) {
				minLength = k.length();
			}
			if (k.length() > maxLength) {
				maxLength = k.length();
			}
			if (((double)count / (double)nObservations) > 0.1) {
				states.put(k, name);
			}
			result.append(" "+k);
		}
		this.maxLength = maxLength;
		this.minLength = minLength;
		return result.toString();
	}
	
	public String predict(ArrayList<? extends ObservationVector> seq) {
		String minimalStateSequence = getMinimalStateSequence(model.mostLikelyStateSequence(seq));
		if (minimalStateSequence.length() < minLength) {
			return null;
		}
		String bestMatch = null;
		int minDistance = 1000;
		for (String k : states.keySet()) {
			int dist = Levenshtein.getLevenshteinDistance(k, minimalStateSequence);
			if (bestMatch == null || dist < minDistance) {
				bestMatch = k;
				minDistance = Levenshtein.getLevenshteinDistance(bestMatch, minimalStateSequence);
			}
		}
		return states.get(bestMatch);
	}
	
	public void dumpRecognizer(String outName) throws IOException {
	    FileWriter writer = new FileWriter(outName);
	    // we create our own impl of the OpdfIntegerWriter because we want
	    // to control the formatting of the opdf probabilities. With the 
	    // default OpdfIntegerWriter, small probabilities get written in 
	    // the exponential format, ie 1.234..E-4, which the HmmReader does
	    // not recognize.
	    OpdfMultiGaussianWriter opdfWriter = new OpdfMultiGaussianWriter();
	    HmmWriter.write(writer, opdfWriter, model);
	    writer.flush();
	    writer.close();
	    System.out.println("Wrote the HMM to " + outName);
	  }
/*	
	public static Hmm<ObservationVector> loadRecognizer(String inName) throws IOException, FileFormatException {
		File file = new File(inName);
	    FileReader reader = new FileReader(inName);
	    return hmm;
	}
	*/
}

	
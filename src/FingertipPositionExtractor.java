import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Timer;
import java.util.TimerTask;

import be.ac.ulg.montefiore.run.jahmm.ObservationVector;


public class FingertipPositionExtractor extends FeatureExtractor {

	public FingertipPositionExtractor(int nFingers, int windowSize, int minSequenceLength) {
		super(nFingers, windowSize, minSequenceLength);
	}
	/*
	 * Simple feature extractor which extracts fingertip position from
	 * Leap Frames.
	 */

}
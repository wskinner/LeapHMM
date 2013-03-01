import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.text.ParseException;
import java.util.HashMap;
import java.util.Iterator;
import java.util.ArrayList;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;


public class VelocityFeatureExtractor extends FeatureExtractor {
	
	public VelocityFeatureExtractor(int nFingers, int windowSize,
			int minSequenceLength) {
		super(nFingers, windowSize, minSequenceLength);
		// TODO Auto-generated constructor stub
	}

	public static void main(String[] args) {
		VelocityFeatureExtractor vff = new VelocityFeatureExtractor(1, 50, 40);
		vff.loadData(LeapHmmSingle.datapath + "test.json");
	}
	/*
	 * Expects filename to refer to a JSON file of the following format:
	 * {'gestures': [
	 * [{'hands': 
	 * [[{'velocities': {'x_norm': double, 'y_norm': double, 'z_norm': double,
	 * 'x': double, 'y': double, 'z': double}
	 * 'position': [double, double, double]}],
	 * ...
	 * ]
	 * } ... ]
	 * ]}
	 * @see FeatureExtractor#loadData(java.lang.String)
	 */
	
	public void loadData(String filename) {
		JSONParser parser = new JSONParser();
		ArrayList<ArrayList<HashMap<String,Double>>> trainingSequence = new ArrayList<ArrayList<HashMap<String,Double>>>();
		try {
	 
			Object obj = parser.parse(new FileReader(filename));
			JSONObject gestureObservations = (JSONObject) obj;
			JSONArray gestures = (JSONArray)gestureObservations.get("gestures");
			for (Object gesture : gestures) {
				JSONObject observations = (JSONObject) ((JSONArray) gesture).get(0);
				JSONArray hands = (JSONArray) observations.get("hands");
				ArrayList<HashMap<String,Double>> g = new ArrayList<HashMap<String,Double>>();
				for (Object fingers : hands) {
					for (Object finger : (JSONArray) fingers) {
						HashMap<String,Double> frame = new HashMap<String,Double>();
						JSONObject jFinger = (JSONObject) finger;
						frame.put("x_norm", (Double)jFinger.get("x_norm"));
						frame.put("y_norm", (Double)jFinger.get("y_norm"));
						frame.put("z_norm", (Double)jFinger.get("z_norm"));
						frame.put("x", (Double)jFinger.get("x"));
						frame.put("y", (Double)jFinger.get("y"));
						frame.put("z", (Double)jFinger.get("z"));
						
						JSONArray position = (JSONArray) jFinger.get("position");
						frame.put("x_pos", (Double)position.get(0));
						frame.put("y_pos", (Double)position.get(1));
						frame.put("z_pos", (Double)position.get(2));
						g.add(frame);
					}
				}
				trainingSequence.add(g);
			}
			System.out.print(trainingSequence);
			
	 
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		} catch (org.json.simple.parser.ParseException e) {
			e.printStackTrace();
		}
	 
     }
}

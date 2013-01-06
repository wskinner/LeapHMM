from lib import Leap
import sys
from controller import AbletonController

def main():
    # Create a sample listener and assign it to a controller to receive events
    ableton_controller = AbletonController()

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    sys.stdin.readline()

    # The controller must be disposed of before the listener
    ableton_controller.destroy()

if __name__=="__main__":
    main()

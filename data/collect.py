import os,sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir) 
from leap.lib import Leap 
from python_src.features import dumpFeaturesCSV as dumpFeatures
from python_src.features import dumpFrames


class Listener(Leap.Listener): 
    def __init__(self): 
        self.recording = False
        super(Listener, self).__init__()

    def onInit(self, controller): 
        self.frames = []

    def onFrame(self, controller): 
        if self.recording: 
            self.frames.append(controller.frame())

    def start_recording(self): 
        self.recording = True

    def stop_recording(self): 
        self.recording = False 
        return_list = [frame for frame in self.frames]
        self.frames = [] 
        return return_list

def listen(gesture_list): 
    listener = Listener() 
    controller = Leap.Controller(listener) 

    print "- Press Enter to toggle recording" 
    print "- Press 'q' + Enter to quit"
    print "[Record]",
    while True: 
        letter = sys.stdin.readline()
        if letter[0]  == 'q': 
            print "Done recognizing gesture"
            break
        if listener.recording: 
            print "Stopping record" 
            print "[Record] ",
            gesture_list.append(listener.stop_recording())
        else: 
            print " ** Recording ** "
            print "[Stop] ",
            listener.start_recording()


if __name__ == '__main__':
    print """Usage:
            learn       : Learn a new gesture 
            recognize   : Let the program guess what you are trying to input 
            q           : Quit""" 
    print "[Command] ",
    while True: 
        command = sys.stdin.readline()
        if "learn" in command: 
            print "Enter the name of the gesture: ", 

            gesture_name = sys.stdin.readline()[:-1]
            gesture_list = []
            listen(gesture_list)

        elif "recognize" in command: 
            pass
            print "[Command] ", 
        elif command[0] == "q": 
            #dumpFeatures(gesture_list, gesture_name)
            dumpFrames(gesture_list, gesture_name)
            print "Goodbye"
            break
        elif "load" in command: 
            pass
            print "[Command] ",
        else: 
            print """Unrecognized command, usage:
            learn       : Learn a new gesture 
            recognize   : Let the program guess what you are trying to input 
            q           : Quit""" 
            print "[Command] ",


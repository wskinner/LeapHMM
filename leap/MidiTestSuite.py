from time import sleep
from MidiInterface import *
inter = MidiInterface()
inter.play_track(1)
for x in range(120, 200):
    inter.set_tempo(x)
    sleep(.1)
for x in range(200, 120, -1):
    inter.set_tempo(x)
    sleep(.1)
for x in range(127, 0, -1):
    inter.vol_track(1, x)
    sleep(.1)
for x in range(0, 127):
    inter.vol_track(1, x)
    sleep(.1)
inter.stop_track(1)

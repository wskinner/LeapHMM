import socket
import sys
import math

class MidiInterface():
    def __init__(self, port=20000, host=''):
        self.HOST = host
        self.PORT = port
        self.BUFSIZE = 1024
        self.ADDR = (self.HOST, self.PORT)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    def send(self, data):
            self.sock.sendto(data, self.ADDR)
    def set_tempo(self, bpm):
        y = 127.0/(250-50)
        x = y*(bpm-50)
        x = int(math.floor(x))
        if x > 127: x=127
        self.send("/tempo %d" % x)
    def stop_track(self, track_num):
        data = "/track%d /stop 127" % track_num
        self.send(data)
    def play_track(self, track_num):
        data = "/track%d /play 127" % track_num
        self.send(data)
    def vol_track(self, track_num, vol):
        data = "/track%d /vol %d" % (track_num, vol)
        self.send(data)
        

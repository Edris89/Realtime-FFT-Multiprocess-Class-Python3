import multiprocessing
from multiprocessing import Queue
import pyaudio
import numpy as np
import time


# Created by Edris89
# Version: Alpha Version
# Githubpage: https://github.com/Edris89/Realtime-FFT-Multiprocess-Class-Python3
# Date: June 14, 2019
# Licensed under the MIT License

class PeakTask(multiprocessing.Process):
    
    def __init__(self,frames_per_buffer, debug, fps):
        multiprocessing.Process.__init__(self)
        self.exitProcess = multiprocessing.Event()
        print("Starting FFT Task")
        
        self.frames_per_buffer = frames_per_buffer
        self.maxValue = 2**16
        self.bars = 35

        #Multiprocess Queue
        self.queue = Queue()

        #Boolean Settings
        self.debug = debug
        self.fps = fps

    def run(self):
        p=pyaudio.PyAudio()
        stream=p.open(format=pyaudio.paInt16,channels=2,rate=44100,
              input=True, frames_per_buffer=self.frames_per_buffer)
        
        if(self.fps):
            start_time = time.time()        # Get the start time so that we can use it later on to calculate with it
            x = 1                           # Displays the frame rate every 1 second
            counter = 0                     # Set the counter variable to zero
        
        while not self.exitProcess.is_set():
            try:
                
                data = np.fromstring(stream.read(self.frames_per_buffer),dtype=np.int16)
                dataL = data[0::2]
                dataR = data[1::2]
                peakL = np.abs(np.max(dataL)-np.min(dataL))/self.maxValue
                peakR = np.abs(np.max(dataR)-np.min(dataR))/self.maxValue
                
                self.queue.put([peakL,peakR])

                if(self.debug):
                    lString = "#"*int(peakL*self.bars)+"-"*int(self.bars-peakL*self.bars)
                    rString = "#"*int(peakR*self.bars)+"-"*int(self.bars-peakR*self.bars)
                    print("L=[%s]\tpeakL=[%f]\tpeakR=[%f]\tR=[%s]"%(lString, peakL , peakR ,rString))
                
                if(self.fps):
                    counter+=1
                    if (time.time() - start_time) > x :
                        print("FPS: ", counter / (time.time() - start_time))
                        counter = 0
                        start_time = time.time()
            except KeyboardInterrupt:
                stream.stop_stream()
                stream.close()
                p.terminate()
                self.shutdown()
        
        stream.stop_stream()
        stream.close()
        p.terminate()
        print("You exited!")

    def shutdown(self):
        self.exitProcess.set()
        print("Shutdown initiated")
    
    def getFromQueue(self):
        return self.queue.get()
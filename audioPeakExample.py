import RFFT



try:
    process = RFFT.PeakTask(frames_per_buffer=1024, debug=False, fps=False)
    process.start()
    
    while(True):
        try:
            dataFromQueue = process.getFromQueue()
            valueL = dataFromQueue[0] #The first in the list is the left audio peak. A float from 0.0 to 1.0
            valueR = dataFromQueue[1] #The second in the list is the right audio peak. A float from 0.0 to 1.0
            print("valueL:[%f]\tvalueR:[%f]"%(valueL, valueR))
            
        except KeyboardInterrupt:
            process.shutdown()        
            break
except KeyboardInterrupt:
    process.shutdown()









import RFFT

apiServerProcess = RFFT.APITask(debug=True, host="192.168.178.24", port=5000)
apiServerProcess.start()

while(True):
    try:
        pass
        
    except KeyboardInterrupt:
        apiServerProcess.shutdown()
        print("Shutting down")
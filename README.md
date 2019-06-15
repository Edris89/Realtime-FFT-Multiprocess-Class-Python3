# Realtime-FFT-Multiprocess-Class-Python3

***The library is in Alpha phase and only tested on Ubuntu 19.04 with Python 3.7.3***

This library taps into the pulseaudio PC audio stream to do Realtime FFT on. It spawns a new process and uses a Queue to talk with the parent process.



**Caution before going further !**

I cannot guarantee that this will not break some of your sound settings.
The class uses pyaudio to tap into the pc audio stream.
You will need to install pulseaudio server or pulseaudio volume control GUI. You can find more information how to install below

## Table of Contents

- [Realtime-FFT-Multiprocess-Class-Python3](#realtime-fft-multiprocess-class-python3)
  - [Table of Contents](#table-of-contents)
  - [Methods](#methods)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installing](#installing)
    - [Running the audioPeakExample](#running-the-audiopeakexample)
    - [Using the class in your own custom script](#using-the-class-in-your-own-custom-script)
  - [HTTP API](#http-api)
    - [Prerequisites](#prerequisites-1)
    - [How to use basic methods](#how-to-use-basic-methods)
    - [API Routes](#api-routes)
      - [PeakTask Routes](#peaktask-routes)
  - [Versioning](#versioning)
  - [Authors](#authors)
  - [License](#license)


## Methods

The library is still in development and for now it only has 1 Task
* PeakTask (This will calculate the peak of the left and right channels pc audio stream.)


In development:
* HTTP API (Spawns a flask server that will listen to http requests, all methods will have support)
## Getting Started 


### Prerequisites

The program is reading the audio buffer from pulseaudio
althoug the normal soundserver is ALSA on Ubuntu, I went for the pulseaudio for easy access to the audio stream

There are 2 options to use pulseaudio
1 is without the GUI
1 is with a GUI

**I cannot guarantee that this will not break some of your sound settings.** I am using Ubuntu 19.04 and the GUI version.

You have to install one of the following packages!
To install pulseaudio server .
```
sudo apt update
sudo apt upgrade
sudo apt install pulseaudio
```

To install pulseaudio volume control.
```
sudo apt install pavucontrol
```

For more information visit the following website [Pulse Audio Ubuntu](https://linuxhint.com/pulse_audio_sounds_ubuntu/)

Library's that are used by the class. You must install the following.

```
sudo apt update
sudo apt upgrade
sudo apt install python3-pip 
pip3 install wheel
pip3 install PyAudio
pip3 install numpy
```

### Installing

Make sure you installed the prerequisites before going further.


Step 1: Clone this repository
```
git clone https://github.com/Edris89/Realtime-FFT-Multiprocess-Class-Python3.git
```

Step 2: cd into the directory

```
cd Realtime-FFT-Multiprocess-Class-Python3
```

Step 3: Done! 
We can now make our own script and use the class or use the audioPeakExample.py that is provided.

### Running the audioPeakExample

Step 1: Cd into examples
```
cd examples
```
Step 2: execute the python3 audioPeakExample script
```
python3 audioPeakExample.py
```

If all went good you should see the following printout in the terminal
```
valueL:[0.363205]	valueR:[0.426743]
```

**To exit the script use Ctr+C this ensures that the spawned child process will properly shutdown**


### Using the class in your own custom script

Important!: Copy examples/RFFT.py to the location where your script is before using it otherwise it can not import it and you will get a error.

Assuming you have copied the example/RFFT.py to the location where your script is. Import RFFT
```
import RFFT
```

Initialize the class for the peak audio. For now this is the only Task supported.
```
process = RFFT.PeakTask(frames_per_buffer=1024, debug=False, fps=False)
```

To start the process use
```
process.start()
```
To stop the process use
```
process.shutdown()
```
To get values from the process Queue use
```
#This returns a list [leftPeak, rightPeak]
dataFromQueue = process.getFromQueue()
valueL = dataFromQueue[0] #The first in the list is the left audio peak. A float from 0.0 to 1.0
valueR = dataFromQueue[1] #The second in the list is the right audio peak. A float from 0.0 to 1.0
```
To see debugging output on the terminal use
```
process = RFFT.PeakTask(frames_per_buffer=1024, debug=True, fps=False)
```
To print the FPS count every second use
```
process = RFFT.PeakTask(frames_per_buffer=1024, debug=False, fps=True)
```

## HTTP API 

### Prerequisites

For this to work you will need the Flask package
Flask is a microframework for Python based on Werkzeug, Jinja 2.
For more information visis their [Flask Website](http://flask.pocoo.org/)

You can install Flask by the following command
```
pip3 install Flask
```
### How to use basic methods

First copy the examples/RFFT.py to where your script is located then in your 
script import RFFT
```
import RFFT
```
To initialize the class, see the following example

You must provide debug, host and port otherwise it won't start the process.
```
apiServerProcess = RFFT.APITask(debug=True, host="192.168.178.24", port=5000)

```

To start the API Process
```
apiServerProcess.start()
```
To stop the API Process
```
apiServerProcess.shutdown()
```
### API Routes

#### PeakTask Routes
Start PeakTask Route
```
http://localhost:5000/startPeakTask
```
Stop PeakTask Route
```
http://localhost:5000/stopPeakTask
```




## Versioning

* Alpha State

## Authors

* **Edris89**


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details




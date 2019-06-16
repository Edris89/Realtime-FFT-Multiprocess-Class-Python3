# Realtime-FFT-Multiprocess-Class-Python3

***The library is in Alpha phase and only tested on Ubuntu 19.04 with Python 3.7.3***

This library taps into the pulseaudio PC audio stream to do Realtime FFT on. It spawns a new process and uses a Queue to talk with the parent process.



**Caution before going further !**

I cannot guarantee that this will not break some of your sound settings.
The class uses pyaudio to tap into the pc audio stream.
You will need to install pulseaudio volume control GUI. You can find more information how to install below

## Table of Contents

- [Realtime-FFT-Multiprocess-Class-Python3](#realtime-fft-multiprocess-class-python3)
  - [Table of Contents](#table-of-contents)
  - [Methods](#methods)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installing](#installing)
    - [Configuring the Pulse Audio Volume Control GUI](#configuring-the-pulse-audio-volume-control-gui)
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
although the normal soundserver is ALSA on Ubuntu, I went for the pulseaudio for easy access to the audio stream.

**I cannot guarantee that this will not break some of your sound settings.** I am using Ubuntu 19.04 and the GUI version.


I **recommend** to install the gui. This way you can easily change on what to monitor for the audio stream.
To install pulseaudio volume control gui.
```
sudo apt update
sudo apt upgrade
sudo apt install pavucontrol
```

Library's that are used by the class. You must install the following.

```
sudo apt update
sudo apt upgrade
sudo apt install python3-pip 
pip3 install wheel
For PyAudio use sudo apt-get install python3-pyaudio
because pip3 install PyAudio somehow seems to fail.
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
You can now configure pulseaudio volume control.

### Configuring the Pulse Audio Volume Control GUI


**Step 1:** Start the volume control program by searching for PulseAudio in your system.

You will get something like this.


Image 1: PulseAudio Volume Control
![Volume Control](https://github.com/Edris89/Realtime-FFT-Multiprocess-Class-Python3/blob/master/images/volume_control_recording.png?raw=true)

**Step 2:** As you can see no application is recording audio. But we can change that. We start our audioPeakExample.py in the terminal by going into the **examples** folder.
```
python3 audioPeakExample.py
```
You will get something like this.

Image 2: audioPeakExample.py in examples folder
![Terminal example](https://github.com/Edris89/Realtime-FFT-Multiprocess-Class-Python3/blob/master/images/audioPeakExample.png?raw=true)

**Step 3:** Go back to PulseAudio Volume Control but let the script **run** ! and you will see something like this (Image 3) when the example is running.

Image 3: audioPeakExample.py in examples folder
![Pulse Audio Volume Control](https://github.com/Edris89/Realtime-FFT-Multiprocess-Class-Python3/blob/master/images/pulse_audio_volume_control.png?raw=true)
As you can see there is now a application available. That's our script. Now click on the Monitor of Scarlett button, now in your case this may be different ! 

That **will** look something like this.

Image 4: Monitor of your sounddriver
![Monitor source](https://github.com/Edris89/Realtime-FFT-Multiprocess-Class-Python3/blob/master/images/Choose%20Monitor.png?raw=true)

You should choose only devices that start with **Monitor**. In my case this was Monitor of Scarlett Solo USB Analog Stereo and as you can see I already applied that.
Luckily this setting has to be set only once. You can now start your script anytime and pulseaudio will automatically assign the choosen device.

**Final:** Play some music and you should now see realtime changes in the terminal.

For more information visit the following website [Pulse Audio Ubuntu](https://linuxhint.com/pulse_audio_sounds_ubuntu/)

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




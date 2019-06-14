# Realtime-FFT-Multiprocess-Class-Python3

This library taps into the pulseaudio PC audio stream to do Realtime FFT on. It spawns a new process and uses a Queue to talk with the parent process.


**Caution before going further !**

I cannot guarantee that this will not break some of your sound settings.
The class uses pyaudio to tap into the pc audio stream.
You will need to install pulseaudio server or pulseaudio volume control GUI. You can find more information how to install below

## Getting Started 


### Prerequisites

The program is reading the audio buffer from pulseaudio
althoug the normal soundserver is ALSA on Ubuntu, I went for the pulseaudio for easy access to the audio stream

There are 2 options to use pulseaudio
1 is without the GUI
1 is with a GUI

**I cannot guarantee that this will not break some of your sound settings.** I am using Ubuntu 19.04 and the GUI version.

You have to install one of the following packages!
To install pulseaudio server 
```
sudo apt update
sudo apt upgrade
sudo apt install pulseaudio
```

To install pulseaudio volume control
```
sudo apt install pavucontrol
```

For more information visit https://linuxhint.com/pulse_audio_sounds_ubuntu/

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

Make sure you installed the prerequisites before going further


Step 1: Clone this repository
```
git clone https://github.com/Edris89/Realtime-FFT-Multiprocess-Class-Python3.git
```

Step 2: cd into the directory

```
cd Realtime-FFT-Multiprocess-Class-Python3
```

Step 3: Done! 
We can now make our own script and use the class or use a the audioPeakExample.py that is provided.

## Running the audioPeakExample

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


## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Edris89** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc


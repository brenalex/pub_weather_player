# pub_weather_player

Generative music project focused on taking weather data as a seed and creating music based off of it.

Notes:
This project makes use of the python music21 library and the python easygui library, as well as the random library. 
Additionally the show('midi') function from music21 only works on Windows OS with Quicktime player. On other systems, the midi files can still be generated, but they will need to be played using other software (e.g. GarageBand).

Use:
pip install -r requirements.txt

to install all libraries used in this project. 

To run normally, simply run 'main_logic.py' using your code editor (VSCode was used for this project, and this has not been tested with other editors). A series of windows will pop up allowing you to select parameters for music generation.

To modify the generation, you can make changes to the parameters in main_logic.py lines 60-98. This will alter things like:

1. key
2. melody_mode                                 
3. melody_freq                                 
4. repetition_coefficient                      multiplier to increase chance of repetition (high number is more likely to repeat)
5. transposition_coefficient                   range for randint transposition function (lower # means more likely to transpose)
6. transposition_weights                       array of length 2 and sum of 100. first number is % chance to transpose up, second number is % chance to transpose down.

A note on melody_mode and melody_freq:

melody_mode can be set to 0 or 1. 0 means that the melody will be generated with only notes from the current chord, 1 means that any note from the key can be generated. 

melody_freq can be set to 0, 1, or 2. 0 means that a note will be generated every beat, 1 means that every note has a 50% chance to be a rest, and 2 means that every note has a 25% chance to be a rest. This can control how much "space" your composition has. 

Naturally these options can be expanded, but these are their only current options. 

To test certain presets, simply hard-code the weather_type variable to test your selection.

For even further customization, you can modify the transformations.py file to add transformations, or alter the way melody or chords are generated. For example, you could construct your own chord tree to try out theoretical musical concepts, or add new possible values for melody_mode, perhaps ones that allow notes out of the key to be generated. Here, the sky is the limit. 

Enjoy generating music!


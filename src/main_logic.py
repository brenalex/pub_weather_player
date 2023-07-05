import sys
import os
from music21 import *
from random import choices, randint
from easygui import *

from transformations import *
from weather_data import *

key_transforms = [transpose_up, transpose_down]

#Start up gui
#Get user input
title = "Weather Player"

message = "Welcome to weather player! Weather player takes current weather data, and uses that to generate music based on a set of rules and elements of randomness. Perfect for ambient listening!"

button = "Get Started"

# A nice welcome message
ret_val = msgbox(message, title, button)
if ret_val is None: # User closed msgbox
    sys.exit(0)

city_choices = ["Austin", "Beijing", "Boston", "Hong Kong", "Lagos", "London", "Manchester", "New York", "Riyadh", "Seoul", "Singapore"]
city = choicebox("What city's weather would you like to listen to?", title, city_choices)
if city is None: #User closed choicebox
    sys.exit(0)


#Pull from weather api
weather_data = init_weather(city)
weather_type = desc2num(weather_data[0])


num_min = integerbox("How many minutes would you like to generate?", title)
if num_min is None: #User closed integerbox
    sys.exit(0)

msgbox("Please choose where you'd like to save the file:", title)

save_loc = diropenbox("Save to:", title)
if save_loc is None: #User closed diropenbox
    sys.exit(0)

filename = enterbox("Save as: \n (please avoid using special characters, as they will be removed)", title)
if filename is None: #User closed enterbox
    sys.exit(0)

filename = process_filename(filename)

feedback_msg = "The weather in " + city + " is " + weather_data[0] + "! \n Press 'OK' to generate music based on this weather."
msgbox(feedback_msg, title)


finish_msg = "Generating music...\n It will play automatically after this window is closed. To play again later, please check " + save_loc + " for new files."
msgbox(finish_msg, title)


if(weather_type == 0):                              #sunny
    my_key = key.Key('A3')                         #A maj
    melody_mode = 0                                 #melody note generated from solely chord notes
    melody_freq = 0                                 #melody note generated each beat
    repetition_coefficient = 0                      #multiplier to increase repetition
    transposition_coefficient = 1                   #range for randint transposition function (lower # means more likely to transpose)
    transposition_weights = [75, 25]                #likelihood of transposing up vs down

elif(weather_type == 1):                            #cloudy
    my_key = key.Key('b3')                         #B min
    melody_mode = 1                                 #melody note generated from all notes in key
    melody_freq = 1                                 #melody note with 50% chance not to generate each beat
    repetition_coefficient = 2                      #multiplier to increase repetition
    transposition_coefficient = 3                   #range for randint transposition function (lower # means more likely to transpose)
    transposition_weights = [50, 50]                #likelihood of transposing up vs down

elif(weather_type == 2):                            #rainy
    my_key = key.Key("c#3")                        #C# min
    melody_mode = 1                                 #melody note generated from all notes in key
    melody_freq = 2                                 #melody note with 25% chance to not generate each beat
    repetition_coefficient = 1                      #multiplier to increase repetition
    transposition_coefficient = 2                   #range for randint transposition function (lower # means more likely to transpose)
    transposition_weights = [25, 75]                #likelihood of transposing up vs down

elif(weather_type == 3):                            #snow
    my_key = key.Key('B-3')                        #Bb major
    melody_mode = 0                                 #melody note generated from solely chord notes
    melody_freq = 2                                 #melody note with 25% chance to not generate each beat
    repetition_coefficient = 0                      #multiplier to increase repetition
    transposition_coefficient = 1                   #range for randint transposition function (lower # means more likely to transpose)
    transposition_weights = [75, 25]                #likelihood of transposing up vs down

elif(weather_type == 4):                            #storm
    my_key = key.Key('d#3')                         #D# min
    melody_mode = 1                                 #melody note generated from all notes in key
    melody_freq = 0                                 #melody note generated each beat
    repetition_coefficient = 0                      #multiplier to increase repetition
    transposition_coefficient = 1                   #range for randint transposition function (lower # means more likely to transpose)
    transposition_weights = [0, 100]                #likelihood of transposing up vs down


#create streams to be modified
chordstream = stream.Stream()
melodystream = stream.Stream()

#start on root chord
new_chord = create_chord(my_key, my_key.pitches[0])
chordstream.append(new_chord[0])
add_melody(melodystream, my_key, new_chord[0], new_chord[1], melody_mode, melody_freq)

#while less than user-entered time
#  it is important to note here that all streams are created at 120bpm
#  this was calculated by observing output and monitoring duration
#  we will use duration and bpm knowledge to turn that into real minutes
current_duration = chordstream.duration
while int(current_duration.quarterLength) < (120 * num_min):

    #create a chord progression to iterate over
    current_prog = create_chord_progression(my_key)
    num_prog_loops = randint(1, (2 + repetition_coefficient))               # Type of weather effects how likely a progression is to repeat

    #stay in this chord progression for random amount of time
    for x in range(num_prog_loops):
        #cycle through current chord progression, 
        # adding each chord to the stream
        # and creating and adding melody for each chord
        for chord in current_prog:
            new_chord = create_chord(my_key, chord)
            chordstream.append(new_chord[0])
            add_melody(melodystream, my_key, new_chord[0], new_chord[1], melody_mode, melody_freq)

    #chance to transpose or to create new chord progression
    coin = randint(0, transposition_coefficient)                            # Type of weather effects how likely tranposition is
    #transpose (this updates the key for the next loop and prog creation)
    if coin == 1:
        transform_list = [0, 1]
        transform_num = choices(transform_list, weights=transposition_weights, k=1)     # Weather type effects likelihood of transposing up/down
        my_key = key_transforms[transform_num[0]](my_key)                               #transpose and update key with return value
        my_key = key.Key(correct_transposition(my_key))
    current_duration = chordstream.duration

#save music to file
total_stream = stream.Stream()
total_stream.insert(0, chordstream)
total_stream.insert(0, melodystream)

save_loc = os.path.join(save_loc, filename)
fp = total_stream.write('midi', fp=save_loc)

#output generated music
total_stream.show('midi')


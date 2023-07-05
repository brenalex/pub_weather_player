from music21 import *

from random import choices, randint

from tree import *

chord_tree = NonBinTree(1)
chord_tree.add_node(2)        #chord_tree.nodes[0]
chord_tree.add_node(3)        #chord_tree.nodes[1]
chord_tree.add_node(4)        #chord_tree.nodes[2]
chord_tree.add_node(5)        #chord_tree.nodes[3]
chord_tree.add_node(6)        #chord_tree.nodes[4]
chord_tree.add_node(7)        #chord_tree.nodes[5]
############################################################1->2##########################################################
# 1 -> 2 ->(5 || 7) (->(7||1) -> 1)
# 5-> (1 || 7)
# 7-> 1
chord_tree.nodes[0].add_node(5)
chord_tree.nodes[0].add_node(7)

#five ending
chord_tree.nodes[0].nodes[0].add_node(7)
chord_tree.nodes[0].nodes[0].add_node(1)

chord_tree.nodes[0].nodes[1].add_node(1)

chord_tree.nodes[0].nodes[0].nodes[0].add_node(1)


############################################################1->3##########################################################
# 1 -> 3 -> (6 || 4) -> (2 || 4) -> (5 || 7)
chord_tree.nodes[1].add_node(6)
chord_tree.nodes[1].add_node(4)

chord_tree.nodes[1].nodes[0].add_node(2)
chord_tree.nodes[1].nodes[0].add_node(4)

chord_tree.nodes[1].nodes[1].add_node(5)
chord_tree.nodes[1].nodes[1].add_node(7)
chord_tree.nodes[1].nodes[1].add_node(2)


chord_tree.nodes[1].nodes[0].nodes[0].add_node(5)
chord_tree.nodes[1].nodes[0].nodes[0].add_node(7)
chord_tree.nodes[1].nodes[0].nodes[1].add_node(5)
chord_tree.nodes[1].nodes[0].nodes[1].add_node(7)
chord_tree.nodes[1].nodes[0].nodes[1].add_node(2)

# 4-> 5, 7 branch
chord_tree.nodes[1].nodes[1].nodes[0].add_node(7)
chord_tree.nodes[1].nodes[1].nodes[0].add_node(1)


chord_tree.nodes[1].nodes[1].nodes[1].add_node(1)


chord_tree.nodes[1].nodes[1].nodes[0].nodes[0].add_node(1)
chord_tree.nodes[1].nodes[1].nodes[1].add_node(1)

# 4 to 2 branch upper
chord_tree.nodes[1].nodes[1].nodes[2].add_node(5)
chord_tree.nodes[1].nodes[1].nodes[2].add_node(7)

chord_tree.nodes[1].nodes[1].nodes[2].nodes[0].add_node(7)
chord_tree.nodes[1].nodes[1].nodes[2].nodes[0].add_node(1)

chord_tree.nodes[1].nodes[1].nodes[2].nodes[0].nodes[0].add_node(1)

chord_tree.nodes[1].nodes[1].nodes[2].nodes[1].add_node(1)

#4 branch lower
chord_tree.nodes[1].nodes[0].nodes[1].nodes[0].add_node(7)
chord_tree.nodes[1].nodes[0].nodes[1].nodes[0].add_node(1)

chord_tree.nodes[1].nodes[0].nodes[1].nodes[0].nodes[0].add_node(1)

chord_tree.nodes[1].nodes[0].nodes[1].nodes[1].add_node(1)

chord_tree.nodes[1].nodes[0].nodes[1].nodes[2].add_node(5)
chord_tree.nodes[1].nodes[0].nodes[1].nodes[2].add_node(7)

chord_tree.nodes[1].nodes[0].nodes[1].nodes[2].nodes[0].add_node(7)
chord_tree.nodes[1].nodes[0].nodes[1].nodes[2].nodes[0].add_node(1)

chord_tree.nodes[1].nodes[0].nodes[1].nodes[2].nodes[1].add_node(1)
chord_tree.nodes[1].nodes[0].nodes[1].nodes[2].nodes[0].nodes[0].add_node(1)

#2 branch
chord_tree.nodes[1].nodes[0].nodes[0].nodes[0].add_node(7)
chord_tree.nodes[1].nodes[0].nodes[0].nodes[0].add_node(1)

chord_tree.nodes[1].nodes[0].nodes[0].nodes[1].add_node(1)

chord_tree.nodes[1].nodes[0].nodes[0].nodes[0].nodes[0].add_node(1)

############################################################1->4##########################################################
# 1 -> 4 -> (5 ||7)
chord_tree.nodes[2].add_node(5)
chord_tree.nodes[2].add_node(7)
chord_tree.nodes[2].add_node(2)

chord_tree.nodes[2].nodes[0].add_node(7)
chord_tree.nodes[2].nodes[0].add_node(1)

chord_tree.nodes[2].nodes[0].nodes[0].add_node(1)

chord_tree.nodes[2].nodes[1].add_node(1)

chord_tree.nodes[2].nodes[2].add_node(5)
chord_tree.nodes[2].nodes[2].add_node(7)

chord_tree.nodes[2].nodes[2].nodes[0].add_node(7)
chord_tree.nodes[2].nodes[2].nodes[0].add_node(1)

chord_tree.nodes[2].nodes[2].nodes[0].nodes[0].add_node(1)

chord_tree.nodes[2].nodes[2].nodes[1].add_node(1)

############################################################1->5##########################################################
chord_tree.nodes[3].add_node(7)
chord_tree.nodes[3].add_node(1)
chord_tree.nodes[3].nodes[0].add_node(1)

############################################################1->6##########################################################
# 1 -> 6 -> (2 || 4) -> (5 || 7)
chord_tree.nodes[4].add_node(2)
chord_tree.nodes[4].add_node(4)

chord_tree.nodes[4].nodes[0].add_node(5)
chord_tree.nodes[4].nodes[0].add_node(7)
chord_tree.nodes[4].nodes[1].add_node(5)
chord_tree.nodes[4].nodes[1].add_node(7)
chord_tree.nodes[4].nodes[1].add_node(2)

chord_tree.nodes[4].nodes[0].nodes[0].add_node(7)
chord_tree.nodes[4].nodes[0].nodes[0].add_node(1)

chord_tree.nodes[4].nodes[0].nodes[1].add_node(1)

chord_tree.nodes[4].nodes[1].nodes[0].add_node(7)
chord_tree.nodes[4].nodes[1].nodes[0].add_node(1)

chord_tree.nodes[4].nodes[1].nodes[1].add_node(1)

chord_tree.nodes[4].nodes[1].nodes[2].add_node(5)
chord_tree.nodes[4].nodes[1].nodes[2].add_node(7)

chord_tree.nodes[4].nodes[0].nodes[0].nodes[0].add_node(1)
chord_tree.nodes[4].nodes[1].nodes[0].nodes[0].add_node(1)

chord_tree.nodes[4].nodes[1].nodes[2].nodes[0].add_node(7)
chord_tree.nodes[4].nodes[1].nodes[2].nodes[0].add_node(1)

chord_tree.nodes[4].nodes[1].nodes[2].nodes[1].add_node(1)

chord_tree.nodes[4].nodes[1].nodes[2].nodes[0].nodes[0].add_node(1)

############################################################1->7##########################################################
chord_tree.nodes[5].add_node(1)
chord_tree.nodes[5].add_node(6)

chord_tree.nodes[5].nodes[1].add_node(2)
chord_tree.nodes[5].nodes[1].add_node(4)

chord_tree.nodes[5].nodes[1].nodes[0].add_node(5)
chord_tree.nodes[5].nodes[1].nodes[0].add_node(7)
chord_tree.nodes[5].nodes[1].nodes[1].add_node(5)
chord_tree.nodes[5].nodes[1].nodes[1].add_node(7)
chord_tree.nodes[5].nodes[1].nodes[1].add_node(2)

chord_tree.nodes[5].nodes[1].nodes[0].nodes[0].add_node(7)
chord_tree.nodes[5].nodes[1].nodes[0].nodes[0].add_node(1)
chord_tree.nodes[5].nodes[1].nodes[0].nodes[1].add_node(1)

chord_tree.nodes[5].nodes[1].nodes[1].nodes[0].add_node(7)
chord_tree.nodes[5].nodes[1].nodes[1].nodes[0].add_node(1)


chord_tree.nodes[5].nodes[1].nodes[1].nodes[1].add_node(1)

chord_tree.nodes[5].nodes[1].nodes[1].nodes[2].add_node(5)
chord_tree.nodes[5].nodes[1].nodes[1].nodes[2].add_node(7)

chord_tree.nodes[5].nodes[1].nodes[0].nodes[0].nodes[0].add_node(1)

chord_tree.nodes[5].nodes[1].nodes[1].nodes[0].nodes[0].add_node(1)

chord_tree.nodes[5].nodes[1].nodes[1].nodes[2].nodes[0].add_node(7)
chord_tree.nodes[5].nodes[1].nodes[1].nodes[2].nodes[0].add_node(1)
chord_tree.nodes[5].nodes[1].nodes[1].nodes[2].nodes[1].add_node(1)

chord_tree.nodes[5].nodes[1].nodes[1].nodes[2].nodes[0].nodes[0].add_node(1)

##################################################################################################################################

length_list = [1, 2, 3, 4]

#Function for processing user input for filename
def process_filename(fn):
    fn = fn.replace(" ", "")
    ret_name = ""
    for letter in fn:
        if (letter.isalnum()):
            ret_name = ret_name + letter
    ret_name = ret_name + ".mid"
    return ret_name

def transpose_up(key):
    transposition = randint(1, 2)
    key.transpose(transposition, inPlace=True)
    return key

def transpose_down(key):
    transposition = randint(-2, -1)
    key.transpose(transposition, inPlace=True)
    return key

def correct_transposition(key):
    root = key.pitches[0]
    root = str(root)
    root = root[:-1]
    root = root + "3"
    return root
    
def create_chord_progression(key):
    pitch_arr = key.pitches
    progression_arr = []
    my_root = chord_tree
    #loop iterating down the chord_tree til you reach a leaf
    while not my_root.is_leaf():
        #add a chord from the available chords in chord_tree
        options_list = my_root.these_nodes()
        index = randint(0, len(options_list)-1)
        selection = options_list[index]
        progression_arr.append(pitch_arr[selection-1])
        #iterate deeper into tree
        my_root = my_root.nodes[index]   
    return progression_arr

#Function to create a new chord
#input: key and starting note
#output: [generated chord, duration of chord]

def create_chord(key, start_note):
    #select random chord from key
    pitch_arr = key.pitches
    root = pitch_arr.index(start_note)
    #randomize duration
    dur = choices(length_list, weights=(10, 30, 0, 60), k=1)
    #convert from list type to int
    dur = dur[0]
    #see inversion possibilities here
    inversion = randint(0, 2)
    if inversion == 0:              #root position
        new_chord = chord.Chord([pitch_arr[root], pitch_arr[(root + 2)%7], pitch_arr[(root + 4)%7]], quarterLength=dur)
    elif inversion == 1:            #first inversion
        new_chord = chord.Chord([pitch_arr[(root + 2)%7], pitch_arr[(root + 4)%7], pitch_arr[root]], quarterLength=dur)
    else:                           #second inversion
        new_chord = chord.Chord([pitch_arr[(root + 4)%7], pitch_arr[root], pitch_arr[(root + 2)%7]], quarterLength=dur)
    ret_list = [new_chord, dur]
    return ret_list

#Function to create a melody for a given chord
#input: stream (to be appended to), key, chord, duration (how many notes to generate), mode, and frequency
#Mode and Frequency determine which notes are eligible to pull from, and how often to pull notes.
def add_melody(stream, key, chord, duration, mode, frequency):
    for i in range(duration):
        if(frequency == 0):                                     # generate note every beat
            mode_gen(stream, key, chord, mode)

        elif(frequency == 1):                                   # 50% chance to not generate note
            chance = randint(0, 1)
            if (chance == 0):
                stream.append(note.Rest())
            else:
                mode_gen(stream, key, chord, mode)

        else:
            chance = randint(0, 4)
            if (chance == 0):
                stream.append(note.Rest())
            else:
                mode_gen(stream, key, chord, mode)
                

def mode_gen(stream, key, chord, mode):
    #generate using only notes from the chord
    if(mode == 0):
        note_num = randint(0, 2)
        mel_note = note.Note(chord.pitches[note_num])
        mel_note.transpose('P8', inPlace=True)
        stream.append(mel_note)
    #generate using notes from whole key
    else:
        note_num = randint(0, 6)
        mel_note = note.Note(key.pitches[note_num])
        mel_note.transpose('P8', inPlace=True)
        stream.append(mel_note)
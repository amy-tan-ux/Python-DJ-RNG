
"""
DJ RNG 8000 beta

Written by: Amy Tan

Copyright 2022
Updated in 2022

"""

from random import randint
from midiutil import MIDIFile

from MusicCreator import *

""" 
----------------
Start Input
----------------
"""

bars= 8                         # No. of Bars
key = "m_G"                     # Key
scale="major_scale"        # Scale
tempo= 45                      # Tempo - In BPM
emotion = "light"               # Emotion - (light, neutral, dark, jazz, exotic)
volume   = 100                  # 0-127, as per the MIDI standard - fixed
track    = 0
channel  = 0
time     = 0    # In beats

"""
------------------------------
INTRODUCING DJ RNG 8000 Beta
------------------------------
"""

rythm = Rhythm(1)
rythmbar = rythm.beats(4,120)

DJRNG = CreateChord(key, scale, emotion)

#DJRNG.keyChange()

DJRNG.start()

output = []

MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created
                      # automatically)
MyMIDI.addTempo(track, time, tempo)

DJRNG.next_melody(0)

chord =[]
bass =[]

for beat in rythmbar:

    if beat != "x":

        MyMIDI.addNote(track, channel, DJRNG.next_melody(0)[0], time, float(beat)/16, volume)

        if time % 4 ==0:

            if randint(0,5)> 1:

                chord = DJRNG.next_chord()
                bass = DJRNG.next_bass(1)

                for note in chord:
                    MyMIDI.addNote(track, channel, note, time, float(beat)/16, volume)
                
                for note in bass:
                    MyMIDI.addNote(track, channel, note, time, float(beat)/16, volume)


        elif randint(0,4) <2:

            for note in chord:
                MyMIDI.addNote(track, channel, note, time, float(beat)/16, volume)
            
            for note in bass:
                MyMIDI.addNote(track, channel, note, time, float(beat)/16, volume)

        
        time += float(beat) /16

    else:

        time += 1/16



with open("testling7.mid", "wb") as output_file:
   MyMIDI.writeFile(output_file)

"""
print(rythmbar)
print(output)


degrees1  = [64, 67, 71, 71, 64, 60, 60, 60]  # MIDI note numberdegrees
track    = 0
channel  = 0
time     = 0    # In beats
duration = 1    # In beats

MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created
                      # automatically)
MyMIDI.addTempo(track, time, tempo)

for i, pitch in enumerate(output):
     MyMIDI.addNote(track, channel, pitch, time + i, duration, volume)

#for i, pitch in enumerate(degrees1):
    # MyMIDI.addNote(track, channel, pitch, time + i, duration, volume)

with open("major-scale.mid", "wb") as output_file:
   MyMIDI.writeFile(output_file)

"""

"""

chance = randint(0,2)
chunks = min(bars, randint(1,6)) # Number of potential verse/chorus/bridge ect

fillerchuncks = min(randint(chunks, chunks + 4), bars) # Total chuncks to split song into

chunkslen = bars / fillerchuncks

if chance ==1:

    speed = 1

else:
    speed=-1

rhythm  = Rhythm(speed)

# Randomize Harmony for # of Avalible Chunchs
harmony=[0,0,0,0] 
binary =bin(randint(0,15))[2:]
lenbin = len(binary)

for i in range(0,lenbin):
    harmony[(4-lenbin+ i)]=int(binary[i])


#degrees  = [60, 62, 64, 65, 67, 69, 71, 72]  # MIDI note numberdegrees
degrees1  = [64, 67, 71, 71, 64, 60, 60, 60]  # MIDI note numberdegrees
track    = 0
channel  = 0
time     = 0    # In beats
duration = 1    # In beats
#tempo    = 60   # In BPM
#volume   = 100  # 0-127, as per the MIDI standard

MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created
                      # automatically)
MyMIDI.addTempo(track, time, tempo)

for i, pitch in enumerate(output):
     MyMIDI.addNote(track, channel, pitch, time + i, duration, volume)

#for i, pitch in enumerate(degrees1):
    # MyMIDI.addNote(track, channel, pitch, time + i, duration, volume)

with open("major-scale.mid", "wb") as output_file:
   MyMIDI.writeFile(output_file)

"""
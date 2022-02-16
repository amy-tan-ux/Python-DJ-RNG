import random
from random import randint

from musicDB import theory, mdb_mode, mdb_notetype
from Knapsack import knapsack
# MusicCreator


"""
-----------------------------------------------------------
Tools for Chords, Progressions, Beats and Rhythm
-----------------------------------------------------------

"""

def shift_chord(key, notes, progression):
    # Converting list of Chords to the right degree 
    # key is the relative shift
    chords=dict()
    for i in progression:
        degree = theory.get("interval")[i[0]]
        semitone = (degree[1] + key) % 12 
        chord_set = { x + semitone for x in theory.get("chord")[i[1]]}
        insert_chord = chord_set.intersection(notes)
 
        if insert_chord != set():

            if degree[0] in chords:
                chords[degree[0]] += [insert_chord]
                
            else:
                chords[degree[0]] = [insert_chord]
    
    return chords         # a dictionary of chords that uses notes from notes



""" 
--------------------
Beats and Rhythm 
--------------------
"""

# Generate the time signitures - beats per bar
class Bpb:

  def __init__(self):

    self.bpb=[]

    for i in [1,2,3]:
        rng= randint(0,8) # results 0= 4bpb, 1= 4bpb, 2= 2bpb, 3= 3bpb, 4= 4bpb, 5= 5bpb, 6= 6bpb, 7= 7bpb, 8= 8bpb
        if rng < 2: self.bpb+= [4]      
        else: self.bpb+= [rng]


# probability of note types
class Rhythm:

  def __init__(self, speed): # -1= slow, 1= fast

    self.value=[]
    self.restraint=[]

    for i in range(0,11):
      
      self.value += [randint(1, 111 + (speed * randint(i, i+i) * 5))]
      self.restraint += [randint(0, 11 + (speed * i))]
    
  def beats (self, bpb, no_bars):

    notes_distributed = [] # initalize

    for i in range(no_bars):

      temp_distribution = []
      solution= knapsack(11,self.value, mdb_notetype, self.restraint,bpb * 16)  # mdb_notetype = [10000, 5000, 2500, 1250, 625]

      for i in range(0,11):

        if solution[i] != 0:
          temp_distribution += [mdb_notetype[i] for x in range(solution[i])]
    
      pause= (bpb * 16) - sum(temp_distribution)

      if pause !=0: # rests
      
        temp_distribution += ["x" for x in range(pause)]

      random.shuffle(temp_distribution)
    
      notes_distributed.extend(temp_distribution)

    return notes_distributed



"""
------------------------------------------------
--------MUSIC GUIDE---------------------|-------
----------------------------------|--- X -------
--------------------------|----- X -------------
------------------------ X ---------------------
"""
# (degrees: [destinations])

progression_direct = { 0: {0, 1, 3, 4, 2},
                        1: {0, 2, 1,3},
                        2: {0, 4, 2},
                        3: {2, 4, 3},
                        4: {0, 5, 4},
                        5: {0, 3, 5},
                        6: {0, 5, 6} }

modal_scales = ["major_scale", "dorian_scale", 
                    "phrygian_scale", "lydian_scale", 
                    "mixolydian_scale", "minor_scale", 
                    "locrian_scale"]



class MusicGuide(Bpb): # Creating the music_guide object that DJ RNG will follow

    def __init__(self, key, scale, emotion):

        Bpb.__init__(self)
        self.beats= [Bpb().bpb, Bpb().bpb, Bpb().bpb]
        self.key = theory.get("note")[key]
        self.scale = [[key, scale]]
        self.mode = theory.get("scales")[scale][0]
        self.notes_list = theory.get("scales")[scale][1] # notes in scale
        self.notes_set = (set(self.notes_list).union({x+12 for x in self.notes_list})).union({x-12 for x in self.notes_list})
        self.relchords= theory.get("emotion")[emotion]["chord"]

        progressions= theory.get("emotion")[emotion]["progression"]
        random.shuffle(progressions)
        self.progression= theory.get("progression")[progressions[0]] # list of progression [Degree,Chord]

        if progressions[0] == "major_scale":
            self.major= (1 -self.mode) % len(self.notes_list) # This is the difference between the major and scale

        elif progressions[0] == "minor_scale":
            self.major = ((1 -self.mode) + 6 ) % len(self.notes_list)
        
        else:
            self.major = 0
        
        self.keychangeCount = 0
    
    def keyChange (self): # Following common key change / modulation practice : https://www.youtube.com/watch?v=QGFvTlA1l8k&list=PLvITZfqtzAnVpv3_u_3LYzYCUUZyR5Mfl&index=6
        
        current_scale = self.scale[self.keychangeCount][1]
        rng_change = randint(0,9)

        if rng_change > 6:
            # Relative Modulation
            new_mode = randint(1,7)
            change_mode = (new_mode - self.mode) % 7
            self.keychange = self.notes_list[change_mode]
            self.key += self.keychange

            new_scale= mdb_mode[new_mode]
            self.major = (1 -self.mode) % len(self.notes_list)
            self.progression= theory.get("progression")["major_scale"]
            self.notes_list = theory.get("scales")[new_scale][1] # notes in scale
            self.notes_set = {x-12 for x in self.notes_list}.union(set(self.notes_list).union({x+12 for x in self.notes_list}))
            
            self.scale += [[self.key, new_scale]]
            self.mode = new_mode

        elif rng_change > 3:

            # Different Key Same Scale Same Progression
            self.keychange = self.notes_list[ randint(0,len(self.notes_list))-1]
            self.key += self.keychange
            
            self.scale += [[self.keychange, current_scale]]

        else:
            
            # Change by degree (3, 5, )
            shift = self.progression[randint(0, len(self.progression))-1]
            self.keychange = theory.get("interval")[shift[0]][1]
            self.key += self.keychange
            
            self.major = 0

            if "maj" in shift[1]:
                self.progression= theory.get("progression")["major_scale"]
                self.scale += [[self.keychange, "major_scale"]]
            
            else:
                self.progression= theory.get("progression")["minor_scale"]
                self.scale += [[self.keychange, "minor_scale"]]

        self.keychangeCount += 1
        print(self.scale)

"""
------------------------------------
CREATING MUSIC
------------------------------------
"""

class CreateChord(MusicGuide): 

    def __init__(self, key, scale, emotion):
    # chords extracted for each degree

        MusicGuide.__init__(self, key, scale, emotion)

        chance = randint(0, len(self.relchords))
        tonic_chords=[]

        if chance > 0: # Random chords based on emotions
            random.shuffle(self.relchords)
            morechords = self.relchords[:chance]
            for x in morechords:
                insert_tonic_chords= theory.get("chord")[x].intersection(self.notes_set)
                if insert_tonic_chords != set():
                    tonic_chords += [insert_tonic_chords]# List of Chords
        
        self.chords = shift_chord(self.major, self.notes_set, self.progression)
        
        if tonic_chords != set():

            if 0 not in set(self.chords.keys()):
                self.chords[0]= tonic_chords
        
            else: 
                self.chords[0]+= tonic_chords # a dictionary of chords in a degree
        
        self.range = [randint(0,1) * (-1), 0 , randint(0,1), randint(0,1)] 
        # octave relative to chord [-bass, chord, +melody, +harmony]

        self.tones = list(self.chords.keys()) # list of tones in progression
    
    def start(self): # like __iter__ initializes iterations

        self.starTone = self.tones[max( 0, randint(0, len(self.tones))-1)]
        self.melTone = self.starTone
        self.bassTone = self.starTone
        
        chord = self.chords[self.starTone] # list of chords from degree starTone
        random.shuffle(chord)
        useChord = list(chord[0]) # a set of notes in a chord
        random.shuffle(useChord)

        if len(useChord) < 2:
            self.storeChord =  [useChord[0] + self.key]
            self.storeBass = [useChord[0] + self.key + self.range[0]]
        else:
            chordSize = randint(1,len(useChord)-1)
            self.storeChord = [x + self.key for x in useChord[:chordSize]]
            self.storeBass = [x + self.key + self.range[0] for x in useChord[:chordSize]]


        self.storeMelody = [useChord[0] + self.key + self.range[2]]
        self.storeHarmony = [useChord[0] + self.key + self.range[3]]

        return self


    def same_chord(self):
        return self.storeChord
    
    def same_melody(self):
        return self.storeMelody
    
    def same_harmony(self):
        return self.storeHarmony
    
    def same_bass(self):
        return self.storeBass
    
    # Iterating through the notes
    def next_bass(self, refresh):

        if refresh == 1:
            self.bassTone = self.starTone

        direct = set(progression_direct[self.bassTone]).intersection(set(self.tones))

        if direct != set():
            direct=list(direct)
            random.shuffle(direct)
            self.bassTone = direct[0]

            chord = self.chords[self.bassTone] # list of chords

            if len(chord) != 0:

                random.shuffle(chord)
                useChord = list(chord[0]) # a set of notes in a chord

                random.shuffle(useChord)
                if len(useChord) < 2:
                    self.storeBass = [useChord[0] + self.key + self.range[0]]
                else:
                    chordSize = randint(1,len(useChord)-1)
                    self.storeBass = [x + self.key + ( 12 * self.range[0]) for x in useChord[:chordSize]]
        
        return self.storeBass

    def next_chord(self):

        direct = set(progression_direct[self.starTone]).intersection(set(self.tones))

        if direct != set():
            direct=list(direct)

            random.shuffle(direct)
            self.starTone = direct[0]

            chord = self.chords[self.starTone] # list of chords from degree starTone
            random.shuffle(chord)
            useChord = list(chord[0]) # a set of notes in a chord

            if len(useChord) != 0:

                random.shuffle(useChord)
                if len(useChord) < 2:
                    self.storeChord = [useChord[0] + self.key]
                else:
                    chordSize = randint(1,len(useChord)-1)
                    self.storeChord = [x + self.key  for x in useChord[:chordSize]]
        
        return self.storeChord


    def next_melody(self, refresh): # refresh = 0 means to deviate, =1 means to return to starTone

        if refresh == 1:
            self.melTone = self.starTone

        # direct the melody using progression_direct    
            direct = progression_direct[self.melTone].intersection(set(self.tones))

            if direct != set():
                direct=list(direct)
        
                random.shuffle(direct)
                self.melTone = direct[0]
        
        elif self.melTone - 6 < 0:

            self.melTone = (self.melTone +  randint(0, 5))
        

        elif randint(0,100) < 2 :

            if self.melTone + 7 >21:

                self.melTone = (self.melTone + ((-1) * randint(0, 4)))

            else:
                
                self.melTone = (self.melTone + (((-1) **(randint(0,1))) * randint(0, 7))) % 21

        elif self.melTone + 4 > 15:

            self.melTone = (self.melTone + ((-1) * randint(0, 4)))
        
        else:

            self.melTone = (self.melTone + (((-1) **(randint(0,1))) * randint(0, 4)))
        
        note = sorted(list(self.notes_set))[self.melTone] 
        self.storeMelody = [(note + self.key) + (12* self.range[2])]  

        return self.storeMelody 

  
    
    def next_harmony(self):

        direct = progression_direct[self.melTone].intersection(set(self.tones))

        if direct != set():
            direct=list(direct)

            random.shuffle(direct)

            note = list(self.notes_set)[self.melTone] 
            self.storeHarmony = [(note + self.key) + (12 * self.range[3])]

        return self.storeHarmony

"""
---------------------------------
 Chord Progression & Degrees 
---------------------------------

Turning each degree into nodes
Connecting the nodes according to music theory
 
["tonic", "supertonic", "mediant", 
 "subdominant", "dominant", "submediant", "leadingnote", "tonicOctv"] 


# (degrees: [destinations])
progression_direct = { "tonic": ["tonic", "subdominant", "dominant", "mediant"],
                        "supertonic": ["tonic", "mediant", "supertonic", "subdominant"],
                        "mediant": ["tonic", "dominant", "mediant"],
                        "subdominant": ["dominant", "subdominant"],
                        "dominant": ["tonic", "submediant", "dominant"],
                        "submediant": ["tonic", "subdominant", "submediant"],
                        "leadingnote": ["tonic", "submediant", "leadingnote"] }

"""



        
        






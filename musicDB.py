
# Music Theory DB

theory = {

    # ( Note: No. ) | Middle C = m_C = 60
    "note": {"m_C": 60, "m_Db": 61, "m_D": 62, "m_Eb": 63, "m_E": 64,
                "m_F": 65, "m_Gb": 66, "m_G": 67, "m_Ab": 68, "m_A": 69,
                    "m_Bb": 70, "m_B": 71},

    # ( FullScale: [Mode, [ScaleNotes]] )
    "scales": {"major_scale": [1, [0,2,4,5,7,9,11]],
                "dorian_scale": [2, [0,2,3,5,7,9,10]],
                "phrygian_scale": [3, [0,1,3,5,7,8,10]],
                "lydian_scale": [4, [0,2,4,6,7,9,11]],
                "mixolydian_scale": [5, [0,2,4,5,7,9,10]],
                "minor_scale": [6, [0,2,3,5,7,8,10]],
                "locrian_scale": [7,[0,1,3,5,6,8,9]],
                "melodic_minor": [6, [0,2,3,5,7,9,10]],
                "harmonic_scale": [6, [0,2,3,5,6,9,10]],
                "pentatonic_scale": [1, [0,2,4,7,9,13,15]]             
                },

    # ( Interval: [Type, Semitone] )
    "interval": {   "i": [0,0],
                    "I": [0,0], 
                    "ii": [2,1],
                    "II": [2,2],
                    "iii": [3,3],
                    "III": [3,4],
                    "iv": [4,5],
                    "IV": [4,5],
                    "v": [5,7],
                    "V": [5,7],
                    "vi": [6,8],
                    "VI": [6,9],
                    "vii": [5,10],
                    "VII": [5,11],
                    "viii": [0,12],
                    "VIII": [0,12]},

    # (Chord: [Notes])
    "chord": {  "power":{0.7},
                "major": {0,4,7},
                "minor": {0,3,7},
                "sus2": {0,2,7},
                "sus4": {0,5,7},
                "maj7": {0,4,7,11},
                "min7": {0,3,7,10},
                "dom7": {0,4,7,10},
                "add9": {0,4,7,14},
                "minadd9": {0,3,7,14},
                "add11": {0,4,7,17},
                "minadd11": {0,3,7,17},
                "maj6": {0,4,7,9},
                "min6": {0,3,7,9},
                "maj9": {0,4,7,11,14},
                "min9": {0,3,7,10,14},
                "dom9": {0,4,7,10,14},
                "maj11": {0,4,7,11,14,17},
                "min11": {0,3,7,10,14,17},
                "dom11": {0,4,7,10,14,17}, 
                "maj13": {0,4,7,11,14,17,21},
                "min13": {0,3,7,10,14,17,21},
                "dom13": {0,4,7,10,14,17,21},
                "dim": {0,3,6},
                "aug": {0,4,8},
                "b13": {0,3,6,10},
                "s9": {0,4,7,10,15},
                "b9": {0,4,7,10,13},
                "halfdim": {0,4,7,10,14,17,20},
                "four": {0,5} },

    # (Progression : [Pattern])
    "progression": {"doowop" : [["I", "major"], ["vi", "minor"], ["IV", "major"], ["V", "major"]],
                    "pop" : [["I", "major"], ["V", "major"], ["vi", "minor"], ["IV", "major"]],
                    "saduplift" : [["vi", "minor"], ["V", "major"], ["IV", "major"], ["V", "major"]],
                    "storyteller" : [["I", "major"], ["IV", "major"], ["vi", "minor"], ["V", "major"]],
                    "bassplayer" : [["I", "major"], ["ii", "min7"], ["I", "maj6"], ["IV", "major"]],
                    "jazz" : [["I", "major"], ["vi", "minor"], ["ii", "minor"], ["V", "major"]],
                    "journey" : [["IV", "major"], ["I", "maj6"], ["V", "major"]],
                    "secondarydom" : [["IV", "major"], ["V", "major"], ["V", "maj6"], ["vi", "minor"]],
                    "minorchange" : [["IV", "major"], ["iv", "minor"], ["I", "major"]],
                    "trap" : [["i", "minor"], ["VI", "major"], ["I", "major"], ["v", "minor"]],
                    "major_scale": [["I", "major"], ["ii", "minor"], ["iii", "minor"], ["IV", "major"], ["V", "major"], ["vi", "minor"], ["vii", "dim"]],
                    "minor_scale": [["I", "major"], ["ii", "dim"], ["III", "major"], ["iv", "minor"], ["v", "minor"], ["VI", "major"], ["VII", "major"]]},

    # ([Emotion, any(Chord, Progression)] : [Name] )
    "emotion": { "dark": {"chord" : ["power", "maj7", "minadd9", "halfdim", 
                                    "minor", "sus4", "dom7", "minadd11",                    # Sad, Dark, Down ... etc
                                    "dom9", "min11", "dim", "aug", "b13", "b9"],

                        "progression": ["storyteller", "bassplayer", 
                                            "saduplift", "secondarydom", 
                                            "minorchange", "trap", "minor_scale" ,
                                            "minor_scale", "minor_scale", 
                                            "major_scale", "major_scale"],

                        "scales": ["dorian_scale", "minor_scale", "mixolydian_scale", "locrian_scale", "melodic_scale"]},

                 "light" : { "chord": ["power", "maj7", "minadd9", "halfdim", 
                                    "major", "sus2", "add9", "add11", "dom11", "s9"],       # Happy, Light, Upbeat ... etc
                
                             "progression": ["storyteller", "bassplayer", 
                                            "doowop", "pop", "journey", "major_scale", 
                                            "major_scale", "major_scale"],

                             "scales": ["major_scale", "lydian_scale", "mixolydian_scale"]},

                "jazz": {"chord": ["maj7","min7","four","sus4","maj11", "maj13", "min13", "dom13"],

                                    "progression": ["jazz"],

                                    "scales": ["dorian_scale", "minor_scale", "mixolydian_scale", "locrian_scale"
                                    , "melodic_scale","major_scale", "lydian_scale"]},

                "exotic": {"chord": ["four","sus4", "min7", "maj6", "min6", "maj9", "min9"],

                                    "progression": ["jazz", "major_scale", "major_scale", "minor_scale"],

                                    "scales": ["phrygian_scale", "pentatonic_scale", "harmonic_scale"]}}

}

    
# (Mode: Scales)
mdb_mode = {1: "major_scale",
                2: "dorian_scale",
                3: "phrygian_scale",
                4: "lydian_scale",
                5: "mixolydian_scale",
                6: "minor_scale",
                7: "locrian_scale"}


# [note type and duration]
mdb_notetype=[64, 48, 32, 24, 16, 12, 8, 6, 4, 3, 2] # 16 = Quarter Note


###################################
##                               ##
##       Bachelors Thesis        ##
##                               ##
##  Author: Tereza Straková      ##
##  2023                         ##
###################################


from modules.scg import Rule, Variation

input_pitches    = [ 'c1', 'd1', 'e1', 'f1', 'g1', 'a1', 'h1',
                     'c2', 'd2', 'e2', 'f2', 'g2', 'a2', 'h2',
                     'c3']
# music21_pitches  = [ 'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4',
#                      'C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5',
#                      'C6']

pitches = ['c1', 'cis1', 'd1', 'dis1', 'e1', 'f1', 'fis1', 'g1', 'gis1', 'a1', 'ais1', 'h1',
           'c2', 'cis2', 'd2', 'dis2', 'e2', 'f2', 'fis2', 'g2', 'gis2', 'a2', 'ais2', 'h2',
           'c3']
music21_pitches = ['C4', 'C#4', 'D4', 'D#4', 'E4', 'F4', 'F#4', 'G4', 'G#4', 'A4', 'A#4', 'B4',
                  'C5', 'C#5', 'D5', 'D#5', 'E5', 'F5', 'F#5', 'G5', 'G#5', 'A5', 'A#5', 'B5',
                  'C6']

durations = ['1','2','4','8']
music21_durations = ['whole','half','quarter','eighth']

input_alphabet = pitches + music21_durations + ['rest']

to_tinyTheme_duration = {
    'whole'   : '1',
    'half'    : '2',
    'quarter' : '4',
    'eighth'   : '8'
}

to_music21_duration = {
    '1' : 'whole',
    '2' : 'half',
    '4' : 'quarter',
    '8' : 'eighth'
}

# S will be starting symbol
# X will be expanded to pitch/rest
# Y will be expanded to duration
rules = [
    # starting rule
    Rule(['S'],     [['X', 'X']]), # 0

    # copy pitch
    Rule(['X', 'X'], [['c1', 'Y'], ['c1', 'Y']]),  # 1
    Rule(['X', 'X'], [['d1', 'Y'], ['d1', 'Y']]),  # 2
    Rule(['X', 'X'], [['e1', 'Y'], ['e1', 'Y']]),  # 3
    Rule(['X', 'X'], [['f1', 'Y'], ['f1', 'Y']]),  # 4
    Rule(['X', 'X'], [['g1', 'Y'], ['g1', 'Y']]),  # 5
    Rule(['X', 'X'], [['a1', 'Y'], ['a1', 'Y']]),  # 6
    Rule(['X', 'X'], [['h1', 'Y'], ['h1', 'Y']]),  # 7
    Rule(['X', 'X'], [['c2', 'Y'], ['c2', 'Y']]),  # 8
    Rule(['X', 'X'], [['d2', 'Y'], ['d2', 'Y']]),  # 9
    Rule(['X', 'X'], [['e2', 'Y'], ['e2', 'Y']]),  # 10
    Rule(['X', 'X'], [['f2', 'Y'], ['f2', 'Y']]),  # 11
    Rule(['X', 'X'], [['g2', 'Y'], ['g2', 'Y']]),  # 12
    Rule(['X', 'X'], [['a2', 'Y'], ['a2', 'Y']]),  # 13
    Rule(['X', 'X'], [['h2', 'Y'], ['h2', 'Y']]),  # 14
    Rule(['X', 'X'], [['c3', 'Y'], ['c3', 'Y']]),  # 15

    # one step up
    Rule(['X', 'X'], [['c1', 'Y'], ['d1', 'Y']]),  # 16
    Rule(['X', 'X'], [['d1', 'Y'], ['e1', 'Y']]),  # 17
    Rule(['X', 'X'], [['e1', 'Y'], ['f1', 'Y']]),  # 18
    Rule(['X', 'X'], [['f1', 'Y'], ['g1', 'Y']]),  # 19
    Rule(['X', 'X'], [['g1', 'Y'], ['a1', 'Y']]),  # 20
    Rule(['X', 'X'], [['a1', 'Y'], ['h1', 'Y']]),  # 21
    Rule(['X', 'X'], [['h1', 'Y'], ['c2', 'Y']]),  # 22
    Rule(['X', 'X'], [['c2', 'Y'], ['d2', 'Y']]),  # 23
    Rule(['X', 'X'], [['d2', 'Y'], ['e2', 'Y']]),  # 24
    Rule(['X', 'X'], [['e2', 'Y'], ['f2', 'Y']]),  # 25
    Rule(['X', 'X'], [['f2', 'Y'], ['g2', 'Y']]),  # 26
    Rule(['X', 'X'], [['g2', 'Y'], ['a2', 'Y']]),  # 27
    Rule(['X', 'X'], [['a2', 'Y'], ['h2', 'Y']]),  # 28
    Rule(['X', 'X'], [['h2', 'Y'], ['c3', 'Y']]),  # 29
    
    # one step down
    Rule(['X', 'X'], [['d1', 'Y'], ['c1', 'Y']]),  # 30
    Rule(['X', 'X'], [['e1', 'Y'], ['d1', 'Y']]),  # 31
    Rule(['X', 'X'], [['f1', 'Y'], ['e1', 'Y']]),  # 32
    Rule(['X', 'X'], [['g1', 'Y'], ['f1', 'Y']]),  # 33
    Rule(['X', 'X'], [['a1', 'Y'], ['g1', 'Y']]),  # 34
    Rule(['X', 'X'], [['h1', 'Y'], ['a1', 'Y']]),  # 35
    Rule(['X', 'X'], [['c2', 'Y'], ['h1', 'Y']]),  # 36
    Rule(['X', 'X'], [['d2', 'Y'], ['c2', 'Y']]),  # 37
    Rule(['X', 'X'], [['e2', 'Y'], ['d2', 'Y']]),  # 38
    Rule(['X', 'X'], [['f2', 'Y'], ['e2', 'Y']]),  # 39
    Rule(['X', 'X'], [['g2', 'Y'], ['f2', 'Y']]),  # 40
    Rule(['X', 'X'], [['a2', 'Y'], ['g2', 'Y']]),  # 41
    Rule(['X', 'X'], [['h2', 'Y'], ['a2', 'Y']]),  # 42
    Rule(['X', 'X'], [['c3', 'Y'], ['h2', 'Y']]),  # 43

    # step up and transpose
    Rule(['X', 'X'], [['c3', 'Y'], ['d2', 'Y']]),  # 44
    # step down and transpose
    Rule(['X', 'X'], [['c1', 'Y'], ['h1', 'Y']]),  # 45

    ### whole step UP ###
    Rule(['X', 'X'], [['e1', 'Y'], ['fis1', 'Y']]), # 46
    Rule(['X', 'X'], [['h1', 'Y'], ['cis2', 'Y']]), # 47
    Rule(['X', 'X'], [['e2', 'Y'], ['fis2', 'Y']]), # 48
    Rule(['X', 'X'], [['h2', 'Y'], ['cis2', 'Y']]), # 49 # move up and transpose

    Rule(['X', 'X'], [['cis1', 'Y'], ['dis1', 'Y']]),  # 50
    Rule(['X', 'X'], [['dis1', 'Y'], ['f1', 'Y']]),    # 51
    Rule(['X', 'X'], [['fis1', 'Y'], ['gis1', 'Y']]),  # 52
    Rule(['X', 'X'], [['gis1', 'Y'], ['ais1', 'Y']]),  # 53
    Rule(['X', 'X'], [['ais1', 'Y'], ['c2', 'Y']]),    # 54
    Rule(['X', 'X'], [['cis2', 'Y'], ['dis2', 'Y']]),  # 55
    Rule(['X', 'X'], [['dis2', 'Y'], ['f2', 'Y']]),    # 56
    Rule(['X', 'X'], [['fis2', 'Y'], ['gis2', 'Y']]),  # 57
    Rule(['X', 'X'], [['gis2', 'Y'], ['ais2', 'Y']]),  # 58
    Rule(['X', 'X'], [['ais2', 'Y'], ['c3', 'Y']]),    # 59

    ### whole step DOWN ###
    Rule(['X', 'X'], [['c1', 'Y'], ['ais1', 'Y']]),  # 60 # move down and transpose
    Rule(['X', 'X'], [['cis1', 'Y'], ['h1', 'Y']]),  # 61 # move down and transpose

    Rule(['X', 'X'], [['dis1', 'Y'], ['cis1', 'Y']]),  # 62
    Rule(['X', 'X'], [['f1', 'Y'], ['dis1', 'Y']]),    # 63
    Rule(['X', 'X'], [['fis1', 'Y'], ['e1', 'Y']]),    # 64
    Rule(['X', 'X'], [['gis1', 'Y'], ['fis1', 'Y']]),  # 65
    Rule(['X', 'X'], [['ais1', 'Y'], ['gis1', 'Y']]),  # 66
    Rule(['X', 'X'], [['c2', 'Y'], ['ais1', 'Y']]),    # 67
    
    Rule(['X', 'X'], [['cis2', 'Y'], ['h1', 'Y']]),    # 68
    Rule(['X', 'X'], [['dis2', 'Y'], ['cis2', 'Y']]),  # 69
    Rule(['X', 'X'], [['f2', 'Y'], ['dis2', 'Y']]),    # 70
    Rule(['X', 'X'], [['fis2', 'Y'], ['e2', 'Y']]),    # 71
    Rule(['X', 'X'], [['gis2', 'Y'], ['fis2', 'Y']]),  # 72
    Rule(['X', 'X'], [['ais2', 'Y'], ['gis2', 'Y']]),  # 73
    Rule(['X', 'X'], [['c3', 'Y'], ['ais2', 'Y']]),    # 74

    # copy duration
    Rule(['Y', 'Y'], [['whole', 'X'],   ['whole', 'X']]),   # 75
    Rule(['Y', 'Y'], [['half', 'X'],    ['half', 'X']]),    # 76
    Rule(['Y', 'Y'], [['quarter', 'X'], ['quarter', 'X']]), # 77
    Rule(['Y', 'Y'], [['eighth', 'X'],  ['eighth', 'X']]),  # 78

    # halve duration - diminution
    Rule(['Y', 'Y'], [['whole', 'X'], ['half', 'X']]),     # 79
    Rule(['Y', 'Y'], [['half', 'X'], ['quarter', 'X']]),   # 80
    Rule(['Y', 'Y'], [['quarter', 'X'], ['eighth', 'X']]), # 81

    # double duration - augmentation
    Rule(['Y', 'Y'], [['half', 'X'], ['whole', 'X']]),     # 82
    Rule(['Y', 'Y'], [['quarter', 'X'], ['half', 'X']]),   # 83
    Rule(['Y', 'Y'], [['eighth', 'X'], ['quarter', 'X']]), # 84

    # retrogradation rules
    Rule(['Y', 'Y'], [['whole', 'X', 'X'], ['whole']]),     # 85
    Rule(['Y', 'Y'], [['half', 'X', 'X'], ['half']]),       # 86
    Rule(['Y', 'Y'], [['quarter', 'X', 'X'], ['quarter']]), # 87
    Rule(['Y', 'Y'], [['eighth', 'X', 'X'], ['eighth']]),   # 88

    # copy rest
    Rule(['X', 'X'], [['rest', 'Y'], ['rest', 'Y']]), # 89

    Rule(['X', 'X'], [['eps'], ['eps']]), # ? 90

]

# for i,r, in enumerate(rules):
#     print(i,r)


# ll tables
var_repeat = Variation(
                     {
        ('S', 'c1'): 0,
        ('S', 'd1'): 0,
        ('S', 'e1'): 0,
        ('S', 'f1'): 0,
        ('S', 'g1'): 0,
        ('S', 'a1'): 0,
        ('S', 'h1'): 0,
        ('S', 'c2'): 0,
        ('S', 'd2'): 0,
        ('S', 'e2'): 0,
        ('S', 'f2'): 0,
        ('S', 'g2'): 0,
        ('S', 'a2'): 0,
        ('S', 'h2'): 0,
        ('S', 'c3'): 0,
        ('S', 'rest'): 0,

        ('X', 'c1'): 1,
        ('X', 'd1'): 2,
        ('X', 'e1'): 3,
        ('X', 'f1'): 4,
        ('X', 'g1'): 5,
        ('X', 'a1'): 6,
        ('X', 'h1'): 7,
        ('X', 'c2'): 8,
        ('X', 'd2'): 9,
        ('X', 'e2'): 10,
        ('X', 'f2'): 11,
        ('X', 'g2'): 12,
        ('X', 'a2'): 13,
        ('X', 'h2'): 14,
        ('X', 'c3'): 15,

        ('Y', 'whole'): 75,
        ('Y', 'half'): 76,
        ('Y', 'quarter'): 77,
        ('Y', 'eighth'): 78,
        
        ('X', 'rest'): 89,
        
        ('X', '$'): 90
    })
var_sequence_up = Variation(
                     {
        ('S', 'c1'): 0,
        ('S', 'd1'): 0,
        ('S', 'e1'): 0,
        ('S', 'f1'): 0,
        ('S', 'g1'): 0,
        ('S', 'a1'): 0,
        ('S', 'h1'): 0,
        ('S', 'c2'): 0,
        ('S', 'd2'): 0,
        ('S', 'e2'): 0,
        ('S', 'f2'): 0,
        ('S', 'g2'): 0,
        ('S', 'a2'): 0,
        ('S', 'h2'): 0,
        ('S', 'c3'): 0,
        ('S', 'rest'): 0,

        ('X', 'c1'): 16,
        ('X', 'd1'): 17,
        ('X', 'e1'): 18,
        ('X', 'f1'): 19,
        ('X', 'g1'): 20,
        ('X', 'a1'): 21,
        ('X', 'h1'): 22,
        ('X', 'c2'): 23,
        ('X', 'd2'): 24,
        ('X', 'e2'): 25,
        ('X', 'f2'): 26,
        ('X', 'g2'): 27,
        ('X', 'a2'): 28,
        ('X', 'h2'): 29,
        ('X', 'c3'): 44, # step up and transpose down

        ('Y', 'whole'): 75,
        ('Y', 'half'): 76,
        ('Y', 'quarter'): 77,
        ('Y', 'eighth'): 78,
        
        ('X', 'rest'): 89,
        
        ('X', '$'): 90
    })
var_sequence_down = Variation(
                     {
        ('S', 'c1'): 0,
        ('S', 'd1'): 0,
        ('S', 'e1'): 0,
        ('S', 'f1'): 0,
        ('S', 'g1'): 0,
        ('S', 'a1'): 0,
        ('S', 'h1'): 0,
        ('S', 'c2'): 0,
        ('S', 'd2'): 0,
        ('S', 'e2'): 0,
        ('S', 'f2'): 0,
        ('S', 'g2'): 0,
        ('S', 'a2'): 0,
        ('S', 'h2'): 0,
        ('S', 'c3'): 0,
        ('S', 'rest'): 0,

        ('X', 'c1'): 45, # step down and transpose up
        ('X', 'd1'): 30,
        ('X', 'e1'): 31,
        ('X', 'f1'): 32,
        ('X', 'g1'): 33,
        ('X', 'a1'): 34,
        ('X', 'h1'): 35,
        ('X', 'c2'): 36,
        ('X', 'd2'): 37,
        ('X', 'e2'): 38,
        ('X', 'f2'): 39,
        ('X', 'g2'): 40,
        ('X', 'a2'): 41,
        ('X', 'h2'): 42,
        ('X', 'c3'): 43,

        ('Y', 'whole'): 75,
        ('Y', 'half'): 76,
        ('Y', 'quarter'): 77,
        ('Y', 'eighth'): 78,
        
        ('X', 'rest'): 89,
        
        ('X', '$'): 90
    })
var_augmentation = Variation(
                     {
        ('S', 'c1'): 0,
        ('S', 'd1'): 0,
        ('S', 'e1'): 0,
        ('S', 'f1'): 0,
        ('S', 'g1'): 0,
        ('S', 'a1'): 0,
        ('S', 'h1'): 0,
        ('S', 'c2'): 0,
        ('S', 'd2'): 0,
        ('S', 'e2'): 0,
        ('S', 'f2'): 0,
        ('S', 'g2'): 0,
        ('S', 'a2'): 0,
        ('S', 'h2'): 0,
        ('S', 'c3'): 0,
        ('S', 'rest'): 0,

        ('X', 'c1'): 1,
        ('X', 'd1'): 2,
        ('X', 'e1'): 3,
        ('X', 'f1'): 4,
        ('X', 'g1'): 5,
        ('X', 'a1'): 6,
        ('X', 'h1'): 7,
        ('X', 'c2'): 8,
        ('X', 'd2'): 9,
        ('X', 'e2'): 10,
        ('X', 'f2'): 11,
        ('X', 'g2'): 12,
        ('X', 'a2'): 13,
        ('X', 'h2'): 14,
        ('X', 'c3'): 15,


        ('Y', 'whole'): 75,
        ('Y', 'half'): 82,
        ('Y', 'quarter'): 83,
        ('Y', 'eighth'): 84,
        
        ('X', 'rest'): 89,
        
        ('X', '$'): 90 
    })
var_diminution = Variation(
                     {
        ('S', 'c1'): 0,
        ('S', 'd1'): 0,
        ('S', 'e1'): 0,
        ('S', 'f1'): 0,
        ('S', 'g1'): 0,
        ('S', 'a1'): 0,
        ('S', 'h1'): 0,
        ('S', 'c2'): 0,
        ('S', 'd2'): 0,
        ('S', 'e2'): 0,
        ('S', 'f2'): 0,
        ('S', 'g2'): 0,
        ('S', 'a2'): 0,
        ('S', 'h2'): 0,
        ('S', 'c3'): 0,
        ('S', 'rest'): 0,

        ('X', 'c1'): 1,
        ('X', 'd1'): 2,
        ('X', 'e1'): 3,
        ('X', 'f1'): 4,
        ('X', 'g1'): 5,
        ('X', 'a1'): 6,
        ('X', 'h1'): 7,
        ('X', 'c2'): 8,
        ('X', 'd2'): 9,
        ('X', 'e2'): 10,
        ('X', 'f2'): 11,
        ('X', 'g2'): 12,
        ('X', 'a2'): 13,
        ('X', 'h2'): 14,
        ('X', 'c3'): 15,

        ('Y', 'whole'): 79,
        ('Y', 'half'): 80,
        ('Y', 'quarter'): 81,
        ('Y', 'eighth'): 78,
        
        ('X', 'rest'): 89,
        
        ('X', '$'): 90
    })

var_retrograde = Variation(
                        {
        ('S', 'c1'): 0,
        ('S', 'd1'): 0,
        ('S', 'e1'): 0,
        ('S', 'f1'): 0,
        ('S', 'g1'): 0,
        ('S', 'a1'): 0,
        ('S', 'h1'): 0,
        ('S', 'c2'): 0,
        ('S', 'd2'): 0,
        ('S', 'e2'): 0,
        ('S', 'f2'): 0,
        ('S', 'g2'): 0,
        ('S', 'a2'): 0,
        ('S', 'h2'): 0,
        ('S', 'c3'): 0,
        ('S', 'rest'): 0,

        ('X', 'c1'): 1,
        ('X', 'd1'): 2,
        ('X', 'e1'): 3,
        ('X', 'f1'): 4,
        ('X', 'g1'): 5,
        ('X', 'a1'): 6,
        ('X', 'h1'): 7,
        ('X', 'c2'): 8,
        ('X', 'd2'): 9,
        ('X', 'e2'): 10,
        ('X', 'f2'): 11,
        ('X', 'g2'): 12,
        ('X', 'a2'): 13,
        ('X', 'h2'): 14,
        ('X', 'c3'): 15,

        ('Y', 'whole'): 85,
        ('Y', 'half'): 86,
        ('Y', 'quarter'): 87,
        ('Y', 'eighth'): 88,
        
        ('X', 'rest'): 89,
        
        ('X', '$'): 90
    })

var_whole_step_up = Variation(
    {
        ('S', 'c1'): 0,
        ('S', 'd1'): 0,
        ('S', 'e1'): 0,
        ('S', 'f1'): 0,
        ('S', 'g1'): 0,
        ('S', 'a1'): 0,
        ('S', 'h1'): 0,
        ('S', 'c2'): 0,
        ('S', 'd2'): 0,
        ('S', 'e2'): 0,
        ('S', 'f2'): 0,
        ('S', 'g2'): 0,
        ('S', 'a2'): 0,
        ('S', 'h2'): 0,
        ('S', 'c3'): 0,
        ('S', 'rest'): 0,

        ('S', 'cis1'): 0,
        ('S', 'dis1'): 0,
        ('S', 'fis1'): 0,
        ('S', 'gis1'): 0,
        ('S', 'ais1'): 0,
        ('S', 'cis2'): 0,
        ('S', 'dis2'): 0,
        ('S', 'fis2'): 0,
        ('S', 'gis2'): 0,
        ('S', 'ais2'): 0,

        ('X', 'c1'): 16,
        ('X', 'd1'): 17,
        ('X', 'e1'): 46, #
        ('X', 'f1'): 19,
        ('X', 'g1'): 20,
        ('X', 'a1'): 21,
        ('X', 'h1'): 47, #
        ('X', 'c2'): 23,
        ('X', 'd2'): 24,
        ('X', 'e2'): 48, #
        ('X', 'f2'): 26,
        ('X', 'g2'): 27,
        ('X', 'a2'): 28,
        ('X', 'h2'): 49, # step up and transpose down
        ('X', 'c3'): 44, # step up and transpose down

        ('X', 'cis1'): 50,
        ('X', 'dis1'): 51,
        ('X', 'fis1'): 52,
        ('X', 'gis1'): 53,
        ('X', 'ais1'): 54,
        ('X', 'cis2'): 55,
        ('X', 'dis2'): 56,
        ('X', 'fis2'): 57,
        ('X', 'gis2'): 58,
        ('X', 'ais2'): 59,

        ('Y', 'whole'): 75,
        ('Y', 'half'): 76,
        ('Y', 'quarter'): 77,
        ('Y', 'eighth'): 78,
        
        ('X', 'rest'): 89,
        
        ('X', '$'): 90
    }
)

var_whole_step_down = Variation(
    {
        ('S', 'c1'): 0,
        ('S', 'd1'): 0,
        ('S', 'e1'): 0,
        ('S', 'f1'): 0,
        ('S', 'g1'): 0,
        ('S', 'a1'): 0,
        ('S', 'h1'): 0,
        ('S', 'c2'): 0,
        ('S', 'd2'): 0,
        ('S', 'e2'): 0,
        ('S', 'f2'): 0,
        ('S', 'g2'): 0,
        ('S', 'a2'): 0,
        ('S', 'h2'): 0,
        ('S', 'c3'): 0,
        ('S', 'rest'): 0,

        ('S', 'cis1'): 0,
        ('S', 'dis1'): 0,
        ('S', 'fis1'): 0,
        ('S', 'gis1'): 0,
        ('S', 'ais1'): 0,
        ('S', 'cis2'): 0,
        ('S', 'dis2'): 0,
        ('S', 'fis2'): 0,
        ('S', 'gis2'): 0,
        ('S', 'ais2'): 0,

        ('X', 'c1'): 60, # move down and transpose up
        ('X', 'd1'): 30,
        ('X', 'e1'): 31, 
        ('X', 'f1'): 63, #
        ('X', 'g1'): 33,
        ('X', 'a1'): 34,
        ('X', 'h1'): 35, 
        ('X', 'c2'): 67, #
        ('X', 'd2'): 37,
        ('X', 'e2'): 38, 
        ('X', 'f2'): 70, #
        ('X', 'g2'): 40,
        ('X', 'a2'): 41,
        ('X', 'h2'): 42, 
        ('X', 'c3'): 74, #

        ('X', 'cis1'): 61,
        ('X', 'dis1'): 62,
        ('X', 'fis1'): 64,
        ('X', 'gis1'): 65,
        ('X', 'ais1'): 66,
        ('X', 'cis2'): 68,
        ('X', 'dis2'): 69,
        ('X', 'fis2'): 71,
        ('X', 'gis2'): 72,
        ('X', 'ais2'): 73,

        ('Y', 'whole'): 75,
        ('Y', 'half'): 76,
        ('Y', 'quarter'): 77,
        ('Y', 'eighth'): 78,
        
        ('X', 'rest'): 89,
        
        ('X', '$'): 90
    }
)



ll_tables = {
    'repeat' : var_repeat,
    'sequence_up' : var_sequence_up,
    'sequence_down' : var_sequence_down,
    'augmentation' : var_augmentation,
    'diminution' : var_diminution,
    'retrograde' : var_retrograde,
    'whole_step_up' : var_whole_step_up,
    'whole_step_down' : var_whole_step_down
}


class TokenConverter:
    def __init__(self) -> None:

        self.pitches = ['c1', 'cis1', 'd1', 'dis1', 'e1', 'f1', 'fis1', 'g1', 'gis1', 'a1', 'ais1', 'h1',
            'c2', 'cis2', 'd2', 'dis2', 'e2', 'f2', 'fis2', 'g2', 'gis2', 'a2', 'ais2', 'h2',
            'c3']

        self.music21_pitches = ['C4', 'C#4', 'D4', 'D#4', 'E4', 'F4', 'F#4', 'G4', 'G#4', 'A4', 'A#4', 'B4',
                        'C5', 'C#5', 'D5', 'D#5', 'E5', 'F5', 'F#5', 'G5', 'G#5', 'A5', 'A#5', 'B5',
                        'C6']

        # https://pythonguides.com/python-creates-a-dictionary-from-two-lists/
        self.to_tinyTheme_pitch = dict(zip(music21_pitches, pitches))

        self.to_music21_pitch = dict(zip(pitches, music21_pitches))
    
    def convert_note_type_token(self,token,from_music21 = True):
        if from_music21:
            try:
                ret_token = self.to_tinyTheme_pitch[token]
            except Exception as e:
                raise e
        else:
            if token == 'rest':
                return token
            try:
                ret_token = self.to_music21_pitch[token]
            except Exception as e:
                raise e
        return ret_token
    
    def split_tiny_token(self,token):
        try:
            pitch, duration = token.split('_',1)
        except Exception:
            raise ValueError('Invalid input file, unknown token: '+token)
        
        if pitch == 'r':
            pitch = 'rest'
        elif pitch not in input_pitches or duration not in durations:
            raise ValueError('Invalid input file, unknown token: '+token)
        duration = to_music21_duration[duration]
        return pitch, duration

    def to_tiny_token(self,pitch,duration):
        duration = to_tinyTheme_duration[duration]
        token = pitch+'_'+duration
        return token
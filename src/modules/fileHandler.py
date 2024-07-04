###################################
##                               ##
##       Bachelors Thesis        ##
##                               ##
##  Author: Tereza Straková      ##
##  2023                         ##
###################################

import music21
from music21.lily.translate import LilypondConverter

W = '\033[0m'  # white (normal)
B = '\033[34m'  # blue
import os

from modules.scg import InputString
from modules.musicGrammar import TokenConverter

class MusicParser:
    def __init__(self) -> None:
        self.music_tokens = [] # music_tokens extracted from input file
        
        self.time_signature = None # time signature from input file
        self.output_m21_part = music21.stream.Part() # generated variations go here
        self.lilypond_converter = None
        self.first_measure = None
        self.first_measure_is_set = False # to check if first measure is set
        self.measure_duration = 0 #
        self.output_filepath = None
        self.input_filepath = None
        self.tokenConverter = TokenConverter()

    # main method to parse input file, saves path to input file
    def from_file(self,music_filepath):
        self.set_input_filepath(music_filepath)
        if not self.from_tiny_theme_file(music_filepath):
            self.from_music_xml_file(music_filepath)

    def from_tiny_theme_file(self, tiny_filepath):
        try:
            with open(tiny_filepath, "r") as file:
                tiny_header = 'tinyTheme:'
                # try reading the header
                file_header = file.read(len(tiny_header))
                # compare headers
                if file_header.lower() != tiny_header.lower():
                    return False
                # read time signature and set
                time_signature = file.readline().strip()
                m21_ts = music21.meter.TimeSignature(time_signature)
                
                self.set_time_signature(time_signature=m21_ts)
                
                # parse the rest of file
                for line in file:
                    line = line.strip()
                    for token in line.split():
                        pitch,duration = self.tokenConverter.split_tiny_token(token)
                        self.music_tokens.append(pitch)
                        self.music_tokens.append(duration)
                    
        except FileNotFoundError:
            print("File not found. Please check the file path.")
            raise
        except IOError:
            print("Error reading the file. Please check file permissions or other issues.")
            raise

        return True


    
    # called by from_file, fills the `self.music_tokens`
    def from_music_xml_file(self, music_xml_file):

        music21_part = self.music_xml_to_music21(music_xml_file)

        self.set_time_signature(music21_part[music21.meter.TimeSignature].first()) 

        notes = music21_part.flatten().notesAndRests.stream()
        
        for note in notes:
            self.append_music_tokens(note)


    # converts musicXML file to music21 object, find music21 Part() and return it
    def music_xml_to_music21(self, file):
        try:
            score = music21.converter.parse(file)
        
        except Exception as e:
            raise Exception("while parsing {} file: {}".format(file,e))
        
        if isinstance(score, music21.stream.Score):
            return score.parts[0]
        
        elif isinstance(score, music21.stream.Part):
            return score
        
        else:
            raise Exception("not supported musicXML score type")


    def append_music_tokens(self, note):
        if isinstance(note,music21.note.Note):
            note_name = self.tokenConverter.convert_note_type_token(note.nameWithOctave,
                                                          from_music21=True)
            self.music_tokens.append(str(note_name))
        
        elif isinstance(note,music21.note.Rest):
            self.music_tokens.append(str(note.name))
        
        else:
            raise ValueError("expected Note or Rest")
        
        self.music_tokens.append(str(note.duration.type))



    def generate_music21_part(self,list_of_variations):
        music21_part = music21.stream.Part()

        for variation in list_of_variations:
            self.music21_from_variation_tokens(variation, music21_part)

        # set barline of final measure
        music21_part.finalBarline = 'final'
        self.output_m21_part = music21_part


    def create_music21_note(self,note,duration):
        if note == 'rest':
            music21_note = music21.note.Rest()
        else:
            music21_note = music21.note.Note()
            music21_note.pitch = music21.pitch.Pitch(note)
        if duration is None:
            raise Exception('internal error, trying to create a note with None duration.')
        music21_note.duration.type = duration
        return music21_note

    def create_music21_note_quarterLen(self,note,quarterLength):
        if note == 'rest':
            music21_note = music21.note.Rest()
        else:
            music21_note = music21.note.Note()
            music21_note.pitch = music21.pitch.Pitch(note)
        music21_note.duration.quarterLength = quarterLength
        return music21_note

    def music21_from_variation_tokens(self,variation_string,music21_part):
        variation_tokens = InputString(variation_string)
        
        
        leftover = None
        # do while there are variation tokens to parse
        while (not variation_tokens.is_parsed()) or leftover is not None:
            # create empty measure object
            measure = music21.stream.Measure()
            # if it's the first measure, must set time signature
            if not self.first_measure_is_set:
                measure.timeSignature = self.time_signature
                # set measure duration
                self.measure_duration = measure.barDuration.quarterLength
            # how much of the measure is already filled
            filled_duration = 0
            # leftover from previous measure
            if leftover is not None:
                measure.append(leftover)
                filled_duration+=measure.duration.quarterLength
                leftover = None
            # while theres still space in the measure to be filled
            while(filled_duration < self.measure_duration):
                # first check if there are tokens left to be parsed
                if variation_tokens.is_parsed():
                    # if not, fill the rest of measure with a rest
                    # of appropriate length
                    quarterLength = self.measure_duration - filled_duration
                    music21_note = self.create_music21_note_quarterLen('rest',quarterLength)
                    measure.append(music21_note)
                    filled_duration+=music21_note.duration.quarterLength
                    continue

                note_type = variation_tokens.get_current_token()
                
                note_type = self.tokenConverter.convert_note_type_token(note_type,from_music21=False)
                
                note_duration = variation_tokens.read_token()

                music21_note = self.create_music21_note(note=note_type,duration=note_duration)
                

                # check if note/rest fits into measure
                if filled_duration+music21_note.duration.quarterLength <= self.measure_duration:
                    measure.append(music21_note)
                    filled_duration+=music21_note.duration.quarterLength
                    # variation_tokens.read_token()
                else:
                    # how much is needed to fill the rest of this measure
                    quarterLength = self.measure_duration - filled_duration
                    # how much is the leftover, current note minus what will go into this measure
                    leftoverLen = music21_note.duration.quarterLength - quarterLength
                    # create note with that length
                    note1 = self.create_music21_note_quarterLen(music21_note.nameWithOctave,quarterLength)
                    note1.tie = music21.tie.Tie('start') # add start of tie to the note
                    measure.append(note1) # append the note
                    # update how much is filled
                    filled_duration+=quarterLength 
                    # change quarter length on current note
                    music21_note.duration.quarterLength = leftoverLen
                    music21_note.tie = music21.tie.Tie('stop') # add the end of tie to it
                    leftover = music21_note # set it as leftover
                # read next token
                variation_tokens.read_token()
            music21_part.append(measure)
            if not self.first_measure_is_set:
                self.first_measure_is_set = True


    def to_file(self, list_of_variations, file_types):
        tinytheme_out = self.generate_tinytheme_output(list_of_variations=list_of_variations)
        self.generate_music21_part(list_of_variations)

        if file_types is None:
            print(tinytheme_out)
            return

        # will set output file according to input file location
        self.set_output_file_path(self.input_filepath)
        filepath = self.output_filepath
        if filepath is None:
            filepath = 'variations'
        
        if not file_types:
            file_types = ['txt']

        if 'txt' in file_types:
            self.to_tinytheme_txt_file(filepath+'.txt',tinytheme_out)
        
        if 'musicxml' in file_types:
            self.to_musicxml_file(filepath+'.musicxml')
        
        if 'svg' in file_types:
            self.to_svg(filepath)
        
        if 'pdf' in file_types:
            self.to_pdf(filepath)
        
        if 'png' in file_types:
            self.to_png(filepath)
        


    def generate_tinytheme_output(self,list_of_variations):

        tiny_output = 'tinyTheme: ' + self.time_signature.ratioString + '\n'

        for variation in list_of_variations:
            tiny_output += '\n' + self.generate_tinytheme_variation(variation) +'\n'

        return tiny_output

    def generate_tinytheme_variation(self,variation):
        tokens = InputString(variation)
        variation_string = ''
        while not tokens.is_parsed():
            pitch = tokens.get_current_token()
            duration = tokens.read_token()
            token = self.tokenConverter.to_tiny_token(pitch,duration)

            variation_string += token + ' '
            tokens.read_token()
        return variation_string
    
    def to_tinytheme_txt_file(self,file_name,tinytheme_content):
        
        with open(file_name, 'w') as file:
            
            file.write(tinytheme_content)


    def generate_lilypond(self):
        if self.lilypond_converter is None:
            lpConverter = LilypondConverter()
            lpConverter.context.contents.append(lpConverter.versionString)

            # lpConverter.context.contents.append("#(ly:set-option 'crop #t)")
            
            lpConverter.appendM21ObjectToContext(self.output_m21_part)
            self.lilypond_converter = lpConverter

    def to_svg(self, file_name):
        self.generate_lilypond()
        print('writing to',B,file_name,W)
        self.lilypond_converter.runThroughLily(format='svg', backend='svg', fileName=file_name)
    
    def to_png(self, file_name):
        self.generate_lilypond()
        self.lilypond_converter.runThroughLily(format='png', fileName=file_name)
    
    def to_pdf(self, file_name):
        self.generate_lilypond()
        self.lilypond_converter.runThroughLily(format='pdf', fileName=file_name)
    
    def to_musicxml_file(self, file_name):
        GEX = music21.musicxml.m21ToXml.GeneralObjectExporter(self.output_m21_part)
        out = GEX.parse()
        outStr = out.decode('utf-8')
        
        text_file = open(file_name, "w")
        print(B+'writing to :'+W, file_name)
        text_file.write(outStr.strip())
        text_file.close()

    def play_music(self,play_music):
        if play_music:
            stream_player = music21.midi.realtime.StreamPlayer(self.output_m21_part)
            stream_player.play()

    def set_output_file_path(self,file_path):
        directory_path = os.path.dirname(file_path)

        file_name_with_extension = os.path.basename(file_path)

        file_name, file_extension = os.path.splitext(file_name_with_extension)

        new_file_name = file_name + '_variations'

        new_file_path = os.path.join(directory_path, new_file_name)

        self.output_filepath = new_file_path

    def set_time_signature(self, time_signature):
        self.time_signature = time_signature

    def set_input_filepath(self,filepath):
        self.input_filepath = filepath
    
    def get_time_signature(self):
        return self.time_signature
    
    def get_music_tokens(self):
        return self.music_tokens
    

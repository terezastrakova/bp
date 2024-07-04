###################################
##                               ##
##       Bachelors Thesis        ##
##                               ##
##  Author: Tereza Straková      ##
##  2023                         ##
###################################

import modules.scg as scg
import modules.fileHandler as fileHandler
import argparse
import modules.musicGrammar as G

class ArgParser:
    def __init__(self) -> None:
        self.argument_parser = argparse.ArgumentParser()
        self.argument_parser.add_argument('input_file',
                                    help="path to input file")
        self.argument_parser.add_argument('-r','--repeat',
                                    action='store_true',
                                    help="repeat melody")
        self.argument_parser.add_argument('-u','--sequence_up',
                                    action='store_true',
                                    help="move melody up one step on the diatonic scale")
        self.argument_parser.add_argument('-d','--sequence_down',
                                    action='store_true',
                                    help="move melody one step down on the diatonic scale")
        self.argument_parser.add_argument('-A','--augmentation',
                                    action='store_true',
                                    help="double length of every note")
        self.argument_parser.add_argument('-D','--diminution',
                                    action='store_true',
                                    help="halve length of every note")
        self.argument_parser.add_argument('-R','--retrograde',
                                    action='store_true',
                                    help="reverse melody")
        self.argument_parser.add_argument('-W','--whole_step_up',
                                    action='store_true',
                                    help="move melody one whole step up")
        self.argument_parser.add_argument('-w','--whole_step_down',
                                    action='store_true',
                                    help="move melody one whole step down")
        self.argument_parser.add_argument('--show',
                                          action='store_true',
                                          help='show used rules')
        self.argument_parser.add_argument('--play',
                                          action='store_true',
                                          help='play created music')
        self.argument_parser.add_argument('--save',
                                          nargs='*',
                                          choices=['musicxml', 'pdf', 'svg', 'png'],
                                          help='saves output as file in specified format')


        self.program_args = None
        self.variation_types_keys = []

    def parse_args(self):
        self.program_args = self.argument_parser.parse_args()
        
        self.set_keys_from_program_args()

    def set_keys_from_program_args(self):
        if self.program_args.repeat:
            self.append_variation_type('repeat')
        
        if self.program_args.sequence_up:
            self.append_variation_type('sequence_up')

        if self.program_args.sequence_down:
            self.append_variation_type('sequence_down')

        if self.program_args.augmentation:
            self.append_variation_type('augmentation')

        if self.program_args.diminution:
            self.append_variation_type('diminution')

        if self.program_args.whole_step_up:
            self.append_variation_type('whole_step_up')
        
        if self.program_args.whole_step_down:
            self.append_variation_type('whole_step_down')

        if self.program_args.retrograde:
            self.append_variation_type('retrograde')

    def append_variation_type(self, variation_type):
        self.variation_types_keys.append(variation_type)

    def get_variation_types_keys(self):
        return self.variation_types_keys
    
    def get_input_file(self):
        return self.program_args.input_file
    
    def get_show(self):
        return self.program_args.show

    def get_play(self):
        return self.program_args.play
    
    def get_file_types(self):
        return self.program_args.save


def main():
    # init modules
    xml_parser = fileHandler.MusicParser()
    scg_parser = scg.Parser(input_alphabet=G.input_alphabet, rules=G.rules, ll_tables=G.ll_tables)
    arg_parser = ArgParser()

    arg_parser.parse_args()

    xml_parser.from_file(arg_parser.get_input_file())

    scg_parser.set_input_string(xml_parser.get_music_tokens())
    scg_parser.set_show(arg_parser.get_show())
    scg_parser.set_variation_types(arg_parser.get_variation_types_keys())

    scg_parser.generate_variations()

    xml_parser.to_file(scg_parser.get_variations_results(), file_types=arg_parser.get_file_types())

    xml_parser.play_music(play_music=arg_parser.get_play())



if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error occured:", e)
        exit(1)

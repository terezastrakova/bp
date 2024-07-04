###################################
##                               ##
##       Bachelors Thesis        ##
##                               ##
##  Author: Tereza Straková      ##
##  2023                         ##
###################################

import os

W = ''
R = ''
G = ''
O = ''
B = ''
P = ''
GG = ''
RR = ''

def set_ansi_colors():
    try:
        os.system('...')        
        # set ansi terminal colors
        W = '\033[0m'  # white (normal)
        R = '\033[31m'  # red
        G = '\033[32m'  # green
        O = '\033[33m'  # orange
        B = '\033[34m'  # blue
        P = '\033[35m'  # purple
        GG = '\033[92m'  # bright green
        RR = '\033[91m'  # bright red
    except:
        # couldnt set
        print('not able to set ansi colors')

try:
    os.system('')        
    # set ansi terminal colors
    W = '\033[0m'  # white (normal)
    R = '\033[31m'  # red
    G = '\033[32m'  # green
    O = '\033[33m'  # orange
    B = '\033[34m'  # blue
    P = '\033[35m'  # purple
    GG = '\033[92m'  # bright green
    RR = '\033[91m'  # bright red
except:
    # couldnt set
    print('not able to set ansi colors')
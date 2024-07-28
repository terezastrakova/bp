# bp
Practical part of my bachelor's thesis.

## Overview
The application allows users to process music files, apply various transformations, and export the results in different formats. It is designed to facilitate the analysis and transformation of musical themes, catering to both educational and creative uses.

## Project Structure
- **src**: Contains source code of the application.
  - **data**: Contains example input files.
  - **modules**:
 
## Technologies
- Python 3.10
- music21 library
- Optional: LilyPond for music notation rendering

## Getting Started

### Prerequisites
- Python 3.10 or higher
- pip package installer

### Setup
1. **Clone the repository**
   ```sh
   git clone https://github.com/terezastrakova/bp.git
   cd bp/src
2. **Install dependencies**
   Ensure you have Python and pip installed. Then, run the following command to install necessary packages:
   ```sh
   pip install -r requirements.txt
3. **Run the application**
   To see the help message and understand how to use the application, you can start with:
   ```sh
   python music_generator.py -h
4. **Using the application**
   To process a music file and apply transformations, run:
   ```sh
   python music_generator.py [input_file] [options]
   ```
   Replace `[input_file]` with your file and `[options]` with desired transformation options.


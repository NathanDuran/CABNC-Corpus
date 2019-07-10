from cabnc_utilities import *

# Data source and output paths
archive_dir = "cabnc_archive/KB2/"
data_dir = "cabnc_data/text"

# Excluded characters for ignoring i.e. '=='
excluded_chars = {'<', '>', '-', '#', '&', '|', '=', '@', '', '[', ']'}
strip_chars = [':', '⌊', '⌋', '⌈', '⌉', '“', '”', '"', '(', ')', '◉']

file_name = "KB2RE00A.cha"
# Load the file data
file_data = load_text_data(archive_dir + file_name)

# Process each dialogue
dialogue = process_dialogue(file_data, file_name, excluded_chars, strip_chars)

for utt in dialogue['utterances']:
    print(utt)
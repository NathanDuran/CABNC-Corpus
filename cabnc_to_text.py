from cabnc_utilities import *

# Data source and output paths
archive_dir = "cabnc_archive/"
data_dir = "cabnc_data/text"

# If flag is set will only write utterances and not speaker
utterance_only_flag = False

# Excluded characters for ignoring i.e. '=='
excluded_chars = {'<', '>', '#', '&', '|', '=', '@', '', '[', ']'}
strip_chars = [':', '⌊', '⌋', '⌈', '⌉', '“', '”', '"', '(', ')', '◉']

# Get a list of all the dialogue directories
dialogue_dir_list = os.listdir(archive_dir)

for dialogue_dir in dialogue_dir_list:

    # Get a list of all the dialogues
    dialogue_list = os.listdir(archive_dir + "/" + dialogue_dir)

    for file_name in dialogue_list:
        # Load the file data
        file_data = load_text_data(archive_dir + "/" + dialogue_dir + "/" + file_name)

        # Process each dialogue
        dialogue = process_dialogue(file_data, file_name, excluded_chars, strip_chars)

        # Write to text file
        dialogue_to_text_file(data_dir + "/" + dialogue_dir, dialogue['dialogue_id'], dialogue, utterance_only_flag)

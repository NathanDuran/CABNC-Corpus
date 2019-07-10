from cabnc_utilities import *

# Data source and output paths
archive_dir = "cabnc_archive/"
data_dir = "cabnc_data/json"

# Excluded characters for ignoring i.e. '=='
excluded_chars = {'<', '>', '#', '&', '|', '=', '@', '', '[', ']'}
strip_chars = [':', '⌊', '⌋', '⌈', '⌉', '“', '”', '"', '(', ')', '◉']

# Get a list of all the dialogue directories
dialogue_dir_list = os.listdir(archive_dir)

for dialogue_dir in dialogue_dir_list:

    # Get a list of all the dialogues
    dialogue_list = os.listdir(archive_dir + "/" + dialogue_dir)

    dialogue_data = dict()
    dialogues = []

    for file_name in dialogue_list:
        # Load the file data
        file_data = load_text_data(archive_dir + "/" + dialogue_dir + "/" + file_name)

        # Process each dialogue
        dialogue = process_dialogue(file_data, file_name, excluded_chars, strip_chars)

        # Append to set
        dialogues.append(dialogue)

    # Add dataset metadata
    dialogue_data['dataset'] = "cabnc_" + dialogue_dir
    dialogue_data['num_dialogues'] = len(dialogues)
    dialogue_data['dialogues'] = dialogues

    # Save to JSON file
    save_json_data(data_dir, dialogue_data['dataset'], dialogue_data)
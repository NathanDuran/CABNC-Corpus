import os
import re
import traceback
import json
import spacy
from spacy.tokenizer import Tokenizer

nlp = spacy.load('en')
tokenizer = Tokenizer(nlp.vocab)


def process_dialogue(dialogue_file_data, file_name, excluded_chars, strip_chars):

    # Get the file name
    file_name = file_name.split('.')[0]

    tmp_utterances = []
    for line in dialogue_file_data:

        # Ignore non-dialogue lines that start with @ or %
        if line[0] is '@' or line[0] is '%':
            continue

        # Split on tab to get the speaker and text
        line = line.split('\t')
        speaker = re.sub('[*:]', '', line[0])
        text = line[1].strip()

        # Tokenise text
        utterance_tokens = tokenizer(text)
        utterance_tokens = [word.text for word in utterance_tokens]

        # Remove the word annotations and filter disfluency
        utterance_text = []
        for i, word in enumerate(utterance_tokens):

            # If no excluded characters are present just add it
            if all(char not in excluded_chars for char in word) and not any(char.isdigit() for char in word):

                # Strip any characters in the list
                if any(char in strip_chars for char in word):
                    word = re.sub('[:⌊⌋⌈⌉“”"◉()]', '', word)
                # If it is a redacted word i.e. 'xxx', replace with <unk>
                if 'xxx' in word:
                    word = word.replace('xxx', '<unk>')

                # Concatenate contractions that have been tokenised i.e "it" , "'s"
                if i + 1 < len(utterance_tokens):
                    next_word = utterance_tokens[i + 1]
                    if len(next_word) >= 2 and (next_word[0] == "'" or next_word[1] == "'"):
                        word += next_word
                        del utterance_tokens[i + 1]

                # Append the word
                utterance_text.append(word)

        # Remove empty words
        for i, word in enumerate(utterance_text):
            if word == ' ':
                del utterance_text[i]

        # Check for 'floating' punctuation (because other chars/words were removed)
        if len(utterance_text) >= 2 and all(char in ['.', '?', '!'] for char in utterance_text[-1]):
            # If so remove it from the end and add to the next word
            char = utterance_text.pop()
            utterance_text[-1] += char

        # Join words for complete sentence
        utterance_text = " ".join(utterance_text)
        # Strip leading and trailing whitespace
        utterance_text.strip()
        # Strip duplicate whitespace
        utterance_text = re.sub(' +', ' ', utterance_text)

        # Create utterances
        utterance = dict()
        # Set speaker
        utterance['speaker'] = speaker
        # Set the utterance text
        utterance['text'] = utterance_text
        # Set labels to empty
        utterance['ap_label'] = ""
        utterance['da_label'] = ""
        # Add empty slots data
        utterance['slots'] = dict()

        # Add to utterances
        tmp_utterances.append(utterance)

    dialogue = dict()
    utterances = []

    # Remove empty utterances
    for utt in tmp_utterances:
        if len(utt['text']) > 0 and not all(char in ['.', '?', '!', ' '] for char in utt['text']):
            utterances.append(utt)

    # Create dialogue
    dialogue['dialogue_id'] = file_name
    dialogue['num_utterances'] = len(utterances)
    dialogue['utterances'] = utterances

    return dialogue


def load_json_data(path, file_name):
    try:
        with open(path + file_name + ".json") as file:
            data = json.load(file)

    except (IOError, ValueError):
        traceback.print_exc()
        return False

    return data


def save_json_data(path, file_name, data):
    if not os.path.exists(path):
        os.mkdir(path)
    with open(path + "/" + file_name + '.json', 'w+') as file:
        json.dump(data, file, sort_keys=False, indent=4, separators=(',', ': '))


def load_text_data(path, verbose=True):
    with open(path, "r", encoding="utf8") as file:
        # Read a line and strip newline char
        lines = [line.rstrip('\r\n') for line in file.readlines()]
    if verbose:
        print("Loaded data from file %s." % path)
    return lines


def dialogue_to_text_file(path, file_name, data, utterance_only):
    if utterance_only:
        path = path + "_utt"
    if not os.path.exists(path):
        os.mkdir(path)
    with open(path + "/" + file_name + ".txt", 'w+', encoding="utf8") as file:
        for utt in data['utterances']:
            if utterance_only:
                file.write(utt['text'] + "\n")
            else:
                file.write(utt['speaker'] + "|" + utt['text'] + "\n")

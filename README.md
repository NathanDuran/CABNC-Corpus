# CABNC-Corpus
Utilities for Processing the [CABNC Corpus](https://ca.talkbank.org/access/CABNC.html) 
available from [TalkBank](https://talkbank.org/).
CABNC is a conversation analytic re-transcription of naturalistic conversations from a subcorpus of the British National Corpus
and contains around 4.2 million words in 1436 separate conversations.
The utilities process the original transcripts into plain text or json formats and remove disfluency and other annotation characters.
The intent is to create a more machine-readable format for NLP and computational modelling tasks.

## Scripts
cabnc_to_json.py script processes the dialogues from the original .cha format into .json files using the format
outlined below. Each dialogue set (KB0, KB1 etc) is output as a separate .json file.
This format is intended to facilitate annotation of the dialogue using the 
[Conversation Analysis Modelling Schema](https://nathanduran.github.io/Conversation-Analysis-Modelling-Schema/).

cabnc_to_text.py processes the dialogues from the original .cha format into plain text files,
with one line per-utterance, using the format outlined below.
Setting the *utterance_only* flag to true will remove the speaker label from the output text files.

cabnc_utilities.py script contains various helper functions for loading/saving and processing the data.

## Data Format
The original transcripts have had all disfluency and annotation characters removed. For example '|', '◉', '=', '@'.
The metadata headers and utterance timestamps (marked with '&#9633;') have also been removed.

Utterance marked with '0', i.e. silence/no transcription have been removed.

In the original transcripts contractions (I'll, Haven't etc) were split into separate tokens i.e I and 'll or Have and n't.
These have been concatenated to form the original contraction. This is to maintain grammatically correct sentences and 
it is trivial to re-tokenise the contractions.

Certain words, such as swear words or names, were redacted in the original transcripts and replaced with *'xxx'*.
These have been replaced with an *\<unk\>* token.

### Example Text Format
PS0X8|But they said wet and windy but that wasn't there was it.

PS0X9|I think that was more up North.

PS0X8|Oh up North right.

### Example JSON Format
The following is an example of the JSON format for the SCoSE corpus.

```json
    {
        "dataset": "dataset_name",
        "num_dialogues": 1,
        "dialogues": [
            {
                "dialogue_id": "dataset_name_1",
                "num_utterances": 2,
                "utterances": [
                    {
                        "speaker": "A",
                        "text": "Utterance 1 text.",
                        "ap_label": "AP-Label",
                        "da_label": "DA-Label"
                    },
                    {
                        "speaker": "B",
                        "text": "Utterance 2 text.",
                        "ap_label": "AP-Label",
                        "da_label": "DA-Label",
                        "slots": { //Optional
                            "slot_name": "slot_value"
                        }
                    }
                ],
                "scenario": { //Optional
                    "db_id": "1",
                    "db_type": "i.e booking",
                    "task": "i.e book",
                    "items": []
                }
            }
        ]
    }
```
## Licensing and Attribution
The original authors for the CABNC corpus: Saul Albert, Laura E. de Ruiter, and J.P. de Ruiter (2015) [CABNC: the Jeffersonian transcription of the Spoken British National Corpus](https://saulalbert.github.io/CABNC/).

The code within this repository is distributed under the [GNU General Public License](https://www.gnu.org/licenses/gpl-3.0.en.html).

The corpora available from [TalkBank](https://talkbank.org/), and the adapted format within this repository,
is licensed under a [Creative Commons Attribution 3.0 Unported License](http://creativecommons.org/licenses/by/3.0/).

<a rel="license" href="http://creativecommons.org/licenses/by/3.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/3.0/88x31.png" /></a>

# CABNC-Corpus
Utilities for Processing the [CABNC Corpus](https://ca.talkbank.org/access/CABNC.html) 
available from [TalkBank](https://talkbank.org/).
CABNC is a conversation analytic re-transcription of naturalistic conversations from a subcorpus of the British National Corpus
 and contains around 4.2 million words in 1436 separate conversations


## Scripts
cabnc_to_json.py script processes the 14 dialogues from the original .cha format into .json files using the format
outlined below.
This format is intended to facilitate annotation of the dialogue using the 
[Conversation Analysis Schema](https://nathanduran.github.io/CA-Schema/)
and [Dialogue tagger](https://github.com/NathanDuran/CA-Dialogue-Tagger).

cabnc_to_text.py processes the 14 dialogues from the original .cha format into plain text files,
with one line per-utterance, using the format outlined below.

cabnc_utilities.py script contains various helper functions for loading/saving and processing the data.

## Data Format
The original transcripts have had all disfluency and annotation characters removed. For example '|', '◉', '=', '@'.
The metadata 'headers' have also been removed.

Any sentences that are continued on another line by the same speaker (marked with '+') have been
concatenated to form complete uninterrupted sentences.

Certain words, such as swear words or names, were redacted in the original transcripts and replaced with *'xxx'*.
These have been raplaced with an *\<unk\>* token.

### Example Text Format
ERI|didn't they, didn't you ever hear that they, they found an entire woolly mammoth, frozen.

JAC|yeah, and they ate it.

ERI|an entire one though.

JAC|yeah.

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

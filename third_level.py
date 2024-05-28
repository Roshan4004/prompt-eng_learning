import json
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from my_paraphraser import paraphrase_sentence

# Original JSON data
f = open('main_data.json')
data=json.load(f)

new_format_data = []

for prompt in data:
    for sample in prompt["samples"]:
        para_imput=paraphrase_sentence(sample["input"])
        new_entry1 = {
            "messages": [
                {"role": "system", "content": "You are an English learning tutor."},
                {"role": "user", "content": para_imput},
                {"role": "assistant", "content": sample["output"]}
            ]
        }        
        new_format_data.append(new_entry1)
        new_entry2 = {
            "messages": [
                {"role": "system", "content": "You are an English learning tutor."},
                {"role": "user", "content": sample["input"]},
                {"role": "assistant", "content": sample["output"]}
            ]
        }
        new_format_data.append(new_entry2)

with open("third_level_data.jsonl", "w") as file:
    for entry in new_format_data:
        file.write(json.dumps(entry) + "\n")

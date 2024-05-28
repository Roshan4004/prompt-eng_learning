import json

# Original JSON data
f = open('main_data.json')
data=json.load(f)

new_format_data = []

for prompt in data:
    for sample in prompt["samples"]:
        new_entry = {
            "messages": [
                {"role": "system", "content": "You are an English learning tutor."},
                {"role": "user", "content": sample["input"]},
                {"role": "assistant", "content": sample["output"]}
            ]
        }
        new_format_data.append(new_entry)

with open("second_level_data.jsonl", "w") as file:
    for entry in new_format_data:
        file.write(json.dumps(entry) + "\n")

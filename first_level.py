import json

f=open("main_data.json")

data=json.load(f)

def convert_to_fine_tuning_format(original_data):
    fine_tuning_data = []
    for prompt_obj in original_data:
        prompt = prompt_obj["prompt"]
        for sample in prompt_obj["samples"]:
            fine_tuning_data.append({"prompt": sample["input"], "completion": sample["output"]})
    return fine_tuning_data

fine_tuning_data = convert_to_fine_tuning_format(data)
with open('first_level_data.jsonl', 'w') as f:
    for entry in fine_tuning_data:
        json.dump(entry, f)
        f.write('\n')

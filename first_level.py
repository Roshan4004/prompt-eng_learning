import json

f=open("main_data.json")

data=json.load(f)

def fine_tuning_format(real):
    ft_data = []
    for prompt_obj in real:
        prompt = prompt_obj["prompt"]
        for sample in prompt_obj["samples"]:
            ft_data.append({"prompt": sample["input"], "completion": sample["output"]})
    return ft_data

ft_data = fine_tuning_format(data)
with open('first_level_data.jsonl', 'w') as f:
    for entry in ft_data:
        json.dump(entry, f)
        f.write('\n')

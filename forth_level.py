import json
from my_paraphraser import paraphrase_sentence

# Original JSON data
f = open('main_data.json')
data=json.load(f)

new_format_data = []

def add_context_to_prompts(prompts):
    if "beginner" in prompts:
        sys_content = "You are an English learning tutor. This prompt is for beginner English learners so use a very beginner friendly vocabulary and be nice. "
    elif "intermediate" in prompts:
        sys_content = "You are an English learning tutor. This prompt is for intermediate English learners."
    elif "advanced" in prompts:
        sys_content = "You are an English learning tutor. This prompt is for advanced English learners. Make sure to ask them some questions as you're a good tutor."
    else:
        sys_content = "You are a really great and polite English learning tutor. You can even ask user's level in this field."
    return sys_content


for prompt in data:
    for sample in prompt["samples"]:
        sys_content=add_context_to_prompts(sample["input"])
        para_imput=paraphrase_sentence(sample["input"])
        new_entry1 = {
            "messages": [
                {"role": "system", "content": sys_content},
                {"role": "user", "content": para_imput},
                {"role": "assistant", "content": sample["output"]}
            ]
        }        
        new_format_data.append(new_entry1)
        new_entry2 = {
            "messages": [
                {"role": "system", "content": sys_content},
                {"role": "user", "content": sample["input"]},
                {"role": "assistant", "content": sample["output"]}
            ]
        }
        new_format_data.append(new_entry2)

with open("forth_level_data.jsonl", "w") as file:
    for entry in new_format_data:
        file.write(json.dumps(entry) + "\n")

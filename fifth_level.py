import json
from my_paraphraser import paraphrase_sentence

class PromptEngineer:
    def __init__(self):
        self.sys_contents = {
            "beginner": "You are an English learning tutor. This prompt is for beginner English learners so use simple words and be friendly.",
            "intermediate": "You are an English learning tutor. This prompt is for intermediate English learners.",
            "advanced": "You are an English learning tutor. This prompt is for advanced English learners. Ask them questions to help them learn better.",
            "default": "You are a really great and polite English learning tutor. You can even ask user's English profiency level"
        }
    def basic_prompt_completion(self, prompt, completion):
        return {"prompt": prompt, "completion": completion}
    def messages_format(self, role_contents):
        return {"messages": [{"role": i, "content": role_contents[i]} for i in role_contents.keys()]}
    def paraphrase(self, text):        
        return paraphrase_sentence(text)
    def add_context_to_prompts(self, prompt):
        if "beginner" in prompt:
            return self.sys_contents["beginner"]
        elif "intermediate" in prompt:
            return self.sys_contents["intermediate"]
        elif "advanced" in prompt:
            return self.sys_contents["advanced"]
        else:
            return self.sys_contents["default"]    

    
eng=PromptEngineer()
f = open('main_data.json')
data=json.load(f)

new_format_data = []

for prompt in data:
    for sample in prompt["samples"]:
        paraphared=eng.paraphrase(sample["input"])
        sys_prompt=eng.add_context_to_prompts(sample["input"])
        final1=eng.messages_format({"system":sys_prompt,"user":sample["input"],"assistant":sample["output"]})
        final2=eng.messages_format({"system":sys_prompt,"user":paraphared,"assistant":sample["output"]})
        new_format_data.append(final1)
        new_format_data.append(final2)

with open("fifth_level_data.jsonl", "w") as file:
    for entry in new_format_data:
        file.write(json.dumps(entry) + "\n")


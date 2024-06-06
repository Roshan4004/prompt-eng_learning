# Formatting the give data into specific format for fine-tuning.

## 1st level:
- Normal script to just change json to a fine-tuning "prompt-completion" which is a simple format. Usually, it's designed for simple prompt-response tasks where each interaction is a single exchange. Then I just save it into a jsonl file.
```
{"prompt": "What is the capital of France?", "completion": "Paris"}

```

## 2nd level:
- Now, instead of formatting into just prompt-completion format, I used "messages" format which have structure of multiple message with certain roles.
```
{
  "messages": [
    {"role": "system", "content": "You are an English learning tutor."},
    {"role": "user", "content": "What's the capital of France?"},
    {"role": "assistant", "content": "Paris"}
  ]
}

```

## 3rd level:
- Now, with the same "messages" format, I added a paraphrasing part. So, here the user's prompt/input is obviously used but also a paraphrased sentence of the user's prompt. This makes the prompt clearer to the model, and this improves how well AI understands and responds to it.

## 4th level:
- Finally, I added a function which looks for special key sets in the user's prompt and tells the AI/model to respond accordingly. This really improves the conversation between AI and the user as AI is told how to react as per user.
```
    IF "beginner" is in prompts THEN
        SET sys_content to "You are an English learning tutor. This prompt is for beginner English learners so use simple words and be friendly."
    ELSE IF "intermediate" is in prompts THEN
        SET sys_content to "You are an English learning tutor. This prompt is for intermediate English learners."
    ELSE IF "advanced" is in prompts THEN
        SET sys_content to "You are an English learning tutor. This prompt is for advanced English learners. Ask them questions to help them learn better."
    ELSE
        SET sys_content to "You are an English learning tutor. You can even ask the user their English proficiency level."
    END IF
```

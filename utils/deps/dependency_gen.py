



import os
import json
import openai
# openai.api_key = ""
prompt = """Here is the code. I don't know what language it is written in. I want you to find the language it is written in. Then get the dependency file for the code. The output should be in the format of json with keys "lang", "depsFileName","fileContent"

{}

I just want you to give me the json and nothing else. Don't explain me. Don't tell me anything else.
"""

def get_prompt(code):
    return prompt.format(code)

def is_valid_json(json_str):
    required_keys = ["lang", "depsFileName", "fileContent"]
    
    try:
        # Parse the JSON string
        data = json.loads(json_str)
        
        # Check if all required keys are present
        if all(key in data for key in required_keys):
            return True
        else:
            return False
    except json.JSONDecodeError:
        return False
      
def get_deps(code):
  prompt_in = prompt.format(code)
  completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": prompt_in}
  ]
  )
  return completion.choices[0].message.content


def json2file(output_json):
    file_name = output_json["depsFileName"]
    file_content = output_json["fileContent"]
    # Writing to the file
    with open(file_name, 'w') as file:
        file.write(file_content)

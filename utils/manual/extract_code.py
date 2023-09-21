import re

def extract_code_segments(text):
    pattern = r"```(.+?)```"
    return re.findall(pattern, text, re.DOTALL)


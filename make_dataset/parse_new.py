import os
import sys
i=0


def format_instruction(prompt, response):
	return f"""### Instruction:
Write a response that completes the INPUT.

### Input:
{prompt}

### Response:
{response}
"""

old_arr=[
"scripts_2023-08-30 15:20:26.txt",
"scripts_2023-08-30 16:02:38.txt",
"scripts_2023-08-30 16:09:54.txt",
"scripts_2023-08-30 16:55:26.txt",
"scripts_2023-08-30 17:33:07.txt",
"scripts_2023-08-30 17:52:49.txt",
"scripts_2023-08-30 22:06:19.txt",
"scripts_2023-08-31 10:56:27.txt",
"scripts_2023-08-31 16:08:23.txt",
"scripts_2023-08-31 16:30:01.txt",
"scripts_2023-08-31 16:38:34.txt",
"scripts_2023-08-31 16:45:38.txt",
"scripts_2023-08-31 16:56:38.txt",
"scripts_2023-09-01 19:36:17.txt"]

res_arr=[]
for file in os.listdir('../'):

    if "scripts_" not in file:
        continue
    if file in old_arr:
        continue
    print(file)
    f=open("../"+file,'r')
    lines=f.read()
    prompt_template_str='prompt template : '
    prompt_str='Prompt==================================================================\n'
    output_str='Output==================================================================\n'
    chunks=lines.split(prompt_template_str)
    prompt_arr=[]

    for chunk in chunks[1:]:
        instruction="Write a response that completes the INPUT."
        
        template_type=chunk.split(prompt_str)[0]
        template_type=template_type.split("/")[-2]+"/"+template_type.split("/")[-1].split(".")[0]
        
        prompt=chunk.split(output_str)[0].split(prompt_str)[1]
        response=chunk.split(output_str)[1].split('\n\n')[0]
        res={"instruction:":instruction,"input":prompt,"output":response, "template_type":template_type}
        res_arr.append(res)
        
    f.close()

import json
output_file = "./geag_data_new.json"

# Save the data as a JSON file
with open(output_file, "w") as json_file:
    json.dump(res_arr, json_file, indent=4)
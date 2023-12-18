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




res_arr=[]
f=open("/home/sngwon/workspace/generative_agents/scripts/scripts_2023-09-04 20:14:26.txt",'r')
lines=f.read()
prompt_template_str='prompt template : '
prompt_str='Prompt==================================================================\n'
output_str='Output==================================================================\n'
chunks=lines.split(prompt_str)
prompt_arr=[]

for chunk in chunks[1:]:
    #instruction="Write a response that completes the INPUT."
    prompt=chunk.split(output_str)[0]
    response=chunk.split(output_str)[1].split('\n\n')[0]
    #res={"instruction:":instruction,"input":prompt,"output":response}
    res={"input":prompt,"output":response}
    res_arr.append(res)
    
f.close()


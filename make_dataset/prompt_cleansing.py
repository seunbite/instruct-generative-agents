
import re
res_arr=[]


def cleanse_prompt(template_type, prompt, response):
    if template_type == "v2/wake_up_hour_v1":
        return prompt, response
    elif template_type == "v2/daily_planning_v6":
        return prompt, response
    elif template_type == "v2/generate_hourly_schedule_v2":
        prompt=prompt.split("===")[1]
        prompt=prompt.replace("Monday February 13 -- ", "")
        prompt = re.sub(r'\(\w+:\w+\) ', '', prompt)
        prompt=prompt.strip()
        if "\n" in response:
            response=response.split("\n")[0]
        return prompt, response
    

    elif template_type == "v2/task_decomp_v3": ##fix !
        instruction=prompt.split("---")[0]
        prompt=prompt.split("---")[2]
        prompt=prompt.strip()
        return "INSTRUCTION: "+ instruction + prompt, response
    
    
    elif template_type == "v1/action_location_sector_v1":
        instruction = prompt.split("Task -- ")[1].split("\n")[0]
        prompt=prompt.split("---")[2]
        prompt=prompt.strip()
        return "INSTRUCTION: "+ instruction+ "\n" + prompt, response
    elif template_type == "v1/action_object_v2":
        prompt=prompt.split("---")[6]
        prompt=prompt.strip()
        return prompt, response
    elif template_type == "v3_ChatGPT/generate_pronunciatio_v1":
        instruction=prompt.split('"""\n')[1].split("\n")[0]
        instruction=instruction + "\n" + \
                        """Output the response to the prompt above in json. The value for the output must ONLY contain the emojis. \n Example output json: {"output": "🛁🧖‍♀️"} """
        prompt="Action description:" + prompt.split("Action description:")[1].split('"""')[0]
        prompt=prompt.strip()
        return "INSTRUCTION: "+ instruction+ "\n" + prompt, response  
    elif template_type == "v2/generate_event_triple_v1":
        instruction = prompt.split("Task:")[1].split("\n")[0]
        instruction=instruction + "\n" + \
                        """Example output:\n---\n Input: Joon Park is brewing coffee.\n Output: (Joon Park, brew, coffee)\n ---\n Input: Jane Cook is sleeping. \n Output: (Jane Cook, is, sleep)\n ---\n Input: Michael Bernstein is writing email on a computer. \n Output: (Michael Bernstein, write, email)\n ---\n """
        instruction=instruction.strip()
        prompt=prompt.split("---")[6]
        prompt=prompt.strip()
        return "INSTRUCTION: "+ instruction+ "\n" + prompt, response
    elif template_type == "v2/decide_to_react_v1":
        instruction = prompt.split("Task -- ")[1].split("\n")[0]
        instruction=instruction + "\n" + \
                                """---\n Context: Sam is Sarah's friend. Sam and Sarah exchanged a conversation about favorite movies at 11pm, October 24, 2022. \n Right now, it is 12:40 pm, October 25, 2022. \n Sam is on the way to study for his test. \n Sam sees Sarah heading to do her laundry. \nMy question: Let's think step by step. Of the following three options, what should Sam do?\n Option 1: Wait on eating his lunch until Sarah is done doing her laundry\n Option 2: Continue on to eating his lunch now\n Reasoning: Sam is likely going to be in his room studying. Sarah, on the other hand, is likely headed to the laundry room for doing the laundry.\n Since Sam and Sarah need to use different areas, their actions do not conflict. \n So, since Sam and Sarah are going to be in different areas, Sam mcan continue on to eating his lunch now.\n Answer: Option 2\n---\n"""      
        prompt=prompt.split("---")[2]
        prompt=prompt.strip()
        return "INSTRUCTION: "+ instruction+ "\n" + prompt, response
    elif template_type =="v2/summarize_conversation_v1":
        instruction = prompt.split('\n\n\n')[1].split('"""\n')[0]
        prompt = prompt.split('\n\n\n')[0] + "\n" + prompt.split('"""\n')[2]
        return "INSTRUCTION: "+ instruction+ "\n" + prompt, response




    else:
        return prompt, response

list_arr=[
"/home/sngwon/workspace/generative_agents/scripts/scripts_2023-09-04 20:14:26.txt",
"/home/sngwon/workspace/generative_agents/scripts/scripts_2023-09-04 20:25:31.txt",
"/home/sngwon/workspace/generative_agents/scripts/scripts_2023-09-04 20:30:44.txt",
"/home/sngwon/workspace/generative_agents/scripts/scripts_2023-09-04 20:31:00.txt"
]
res_arr=[]
for file in list_arr:
    f=open(file,'r')
    lines=f.read()
    prompt_template_str='prompt template : '
    prompt_str='Prompt==================================================================\n'
    output_str='Output==================================================================\n'
    chunks=lines.split(prompt_template_str)

    for chunk in chunks[1:]:
        
        template_type=chunk.split("\n")[0]
        template_type=template_type.split("/")[-2]+"/"+template_type.split("/")[-1].split(".")[0]
        prompt=chunk.split(prompt_str)[1].split(output_str)[0].strip()
        response=chunk.split(output_str)[1].split('\n\n')[0].strip()
        prompt, response=cleanse_prompt(template_type, prompt, response)

        if "INSTRUCTION: " in prompt.split("\n")[0]:
            instruction=prompt.split("\n")[0]
            instruction=instruction.replace("INSTRUCTION: ", "")
            prompt=prompt.split("\n")[1:]
            prompt="\n".join(prompt)
        else:
            instruction="Write a response that completes the INPUT."
        
        
        
        res={"instruction": instruction, "input":prompt,"output":response, "template_type":template_type}
        res_arr.append(res)
    f.close()

import json
output_file = "./geag_data_n25_0906.json"

# Save the data as a JSON file
with open(output_file, "w") as json_file:
    json.dump(res_arr, json_file, indent=4)


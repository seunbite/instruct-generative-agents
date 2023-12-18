import json
import random

def shuffle_array(arr):
    random.shuffle(arr)
    return arr

data=json.load(open("/home/sngwon/workspace/generative_agents/make_dataset/geag_data_n25_0906.json",'r'))
data=shuffle_array(data)
template_dict={}

inference_data=[]
for sample in data:
    template_type=sample["template_type"]
    if template_type not in template_dict:
        template_dict[template_type]=1
    else:
        template_dict[template_type]+=1
    if template_dict[template_type]>10:
        continue
    inference_data.append(sample)
    
with open('./eval_data_0906.json', "w") as json_file:
    json.dump(inference_data, json_file, indent=4)



















# for sample in data:
#     template_type=sample["template_type"]
#     if template_type not in template_dict:
#         template_dict[template_type]=1
#         sample["split"]="train"
#     else:
#         template_dict[template_type]+=1
#         sample["split"]="train"
#     if template_dict[template_type]>10:
#         sample["split"]="val"
        

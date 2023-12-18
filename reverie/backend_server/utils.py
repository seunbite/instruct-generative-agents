# Copy and paste your OpenAI API Key
openai_api_key = "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"

# Put your name
key_owner = "sngwon"

maze_assets_loc = "../../environment/frontend_server/static_dirs/assets"
env_matrix = f"{maze_assets_loc}/the_ville/matrix"
env_visuals = f"{maze_assets_loc}/the_ville/visuals"

fs_storage = "../../environment/frontend_server/storage"
fs_temp_storage = "../../environment/frontend_server/temp_storage"

collision_block_id = "32125"

# Verbose 
debug = False

import time 
import datetime
cur_time=datetime.datetime.now()
cur_time=cur_time.strftime("%Y-%m-%d %H:%M:%S")
script_dir=f"/home/sngwon/workspace/generative_agents/scripts/scripts_{cur_time}.txt"

inference_lm="gpt"

#from inference import chat_completion
#def llama_inference(prompt):
#    chat_completion(model_name="/home/sngwon/llama-2-7b-chat-hf")
#    python inference/chat_completion.py --model_name /home/sngwon/llama-2-7b-chat-hf --prompt_file inference/chats.json  --quantization

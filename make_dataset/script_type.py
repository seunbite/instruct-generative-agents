import os

def read_file_by_line(file_name):
    arr=[]
    with open(file_name, "r") as f:
        while True:
            line = f.readline()
            if ".txt" in line:
                scripts=line.split("/")[-2]+"/"+line.split("/")[-1].split(".")[0]
                arr.append(scripts)
            if not line:
                break
    return arr


arr_=read_file_by_line("../reverie/backend_server/persona/prompt_template/run_gpt_prompt.py")

def save_elements_of_list_to_file(arr, file_name):
    with open(file_name, "w") as f:
        for i in arr:
            f.write(i+"\n")
save_elements_of_list_to_file(arr_, './geag_script_types.txt')
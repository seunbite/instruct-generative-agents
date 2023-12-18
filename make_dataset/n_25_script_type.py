import os

def read_file_by_line(list_arr):
    arr=[]
    for file_name in list_arr:
        with open(file_name, "r") as f:
            while True:
                line = f.readline()
                if "prompt template : " in line:
                    scripts=line.split("/")[-2]+"/"+line.split("/")[-1].split(".")[0]
                    if scripts not in arr:
                        arr.append(scripts)
                    
                if not line:
                    break
    return arr

list_arr=[
"/home/sngwon/workspace/generative_agents/scripts/scripts_2023-09-04 20:14:26.txt",
"/home/sngwon/workspace/generative_agents/scripts/scripts_2023-09-04 20:25:31.txt",
"/home/sngwon/workspace/generative_agents/scripts/scripts_2023-09-04 20:30:44.txt",
"/home/sngwon/workspace/generative_agents/scripts/scripts_2023-09-04 20:31:00.txt"
]
arr_=read_file_by_line(list_arr)

def save_elements_of_list_to_file(arr, file_name):
    with open(file_name, "w") as f:
        for i in arr:
            f.write(i+"\n")
save_elements_of_list_to_file(arr_, './n25_script_types_.txt')
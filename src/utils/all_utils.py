# this file will read the yaml file and return data in dict form 
import yaml 
import os 



def read_yaml(file_path:str ) -> dict :
    with open(file_path , mode='r') as file_ :
        retrived_data = yaml.safe_load(file_)
        file_.close()
        return retrived_data 

def create_dir(dirs_paths:list)-> None:
    for dir_path in dirs_paths:
        if not os.path.isdir(dir_path):
            os.makedirs(dir_path , exist_ok= True)  
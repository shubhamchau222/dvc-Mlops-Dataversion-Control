# this file will read the yaml file and return data in dict form 
import yaml 
import os 
import json



def read_yaml(file_path:str ) -> dict :
    with open(file_path , mode='r') as file_ :
        retrived_data = yaml.safe_load(file_)
        file_.close()
        return retrived_data 

def create_dir(dirs_paths:list)-> None:
    for dir_path in dirs_paths:
        if not os.path.isdir(dir_path):
            os.makedirs(dir_path , exist_ok= True)  


def save_df_local(data , storage_path , indexing = False):
    data.to_csv(storage_path , index=indexing)
    print(f"data is saved at path {storage_path}")



def save_reports(report: dict, report_path: str, indentation=4):
    with open(report_path, "w") as f:
        json.dump(report, f, indent=indentation)
    print(f"reports are saved at {report_path}")
    
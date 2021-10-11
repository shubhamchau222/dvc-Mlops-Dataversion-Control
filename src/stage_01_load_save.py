from src.utils.all_utils import read_yaml , create_dir 
import argparse
import pandas as pd 
import os


def get_data_from_config(config_path:str)-> dict:
    config_data = read_yaml(file_path=config_path)
    # let's unwrapped the config file 
    remote_data_path = config_data["data_source"]
    artiFacts_dir=  config_data["artifacts"]["artifacts_dir"]
    raw_local_dir =  config_data["artifacts"]["raw_local_dir"]
    nameOfFile = config_data["artifacts"]["raw_local_file"]
    artifact_MainDir = os.path.join(artiFacts_dir ,raw_local_dir )
    file_path_to_save =  os.path.join(artifact_MainDir , nameOfFile)
    # let's create the dir 
    create_dir([artifact_MainDir])
    df=pd.read_csv(remote_data_path , delimiter=';')
    df.to_csv(file_path_to_save , sep=',' , index=False)  # saving the csv file into local machine
    
 


if __name__ == "__main__":  # entry point 
    args = argparse.ArgumentParser()
    args.add_argument("--config" ,"-c" , default="config/config.yaml" ) 
    # adding the arguments , default = 'congig filepath'
    parsed_args = args.parse_args()
    get_data_from_config(parsed_args.config)
   

    
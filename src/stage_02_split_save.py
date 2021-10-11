from src.utils.all_utils import read_yaml , save_df_local , create_dir
import argparse
import pandas as pd 
import os
from sklearn.model_selection import train_test_split 


def split_and_save(config_path , params_path ):
    ''' Method : split_and_save
        task : split the data and store at given path  
    
    '''
    config= read_yaml(config_path)
    params= read_yaml(params_path)
    
    artifacts_dir = config["artifacts"]['artifacts_dir']
    raw_local_dir = config["artifacts"]['raw_local_dir']
    raw_local_file = config["artifacts"]['raw_local_file']
    raw_local_file_path = os.path.join(artifacts_dir, raw_local_dir, raw_local_file) # path to csv

    split_ratio = params["base"]["test_size"]
    random_state = params["base"]["random_state"]    

    # read the csv 
    df = pd.read_csv(raw_local_file_path)
    train_data , test_data = train_test_split(df , test_size = split_ratio , random_state =random_state)

    split_data_dir = config["artifacts"]["split_data_dir"] 
    create_dir([os.path.join(artifacts_dir, split_data_dir)]) # createing the split data dir

    train_fileName = config["artifacts"]["train"]
    test_fileName = config["artifacts"]["test"]
    train_path = os.path.join(artifacts_dir, split_data_dir , train_fileName )
    test_path = os.path.join(artifacts_dir , split_data_dir , test_fileName )

    save_df_local(data=train_data , storage_path=train_path , indexing=False)
    save_df_local(data=test_data , storage_path=test_path , indexing=False)

    print(train_path , test_path)

    
    






    
 


if __name__ == "__main__":  
    args = argparse.ArgumentParser()
    args.add_argument("--config" ,"-c" , default="config/config.yaml" )
    args.add_argument("--params" ,"-p" , default="./params.yaml" )
    parsed_args = args.parse_args()
    # print(parsed_args)
    split_and_save(config_path =parsed_args.config , params_path= parsed_args.params)
    
   

    
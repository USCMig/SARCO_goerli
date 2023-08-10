from etherscan import Etherscan
from web3 import Web3
import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
import os
from dotenv import load_dotenv

def read_csv(filepath):
    df = pd.read_csv(filepath)
    return df

def write_csv(df, file_path):
    df.to_csv(file_path, index=False)
    
def get_api_token(network):
    load_dotenv()
    api_key = os.getenv("ETHERSCAN_API_TOKEN")
    eth = Etherscan(api_key, net=network)
    return eth

def get_rpc():
    load_dotenv()
    rpc_http = os.getenv("GOERLI_RPC")
    w3 = Web3(Web3.HTTPProvider(rpc_http))
    return w3

def unix_to_time(df):
    df['timeStamp'] = df['timeStamp'].astype(int)
    df['timeStamp'] = pd.to_datetime(df['timeStamp'], unit='s')
    return df
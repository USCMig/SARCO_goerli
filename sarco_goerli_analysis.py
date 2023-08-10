import pandas as pd
from helper_functions import get_api_token, read_csv, write_csv, get_rpc
from sarco_data import create_address, create_address2
from web3 import Web3

df = read_csv("./outputs/sarco_contract.csv")

print(df.head(20))

w3 = get_rpc()
# Contract data
contract = [create_address, create_address2]

unique_events = df.groupby('functionName')['input'].unique()
print(unique_events)


# Number of unique addresses interacting w/ SARCO contract
unique_addy = df['from'].nunique()
print(f'Total number of unique users interacting w/ Sarco Contract are: {unique_addy} addresses')
avg_user_interaction = df.groupby('from')['txreceipt_status'].mean().mean()
print(f'Average number of contract interactions per user: {avg_user_interaction}')

cum_gas = df['gasPrice'].sum()
cum_gas_eth = cum_gas / 1000000000
print(f'Total Cumulative gas spend in Goerli is: {cum_gas} Gwei or {cum_gas_eth} gETH')

# df_pivot = df.pivot(index=['functionName','hash'], columns='methodId', values=['txreceipt_status','gasPrice'])
# print(df_pivot)
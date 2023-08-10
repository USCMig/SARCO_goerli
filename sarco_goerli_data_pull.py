import pandas as pd
from helper_functions import get_api_token, read_csv, write_csv, unix_to_time
from sarco_data import token_address, create_address, create_address2

eth = get_api_token("goerli")

def query_transfer(contract_address, page):
    df = pd.DataFrame()
    while True:
        data = eth.get_normal_txs_by_address_paginated(address=contract_address, page=page, offset=500, startblock=8637207, endblock=99999999 ,sort="asc")
        df_data = pd.DataFrame(data)
        df = pd.concat([df_data, df])

        if page < 19:
            break
        page += 1
        print(f'Total number of API calls used: {page}')

    df = unix_to_time(df)
    return df

df = query_transfer(contract_address=create_address2, page=0)

write_csv(df, "./outputs/sarco_contract5.csv")

print(df.head(20))
print(df.shape)

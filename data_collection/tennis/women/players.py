import pandas as pd
import requests as r
import os

def get_players_list(page=0, pageSize=100):
    url = f"https://api.wtatennis.com/tennis/players/ranked?page={page}&pageSize={pageSize}&type=rankSingles&metric=SINGLES&sort=asc&at=2023-07-02"
    params = {'Origin': 'https://www.wtatennis.com',
              'Referer': 'https://www.wtatennis.com'}
    response = r.get(url=url, headers=params).json()
    df = pd.json_normalize(response, max_level=1)
    return df

def initiate_player_data(page=0):
    for i in range(0, page+1):
        df = get_players_list(i)
        df.to_csv(os.getcwd() + '\data_collection\\tennis\women\player_data_' + str(i) +'.csv')

initiate_player_data(1)
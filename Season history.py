# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 10:23:46 2019

@author: Consultor
"""
import pandas as pd
import requests


columnas = ['id','league_id','season_id','stage_id','round_id','group_id',
            'aggregate_id','venue_id','referee_id','localteam_id',
            'visitorteam_id','winner_team_id','attendance','localteam_formation',
            'visitorteam_formation','localteam_score','visitorteam_score',
            'localteam_pen_score','visitorteam_pen_score','ht_score','ft_score',
            'et_score','date','time','localteam_coach_id','visitorteam_coach_id',
            'localteam_position','visitorteam_position']

season12919 = requests.get('https://soccer.sportmonks.com/api/v2.0/seasons/12919?api_token=pvd2DDFUl6dtaVtU5xq6yFtsHzcsbUIgFf4YftiqaIMprrNwv71t8dGVXo2G&include=results')
jseason12919 = season12919.json()
res12919 = jseason12919['data']['results']['data']
partido = []
df = pd.DataFrame(columns=columnas)

for i in range(197):
    partido = []
    for col in columnas:
        if col in ['localteam_formation','visitorteam_formation']:
            partido.append(res12919[i]['formations'][col])
        elif col in ['localteam_score','visitorteam_score','localteam_pen_score',
                     'visitorteam_pen_score','ht_score','ft_score','et_score']:
            partido.append(res12919[i]['scores'][col])
        elif col in ['date','time']:
            partido.append(res12919[i]['time']['starting_at'][col])
        elif col in ['localteam_coach_id','visitorteam_coach_id']:
            partido.append(res12919[i]['coaches'][col])
        elif col in ['localteam_position','visitorteam_position']:
            partido.append(res12919[i]['standings'][col])
        else:
            partido.append(res12919[i][col])
    df.loc[i] = partido

export_csv = df.to_csv(r'C:\Users\Consultor\seasonhist12919.csv', index=None, header=True)
            
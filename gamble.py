# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 10:55:29 2019
@author: Consultor
"""

import requests
import pandas as pd
import numpy as np

##############################################################################
##############################################################################

#Definición de Variables Globales

http = "https://soccer.sportmonks.com/api/v2.0/"
sm_token = "pvd2DDFUl6dtaVtU5xq6yFtsHzcsbUIgFf4YftiqaIMprrNwv71t8dGVXo2G"

##############################################################################

#Módulo de Funcioness por Endpoint (includes definidos por función)

def livescores_all():       #Recupera todos los partidos del día 
    incluidos = 'stats,events'
    http_request = requests.get(http + 'livescores?api_token={0}&include={1}'.format(sm_token,incluidos))
    live_day = http_request.json()
    ls_partidos_dia = live_day['data']
    col1 = ['id','league_id','localteam_id','visitorteam_id','winner_team_id']
    col2 = ['ht_score','ft_score','et_score']
    columnas = col1 + col2
    df_partidos = pd.DataFrame(columns=columnas)
    if  len(ls_partidos_dia) == 0:
        x = 'There are no matches today :('
        return(x)
    else:
        i = 0
        for partido in ls_partidos_dia:
            ls_registros = []
            for registro in col1:
                ls_registros.append(partido[registro])
            for registro in col2:
                ls_registros.append(partido['scores'][registro])
            df_partidos.loc[i] = ls_registros
            i = i + 1
        return(df_partidos)
        
def fixtures_id(partido_id):    #Análisis de estadísticas y eventos por partido
    incluidos = 'stats,events'
    http_request = requests.get(http + 'fixtures/{0}?api_token={1}&include={2}'.format(partido_id,sm_token,incluidos))
    fixture = http_request.json()
    fix_data = fixture['data']
    ls_stats = fix_data['stats']['data']        # resumen estadísticas por equipo
    ls_events = fix_data['events']['data']      # eventos cronológicos globales
    
    

        
        
import plotly.express as px
import plotly.graph_objects as go
import  plotly as py
import pandas as pd
import sys

def Analyze(LG, Inf, Office, Out):
    df_LG = pd.read_csv(LG, header=None, delimiter=',')
    df_office = pd.read_csv(Office, header=None, delimiter=',')
    df_LG.columns = ['type', 'x', 'y', 'area']
    df_LG = df_LG[df_LG['type']!='office']

    grouped = df_LG.groupby('type')
    list = []
    for name, group in grouped:
        d = {'type': name, 'count': len(group)}
        list.append(d)
    d = {'type': 'office', 'count': len(df_office)}
    list.append(d)
    df1 = pd.DataFrame(list)

    df_inf = pd.read_csv(Inf, header=None, delimiter=',')
    df_inf.columns = ['#time','x','y','location_type']
    grouped = df_inf.groupby('location_type')

    list = []

    for name, group in grouped:
        d = {'type': name, 'inf_count': len(group)}
        list.append(d)
    df2 = pd.DataFrame(list)

    df = pd.merge(df1, df2, on='type')

    df.to_csv(Out, index=False)

# Analyze('./ealing-out/ealing_buildings.csv', './ensemble07052020/ealing_eagle_hidalgo_1/RUNS/dynamic-lockdown-1-0.3_1/covid_out_infections.csv', './ensemble07052020/ealing_eagle_hidalgo_1/RUNS/dynamic-lockdown-1-0.3_1/offices.csv','./LG_Analysis/Ealing_LG_analysis.csv')
# Analyze('./Hammersmith_Fulham-out/Hammersmith_Fulham_buildings.csv', './ensemble07052020/hammersmith_fulham_eagle_hidalgo_1/RUNS/dynamic-lockdown-1-0.3_1/covid_out_infections.csv', './ensemble07052020/hammersmith_fulham_eagle_hidalgo_1/RUNS/dynamic-lockdown-1-0.3_1/offices.csv','./LG_Analysis/hammersmith_fulham_LG_analysis.csv')
# Analyze('./Harrow-out/harrow_buildings.csv', './ensemble07052020/harrow_eagle_hidalgo_1/RUNS/dynamic-lockdown-1-0.3_1/covid_out_infections.csv', './ensemble07052020/harrow_eagle_hidalgo_1/RUNS/dynamic-lockdown-1-0.3_1/offices.csv','./LG_Analysis/harrow_LG_analysis.csv')
Analyze('./hillingdon-out/hillingdon_buildings.csv', './ensemble07052020/hillingdon_eagle_hidalgo_1/RUNS/dynamic-lockdown-1-0.3_1/covid_out_infections.csv', './ensemble07052020/hillingdon_eagle_hidalgo_1/RUNS/dynamic-lockdown-1-0.3_1/offices.csv','./LG_Analysis/hillingdon_LG_analysis.csv')
# Analyze('./Kensington_Chelsea-out/Kensington_Chelsea_buildings.csv', './ensemble07052020/kensington_chelsea_eagle_hidalgo_1/RUNS/dynamic-lockdown-1-0.3_1/covid_out_infections.csv', './ensemble07052020/kensington_chelsea_eagle_hidalgo_1/RUNS/dynamic-lockdown-1-0.3_1/offices.csv','./LG_Analysis/Kensington_Chelsea_LG_analysis.csv')

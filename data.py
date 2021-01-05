import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from IPython.display import display, HTML, display_html

def convert_csv_to_df(path):
    df = pd.read_csv(path, header=0)
    return df

def construct_dataframe():
    df_happiness = convert_csv_to_df('datasets/world-happiness-report/2020.csv')
    df_countries = convert_csv_to_df('datasets/countries of the world.csv')
    merged_df = pd.merge(df_happiness, df_countries, how='inner', on='Country')
    merged_df.sort_values(by=['Rank'])
    merged_df.to_csv(r'datasets/output.csv')
    return merged_df

def display_side_by_side(*args):
    html_str=''
    for df in args:
        html_str+=df.to_html(index=False)
    display_html(html_str.replace('table','table style="display:inline"'),raw=True)
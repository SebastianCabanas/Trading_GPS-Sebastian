import os 
import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt
#data_path = "C:/Users/sebatiancabanas/Documents/KaxaNuk/Proyects/Trading-GPS/"

def stock_dic(data_path):
    list_stocks = os.listdir(data_path)
    data_dic = {}
    
    for ticker in list_stocks: 
        csv_path = os.path.join(data_path, ticker)
        data_dic[ticker] = pd.read_csv(csv_path)
    
    return data_dic


def stock_plot(df, save_plot=False, filename="grafico_p.png"):
    db_dict = {
        'c_adjusted_open': 'Open',
        'c_adjusted_high': 'High',
        'c_adjusted_low': 'Low',
        'm_adjusted_close': 'Close',
        'm_volume': 'Volume',
        'm_close': 'Adj Close',
        'c_simple_moving_average_21d': '21DMA',
        'c_simple_moving_average_63d': '63DMA',
        'c_simple_moving_average_252d': '252DMA'
    }
    df = df.rename(columns=db_dict)
    df['m_date'] = pd.to_datetime(df['m_date'])
    df.set_index('m_date', inplace=True)

    # Gráfica
    kws = dict(volume=True, tight_layout=True)
    for s in ['nightclouds']:
        ax = mpf.plot(df, **kws, style=s, type='hollow_and_filled')
        ax = ['21DMA'].plot(grid=True, color='blue', lw=1.09)
    
    return ax




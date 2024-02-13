#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 08:10:00 2024

@author: sebatiancabanas
"""

data_path = "input/Data_and_Features/"
import src.modules.custom_functions as fn

dic_stock = fn.stock_dic(data_path)
ej_ticker = dic_stock['AAPL.csv']  
fn.stock_ploti(ej_ticker)




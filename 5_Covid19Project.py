# -*- coding: utf-8 -*-
"""Untitled18.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1esGacbjIfRbkiyNwxfnkAc1zFhEMyGiN
"""

import pandas as pd
import csv
from datetime import datetime, timedelta
from geopy.geocoders import Nominatim
from geopy import distance
geolocator = Nominatim(user_agent="dlab.berkeley.edu-workshop")
file=str(input("Enter the patients .csv file name: "))
df_pat = pd.read_csv(file)
file=str(input("Enter the Places .csv file name: "))
df_pla = pd.read_csv(file)
d=int(input("Enter the Distance to check in *KM*: "))
s_pat=df_pat['sl.no']
s_pla=df_pla['S.no']
master = []
for i in range(len(s_pla)):
    print('i: ',i)
    for j in range(len(s_pat)):
        pat=[]
        p1_lat=df_pla['P_Lat'][i]
        p1_long=df_pla['P_Lon'][i]
        p2_lat=df_pat['lat'][j]
        p2_long=df_pat['long'][j]
        p1=(p1_lat,p1_long)
        p2=(p2_lat,p2_long)
        dist_lam = lambda c1,c2:round(distance.distance(c1,c2).m,2)
        dist=dist_lam(p1,p2)/1000
        print('J: ',j,'Dist: ',dist)
        if (dist<d):
            pat.append(p1_lat)
            pat.append(p1_long)
            pat.append(df_pat['Place'])
            pat.append(p2_lat)
            pat.append(p2_long)
            pat.append(df_pla['id'])
            pat.append(dist)
            master.append(pat)
df_mas = pd.DataFrame(master,columns=['Place','P_LAT','P_LONG','Contact','C_LAT','C_LONG','Distance'])
df_mas.to_csv('BufferZone_DataBase.csv')
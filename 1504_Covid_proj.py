

import pandas as pd
import csv
from datetime import datetime, timedelta
pat_id=[]
master=[]
masters=[]
check=[]
ti_s_pat=[]
ti_s_per=[]
file=str(input("Enter the patients .csv file name: "))
df_pat = pd.read_csv(file)
file=str(input("Enter the people .csv file name: "))
df_per = pd.read_csv(file)
d=int(input("Enter the Distance to check in *meters*: "))
t=int(input("Enter the Time bound in *sec*: "))
ti_pat=df_pat['time']
ti_per=df_per['time']
for i in range(len(ti_pat)):
    ti_s_pat.append(str(ti_pat[i]))
for i in range(len(ti_per)):
    ti_s_per.append(str(ti_per[i]))
from geopy.geocoders import Nominatim
from geopy import distance
geolocator = Nominatim(user_agent="dlab.berkeley.edu-workshop")
for i in range(len(ti_s_pat)):
    pat_id=[]
    pat_id.append(df_pat['id'][i])
    latlong=[]
    for j in range(len(ti_s_per)):
        d1=datetime.strptime(ti_s_pat[i],'%d-%m-%Y %H:%M')
        d2=datetime.strptime(ti_s_per[j],'%d-%m-%Y %H:%M')
        diff=(d2-d1).total_seconds()
        diff=abs(diff)
        if (diff<t) & (df_pat['id'][i] not in check):
            p1_lat=round(df_pat['lat'][i],5)
            p1_long=round(df_pat['long'][i],5)
            p2_lat=round(df_per['lat'][j],5)
            p2_long=round(df_per['long'][j],5)
            p1=(p1_lat,p1_long)
            p2=(p2_lat,p2_long)
            dist_lam = lambda c1,c2:round(distance.distance(c1,c2).m,2)
            dist=dist_lam(p1,p2)
            if dist<d:
                pat_id.append(df_per['id'][j])
                check.append(df_pat['id'][i])
                pat_id.append([p1,p2])
                pat_id.append(geolocator.reverse(p1).address)
                master.append(pat_id)
df_mas = pd.DataFrame(master,columns=['Source','Contact','Coordinate','Address'])
df_mas.to_csv('Contact_DataBase.csv')
import pandas as pd
import csv
from datetime import datetime, timedelta
pat_id=[]
master=[]
masters=[]
check=[]
file=str(input("Enter the .csv file name: "))
df = pd.read_csv(file)
ti=df['time']
ti_s=[]
for i in range(len(ti)):
    ti_s.append(str(ti[i]))
from geopy.geocoders import Nominatim
from geopy import distance
geolocator = Nominatim(user_agent="dlab.berkeley.edu-workshop")
for i in range(len(ti_s)):
    pat_id=[]
    latlong=[]
    pat_id.append(df['id'][i])
    check.append(df['id'][i])
    for j in range(len(ti_s)):
        if (df['id'][j] in check):
            pass
        else:
            d1=datetime.strptime(ti_s[i],'%d-%m-%Y %H:%M')
            d2=datetime.strptime(ti_s[j],'%d-%m-%Y %H:%M')
            diff=(d2-d1).total_seconds()
            if (diff<30):
                p1_lat=round(df['lat'][i],5)
                p1_long=round(df['long'][i],5)
                p2_lat=round(df['lat'][j],5)
                p2_long=round(df['long'][j],5)
                p1=(p1_lat,p1_long)
                p2=(p2_lat,p2_long)
                dist_lam = lambda c1,c2:round(distance.distance(c1,c2).m,2)
                dist=dist_lam(p1,p2)
                if dist<5:
                    pat_id.append(df['id'][j])
                    check.append(df['id'][j])
                    pat_id.append([p1,p2])
                    pat_id.append(geolocator.reverse(p1).address)
                    master.append(pat_id)
df_mas = pd.DataFrame(master,columns=['Source','Contact','Coordinate','Address'])
df_mas.to_csv('Patient_DataBase.csv')












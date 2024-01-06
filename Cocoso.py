import pandas as pd
import numpy as np

    #Excel dosyasını oku ve DataFrame'e dönustur
df_excel = pd.read_excel("C:/Users/gokha/OneDrive/Masaüstü/Tez/10.1-Cocoso.xlsx")
maliyet = df_excel.iloc[1:2].copy()
agirlik = df_excel.iloc[:1].copy()
df = df_excel.iloc[2:]  
satir_sayisi = df.shape[0] 
sutun_sayisi = df.shape[1]

mins = []
maxs = []
for i in range(sutun_sayisi):
        mins.append(df.iloc[:, i].min())  
        maxs.append(df.iloc[:, i].max())

ndm = df.copy() 
for i in range(sutun_sayisi):
    for j in range(satir_sayisi):
        if maliyet.iloc[0,i] == "fayda":
            ndm.iloc[j,i] = (df.iloc[j,i] - mins[i]) / (maxs[i] - mins[i])
        else:
            ndm.iloc[j,i] = (maxs[i] - df.iloc[j,i]) / (maxs[i] - mins[i])
       
wndm = ndm.copy()
for i in range(sutun_sayisi):
    for j in range(satir_sayisi):
        wndm.iloc[j,i] = ndm.iloc[j,i] * agirlik.iloc[0,i]

si = []
for i in range(satir_sayisi):
    toplam = 0
    for j in range(sutun_sayisi):
        toplam += wndm.iloc[i,j]
    si.append(toplam)

nwndm = wndm.copy()
for i in range(sutun_sayisi):
    for j in range(satir_sayisi):
        nwndm.iloc[j,i] = ndm.iloc[j,i] ** agirlik.iloc[0,i]
        
pi = []
for i in range(satir_sayisi):
    toplam = 0
    for j in range(sutun_sayisi):
        toplam += nwndm.iloc[i,j]
    pi.append(toplam)

sumsi = sum(si)
sumpi = sum(pi)
minsi = min(si)
minpi = min(pi)
maxsi = max(si)
maxpi = max(pi)
lam = 0.5

kia = []
for i in range(len(si)):
    kia.append( (si[i] + pi[i] ) / ( sumsi + sumpi ))

kib = []
for i in range(len(si)):
    kib.append( (si[i] / minsi ) + ( pi[i] / minpi ))
    
kic = []
for i in range(len(si)):
    kic.append( (lam * si[i] + (1-lam) * pi[i]) / (lam * maxsi + (1-lam) * maxpi))

ki = []
for i in range(len(si)):
    ki.append(((kia[i] * kib[i] * kic[i]) ** 1/3)+ (1/3 * (kia[i] + kib[i] + kic[i])))
    
print("\n")
for i in range(satir_sayisi):
    max_deger = max(ki)
    max_index = ki.index(max_deger)
    print(f"Cocoso Ki: {max_deger}, İndex: {max_index + 1}")
    ki[max_index] = -99999






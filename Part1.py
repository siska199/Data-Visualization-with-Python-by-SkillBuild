"""
Pembuat Matplotlib: John Hunter.
"""
import numpy as np
import pandas as pd

#Download Data Frame:

df_canada = pd.read_excel('https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DV0101EN/labs/Data_Files/Canada.xlsx',
            sheet_name='Canada by Citizenship',
            skiprows=range(20),
            skipfooter=2)
print(df_canada.head()) #Print 5 baris teratas
print(df_canada.tail()) #Print 5 baris terbawah
print(df_canada.info()) #Mengetahui info dari data frame


#Untuk mengetahui header kolom:
print(df_canada.columns.values.tolist())
#Untuk mengetahui index dari setiap baris:
print(df_canada.index.values.tolist())

#Mengetahui shape dari dataframe:
print(df_canada.shape) #baris x kolom

#men-drop kolom AREA, REG, DEV, Type, dan Converage:
df_canada.drop(['AREA', 'REG', 'DEV', 'Type','Coverage','Unnamed: 43', 'Unnamed: 44', 'Unnamed: 45', 'Unnamed: 46', 'Unnamed: 47', 'Unnamed: 48', 'Unnamed: 49', 'Unnamed: 50'],axis=1,inplace=True)
print(df_canada.head(2))

#Me-rename nama kolom:
df_canada.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'},inplace=True)
print(df_canada.columns.values)

#Menambah kolom yang menjumlahkan total imigran pada setiap negara untuk setiap tahunnya:
tot_imig = df_canada.sum(axis=1)
print(tot_imig)
df_canada['Total'] = tot_imig
print(df_canada.head(2))

#mengetahui jumlah nilai null pada DataFrame
print(df_canada.isnull().sum())

#Mendeskripsikan DataFrame
print(df_canada.describe())

#Cara Mencari Kolom-----------------
"""
df['column'] ---> (returns series)
df[['column 1', 'column 2']] ---> (returns dataframe)
"""

print(df_canada.Country)
print(df_canada[['Country', 1980, 1981, 1982, 1983, 1984, 1985]])

#Cara Menacari Baris--------------------
"""
df.loc[label] ---> filters by the labels of the index/column
df.iloc[index] ---> filters by the positions of the index/column
"""
#Set kolom Country sebagai index:
df_canada.set_index('Country', inplace=True)
#Menghilangkan index name: df_canada.index.name = None
print(df_canada.loc['Yemen'])
print(df_canada.iloc[192])

print(df_canada[2013]) #nama kolom masih dalam bentuk integer

#Merubah nama kolom menjadi string---------
df_canada.columns = (map(str,df_canada.columns))
print(df_canada.columns)

#-------------Plotting Gambar--------------------------
# %matplotlib inline: Untuk environtment notebook kode ini akan membuat gambar tampil di satu windows yang sama

#Buat grafik garis imigrasi dari Haiti
#Ekstrak Data Series dari Haiti:
import matplotlib as mpl
import matplotlib.pyplot as plt
years = list(map(str,range(1980,2014)))
haiti = df_canada.loc['Haiti',years] #[baris,kolom]
haiti.plot(kind='line')
plt.title('Immigration from Haiti')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')
plt.show()

#Plotting grafik garis imigrasi dari China dan India:

df_CI = df_canada.loc[['China','India'],years]
print(df_CI)

#Plot gambar:
df_CI = df_CI.transpose() #lakukan transpose pada dataframe agar lebih mudah untuk di plot
print(df_CI)

df_CI.plot(kind='line')
plt.title('Immigration from China dan India')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')
plt.show()
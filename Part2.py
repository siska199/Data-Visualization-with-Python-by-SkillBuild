#------------Cleaning Data----------------------#
import numpy as np
import pandas as pd

df_canada = pd.read_excel('https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DV0101EN/labs/Data_Files/Canada.xlsx',
            sheet_name='Canada by Citizenship',
            skiprows=20,
            skipfooter=2)
print(df_canada.head())
print(df_canada.tail())

print(df_canada.columns.values)
print(df_canada.index.values) 

#Menghilangkan beberapa kolom yang tidak perlu:
df_canada.drop(['AREA', 'REG', 'DEV', 'Type','Coverage','Unnamed: 43', 'Unnamed: 44', 'Unnamed: 45', 'Unnamed: 46', 'Unnamed: 47', 'Unnamed: 48', 'Unnamed: 49', 'Unnamed: 50'],axis=1,inplace=True)
print(df_canada.head())

df_canada.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'},inplace=True)

#Membuat kolom baru berupa total imigran:
df_canada['Total'] = df_canada.sum(axis=1)
print(df_canada.head())
#Merubah header menjadi string:
df_canada.columns = list(map(str,df_canada.columns))

#Menghitung nilai null yang ada
print(df_canada.isnull().sum())
#Mengetahui desktipsi, info dan ukuran dari data frame:
print(df_canada.info())
print(df_canada.describe())
print(df_canada.shape)
#Membuat data frame baru untuk keperluan pembuatan grafik:
df_canada.set_index('Country',inplace=True)
#Mengurutkan data dari nilai yang tertinggi
df_canada.sort_values(['Total'],ascending=False, axis=0, inplace=True)
print(df_canada.head())

#-----Plotting Grafik Area-------#
import matplotlib.pyplot as plt
import matplotlib as mpl
print(plt.style.available)
mpl.style.use(['ggplot'])
years = list(map(str,range(1980,2014)))

#Satu baris DataFrame
cina = df_canada.loc['China',years]
print(cina)
cina.plot(kind='area')
plt.title('Immigration from Cina')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')
plt.show()
plt.show()
#Dua baris DataFrame
df_CI = df_canada.loc[['China','India'],years]
df_CI = df_CI.transpose()
print(df_CI)
df_CI.plot(kind='area')
plt.title('Immigration from Cina dan India')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')
plt.show()

#Ekstrak top 5 nilai imigran tertinggi:
df_Top5 = df_canada.head(5)
print(years)
df_Top5 = df_Top5[years].transpose()
print(df_Top5)
df_Top5.plot(kind='area', stacked=False, figsize=(20,10)) #Grafik tidak bertumpuk
plt.title('Immigration Trend of Top 5 Countries')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')
plt.show()

#Plotting jenis kedua:
ax = df_Top5.plot(kind='area', alpha=0.5, figsize=(20, 10)) #Grafik bertumpuk

ax.set_title('Immigration Trend of Top 5 Countries')
ax.set_ylabel('Number of Immigrants')
ax.set_xlabel('Years')
plt.show()

#-----Plotting Grafik Histogram-------#
#Satu Data
df_canada['2013'].plot(kind='hist',figsize=(8,5))
plt.title('Histogram of Immigration from 195 Countries in 2013') # add a title to the histogram
plt.ylabel('Number of Countries') # add y-label
plt.xlabel('Number of Immigrants') # add x-label
plt.show()
#Memperbaiki gambar histogram:
count, bin_edges = np.histogram(df_canada['2013'])
print(count)
print(bin_edges)
df_canada['2013'].plot(kind='hist',figsize=(8,5),xticks=bin_edges)
plt.title('Histogram of Immigration from 195 Countries in 2013') # add a title to the histogram
plt.ylabel('Number of Countries') # add y-label
plt.xlabel('Number of Immigrants') # add x-label
plt.show()

#Tiga Data:
df_tiga = df_canada.loc[['Denmark', 'Norway', 'Sweden'],years]
df_tiga = df_tiga.transpose()
count, bin_edges = np.histogram(df_tiga,15)
print(count)
print(bin_edges)
df_tiga.plot(kind='hist',figsize=(10,6),bins=15,alpha=0.5, xticks=bin_edges,
        color=['coral', 'darkslateblue', 'mediumseagreen'])
plt.title('Histogram of Immigration from Denmark, Norway, and Sweden from 1980 - 2013')
plt.ylabel('Number of Years')
plt.xlabel('Number of Immigrants')
plt.show()

#-----Plotting Grafik Bar-------#
#Vertikal
df_canada = df_canada.loc['Iceland', years]
df_canada.plot(kind='bar', figsize=(10,6))
plt.xlabel('Year') # add to x-label to the plot
plt.ylabel('Number of immigrants') # add y-label to the plot
plt.title('Icelandic immigrants to Canada from 1980 to 2013') # add title to the plot
plt.show()

#Horizontal
df_canada = df_canada.loc['Iceland', years]
df_canada.plot(kind='barh', figsize=(10,6))
plt.xlabel('Year') # add to x-label to the plot
plt.ylabel('Number of immigrants') # add y-label to the plot
plt.title('Icelandic immigrants to Canada from 1980 to 2013') # add title to the plot
plt.show()

#Plotting grafik bar 15 negara dengan imigran tertinggi

df_Top5.plot(kind='bar',figsize=(20,10),stacked=False)
plt.title('Histogram of Immigration Top 5 from 1980 - 2013')
plt.ylabel('Number of Years')
plt.xlabel('Number of Immigrants')
plt.show()


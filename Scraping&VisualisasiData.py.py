#!/usr/bin/env python
# coding: utf-8

# In[14]:


import requests
from bs4 import BeautifulSoup
import csv

# menyimpan link web bukalapak  yang akan discrape ke variabel 
web_url = 'https://www.bukalapak.com/c/komputer/gaming/mouse-keyboard-gaming?page='


data = []  # List kosong untuk menyimpan data produk

# Melakukan perulangan untuk scraping pada halaman 2 hingga 6
for page in range(2, 5): 
    url = web_url + str(page)  # Membuat URL halaman yang akan discraping
    req = requests.get(url)  # Mengirim permintaan HTTP GET ke URL bukalapak
    soup = BeautifulSoup(req.text, 'html.parser')  # Membuat objek BeautifulSoup dari untuk memparse konten HTML
    product_items = soup.find_all('div', {'class': 'bl-product-card'})  # Mencari semua elemen dengan tag div dan class tersebut di variabel product_items
    
    # melakukan perulangan untuk mengambil masing2 item yng telah dicari di variabel product_items
    for item in product_items:
        # Mengambil nama, alamat, harga, dan rating produk dari elemen-elemen yang ditemukan
        nama = item.find('a', {'bl-link'}).text.strip()
        alamat = item.find('span', {'mr-4 bl-product-card__location bl-text bl-text--body-14 bl-text--subdued bl-text--ellipsis__1'}).text.strip() # Mencari semua elemen dengan tag span dan class tersebut di variabel address
        harga = item.find('p', {'class': 'bl-text bl-text--subheading-20 bl-text--semi-bold bl-text--ellipsis__1'}).text.strip() # Mencari semua elemen dengan tag p dan class tersebut di variabel price
        data.append([nama, alamat, harga])  # Menyimpan data dalam list data

# Membuat file CSV untuk menyimpan data
csv_file = 'DataProduk.csv'  

with open(csv_file, 'w', newline='', encoding='utf-8') as file: # Membuka file csv_file dengan mode write ('w') untuk menulis data
    writer = csv.writer(file) # Membuat objek writer dari modul CSV untuk menulis data ke dalam file.
    writer.writerow(['Nama', 'Alamat', 'Harga'])  # Menulis header kolom
    writer.writerows(data)  # Menambahkan data ke dalam file CSV


# In[28]:


import pandas as pd
import matplotlib.pyplot as plt

#Baca file
data = pd.read_csv('DataProduk.csv')

#Filter data berdasarkan kata kunci Keyboard dan Mouse
filter_data = data[data['Nama'].str.contains('Keyboard|Mouse', case=False)]

#Menghitung jumlah lokasi yang sesuai filter
hitunglokasi = filter_data['Alamat'].value_counts()

#Membuat bar chart
plt.bar(hitunglokasi.index, hitunglokasi.values)

#Menamai label
plt.xlabel('Lokasi')
plt.ylabel('Jumlah')

#Judul
plt.title('Jumlah Produk Keyboard dan Mouse di Setiap Daerah')

#Membuat tampilan label X agar tidak menumpuk
plt.xticks(rotation=45, ha='right')

#Save JPG
plt.savefig('BarChart_UAS.jpg')

#Tampilkan diagram
plt.show()


# In[29]:


import pandas as pd
import matplotlib.pyplot as plt


dt = pd.read_csv('DataProduk.csv')

#Filter data berdasarkan kata kunci 'Keyboard' dan 'Mouse' pada kolom Nama
filter_dt = dt[dt['Nama'].str.contains('Keyboard|Mouse', case=False)].copy()

#Menggabungkan lokasi Jakarta pusat,barat,utara dan timur
filter_dt.loc[filter_dt['Alamat'].str.contains('Jakarta', case=False), 'Alamat'] = 'Jakarta'

#filter agar hanya mengambil lokasi Bandung, Surabaya, Malang dan sleman
filter_dt = filter_dt[filter_dt['Alamat'].isin(['Bandung', 'Surabaya', 'Malang', 'Sleman', 'Jakarta'])]

#Menghitung jumlah lokasi yang sesuai filter
hitunglokasi = filter_dt['Alamat'].value_counts()

#Membuat Pie Chart
plt.pie(hitunglokasi.values, labels=hitunglokasi.index, autopct='%1.1f%%')

#Judul
plt.title('Persentase Keyboard dan Mouse di setiap daerah')

#Save jpg
plt.savefig('PieChart_UAS.jpg', dpi=300, bbox_inches='tight')

#Tampilkan
plt.show()


# In[ ]:





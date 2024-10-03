import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st 

sns.set(style='dark')

# Helper function yang dibutuhkan untuk menyiapkan berbagai dataframe
def create_sum_bike_per_month(df):
    sum_bike_per_month = bike_per_day_df.groupby('mnth')['cnt'].sum().reset_index()
    return sum_bike_per_month

def create_mean_bike_season(df):
    mean_bike_season = bike_per_day_df.groupby('season')['cnt'].mean().reset_index()
    return mean_bike_season

# Load cleaned data
bike_per_day_df = pd.read_csv("https://raw.githubusercontent.com/dwkysss/bike_per_day/refs/heads/main/day.csv")

datetime_columns = ["dteday"]

for column in datetime_columns:
  bike_per_day_df[column] = pd.to_datetime(bike_per_day_df[column])

with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://raw.githubusercontent.com/dwkysss/bike_per_day/main/bikesharing_logo.png")

# # Menyiapkan berbagai dataframe
monthly_rentals = create_sum_bike_per_month(bike_per_day_df)
seasonal_avg = create_mean_bike_season(bike_per_day_df)

# 
st.header('Bike Sharing Dashboard :sparkles:')
st.subheader('Perkembangan Peminjaman Sepeda per Bulan')
plt.figure(figsize=(12, 6))
sns.lineplot(x='mnth', y='cnt', data=monthly_rentals, marker='o', color='blue')

plt.xlabel('Bulan')
plt.ylabel('Jumlah Total Peminjaman Sepeda')
plt.xticks(ticks=range(1,13), labels=['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Agu', 'Sep', 'Okt', 'Nov', 'Des'])

plt.grid(True)
st.pyplot(plt)

st.subheader('Perbandingan Peminjaman Sepeda: Casual vs Registered')
total_casual = bike_per_day_df['casual'].sum()
total_registered = bike_per_day_df['registered'].sum()

plt.figure(figsize=(8, 6))
labels = ['Casual', 'Registered']
values = [total_casual, total_registered]
colors = ['lightblue', 'lightgreen']
plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors, explode=(0.05, 0.05))
st.pyplot(plt)

st.subheader('Rata-rata Peminjaman Sepeda Berdasarkan Musim')
seasonal_avg = bike_per_day_df.groupby('season')['cnt'].mean().reset_index()
colors = ["#D3D3D3", "#D3D3D3", "#72BCD4", "#D3D3D3"]
plt.figure(figsize=(8, 6))
sns.barplot(x='season', y='cnt', data=seasonal_avg, palette=colors)
plt.xlabel('Musim')
plt.ylabel('Rata-rata Jumlah Peminjaman Sepeda')
plt.xticks(ticks=range(4), labels=['Musim Dingin', 'Musim Semi', 'Musim Panas', 'Musim Gugur'])
st.pyplot(plt)
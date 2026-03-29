import streamlit as st
import pandas as pd
import time 
import os

# Konf page
st.set_page_config(page_title="AI Detec Dashboard", layout="wide")

st.title("AI Obj Detection Log")
st.subheader("Data hasil monitor lewat IP Camera android")

placeholder = st.empty()

log_file = 'detections_log.csv'

while True:
    if os.path.exists(log_file):
        df = pd.read_csv(log_file)

        df_latest = df.tail(10).iloc[::-1]

        with placeholder.container():
            # Baris pertama: Statistik Ringkas
            col1, col2 = st.columns(2)
            col1.metric("Total Deteksi", len(df))
            col2.metric("Objek Terakhir", df['Object'].iloc[-1] if not df.empty else "-")

            # Baris kedua: Tabel Data
            st.write("### 📋 Log Deteksi Terbaru")
            st.table(df_latest)

            # Baris ketiga: Grafik sederhana (jika ada data)
            if not df.empty:
                st.write("### 📊 Tren Objek")
                chart_data = df['Object'].value_counts()
                st.bar_chart(chart_data)

    # Refresh setiap 2 detik
    time.sleep(2)
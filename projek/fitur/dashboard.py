import streamlit as st
import datetime
import pandas as pd

# CSS to Streamlit 
st.markdown(
    """
    <style>
    /* Warna latar belakang aplikasi */
    .stApp {
        background-color: #F5F5DC;
    }

    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #228B22;
        color: white;
        padding: 5px;
    }

    /* Teks pada sidebar */
    [data-testid="stSidebar"] * {
        color: white !important;
        font-size: 16px;
        margin-bottom: 5px;
        margin-top: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

if 'donatur' not in st.session_state:
    st.session_state['donatur'] = []
if 'keuangan' not in st.session_state:
    st.session_state['keuangan'] = []  
if 'pengeluaran' not in st.session_state:
    st.session_state['pengeluaran'] = []  

# ini judul halaman nye
st.title("Dashboard🌙")
st.subheader("Ini adalah aplikasi alat hitung sederhana yang di khususkan untuk menghitung keuangan yayasan")
st.image("./img/logo.jpeg")

st.write("======================================================================================")
st.write("")

# Daftar Anggota Kelompok 2
st.subheader("Daftar Kelompok 2")
image_files = [
    {'img': './img/zul.jpeg', 'name': 'Zulfa Hasanul Karim'},
    {'img': './img/ham.jpeg', 'name': 'Muhammad Ilham Ramadan'},
    {'img': './img/din.jpeg', 'name': 'Andini'},
    {'img': './img/qai.jpeg', 'name': 'Kamila Qaisara Batrisyia'},
]

cols = st.columns(2)
for idx, image_info in enumerate(image_files):
    img_path = image_info['img']
    col_idx = idx % 2
    with cols[col_idx]:
        st.image(img_path, caption=image_info['name'])
    if col_idx == 1 and idx < len(image_files) - 1:
        cols = st.columns(2)


# =========================ini data pemasukan nye =========================
st.subheader("Rincian Pemasukan")
if st.session_state.keuangan:
    laporan_pemasukan = st.session_state.keuangan.laporan_pemasukan()
    if laporan_pemasukan:
        st.table(laporan_pemasukan)
    else:
        st.info("Belum ada data pemasukan.")
else:
    st.info("Belum ada data pemasukan.")

# ========================= ini rincian pengeluaran nye =========================
st.subheader("Rincian Pengeluaran")
if st.session_state.uang:
    laporan_pengeluaran = st.session_state.uang.laporan_pengeluaran()
    if laporan_pengeluaran:
        st.table(laporan_pengeluaran)
    else:
        st.info("Belum ada data pengeluaran.")
else:
    st.info("Belum ada data pengeluaran.")

# ========================= ini data donatur nye =========================
st.subheader("Data Donatur")
if st.session_state.donatur:
    data_donatur = st.session_state['donatur']
    if data_donatur:
        st.table(data_donatur)
    else:
        st.info("Belum ada data donatur.")
else:
    st.info("Belum ada data donatur.")

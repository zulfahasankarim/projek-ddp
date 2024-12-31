import streamlit as st

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

class Pemasukan:
    def __init__(self, nilai, keterangan):
        self.nilai = nilai 
        self.keterangan = keterangan

st.title("🪙Berikut adalah pemasukan Yayasan Darussakinah")

st.header("Jumlah pemasukan:")
nilai_pemasukan = st.number_input("Jumlah pemasukan:", min_value=0)
keterangan_pemasukan = st.text_input("Masukkan Keterangan Pemasukan")

if st.button("Kirim Pemasukan"):
    if nilai_pemasukan > 0 and keterangan_pemasukan.strip(): 
        pemasukan = Pemasukan(nilai_pemasukan, keterangan_pemasukan)
        st.session_state.keuangan.tambah_pemasukan(pemasukan)
        st.success("Pemasukan berhasil dicatat!")
    else:
        st.error("Silakan masukkan nilai pemasukan lebih dari 0 dan lengkapi keterangan!")

#menghitung total pemasukan nye
st.header("Total Pemasukan")    
st.write(f"Total Pemasukan: {st.session_state.keuangan.total_pemasukan()}")


st.header("Laporan Pemasukan")
laporan_pemasukan = st.session_state.keuangan.laporan_pemasukan()
if laporan_pemasukan:

    st.table(laporan_pemasukan)
else:
    st.info("Belum ada data pemasukan.")
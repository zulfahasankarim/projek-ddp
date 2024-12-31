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

class Pengeluaran:
    def __init__(self, nilai, keterangan):
        self.nilai = nilai 
        self.keterangan = keterangan


st.title("Berikut adalah pengeluaran Yayasan Darussakinah 💳")

st.header("Jumlah pengeluaran:")
nilai_pengeluaran = st.number_input("Jumlah pengeluaran:", min_value=0)
keterangan_pengeluaran = st.text_input("Masukkan Keterangan pengeluaran")

if st.button("Kirim pengeluaran"):
    if nilai_pengeluaran > 0 and keterangan_pengeluaran.strip():
        pengeluaran = Pengeluaran(nilai_pengeluaran, keterangan_pengeluaran)
        st.session_state.uang.tambah_pengeluaran(pengeluaran)
        st.success("pengeluaran berhasil dicatat!")
    else:
        st.error("Silakan masukkan nilai pengeluaran lebih dari 0 dan lengkapi keterangan!")


st.header("Total pengeluaran")
st.write(f"Total pengeluaran: {st.session_state.uang.total_pengeluaran()}")


st.header("Laporan pengeluaran")
laporan_pengeluaran = st.session_state.uang.laporan_pengeluaran()
if laporan_pengeluaran:
    st.table(laporan_pengeluaran)
else:
    st.info("Belum ada data pengeluaran.")
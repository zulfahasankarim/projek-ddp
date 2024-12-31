import streamlit as st

# Side Bar
dashboard = st.Page("./fitur/dashboard.py", title="Dashboard🌙")
pemasukan = st.Page("./fitur/pemasukan.py", title="Pemasukan🪙")
pengeluaran = st.Page("./fitur/pengeluaran.py", title="Pengeluaran💳")
donatur = st.Page("./fitur/donatur.py", title="Donatur🌟")

st.logo("img/logo.jpeg")
st.set_page_config(
    page_title="keuangan yayasan",
    page_icon="./img/logo.jpeg"
)
pg = st.navigation(
    {

        "Dashboard": [dashboard],
        "Transaksi": [pemasukan,pengeluaran,donatur]


    }


)

class Keuangan:
    def __init__(self):
        self.pemasukan_list = []

    def tambah_pemasukan(self, pemasukan):
        self.pemasukan_list.append(pemasukan)

    def total_pemasukan(self):
        return sum(pemasukan.nilai for pemasukan in self.pemasukan_list )

    def laporan_pemasukan(self):
        return [
            {"Keterangan": pemasukan.keterangan, "Nilai Pemasukan": pemasukan.nilai}
            for pemasukan in self.pemasukan_list
        ]

if "keuangan" not in st.session_state:
    st.session_state.keuangan = Keuangan()

class Uang:
    def __init__(self):
        self.pengeluaran_list = []

    def tambah_pengeluaran(self, pengeluaran):
        self.pengeluaran_list.append(pengeluaran)

    def total_pengeluaran(self):
        return sum(pengeluaran.nilai for pengeluaran in self.pengeluaran_list )

    def laporan_pengeluaran(self):
        return [
            {"Keterangan": pengeluaran.keterangan, "Nilai pengeluaran": pengeluaran.nilai}
            for pengeluaran in self.pengeluaran_list
        ]

if "uang" not in st.session_state:
    st.session_state.uang = Uang()


pg.run()

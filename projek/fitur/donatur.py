import streamlit as st
import datetime
import pandas as pd

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

# judul
st.title("🌟Donasi")
st.write("Bantu kami untuk terus memberikan dampak positif melalui donasi Anda. Setiap kontribusi sangat berarti!")

# ini form donasi nya
with st.form("donasi_form"):
    nama = st.text_input("Nama Lengkap", placeholder="Masukkan nama Anda")
    email = st.text_input("Email", placeholder="Masukkan email Anda")
    jumlah_donasi = st.number_input("Jumlah Donasi (Rp)", min_value=10000, step=10000)
    metode_pembayaran = st.selectbox("Metode Pembayaran", ["Transfer Bank", "Kartu Kredit", "E-Wallet", "PayPal"])
    pesan = st.text_area("Pesan untuk kami (Opsional)")


    submit_button = st.form_submit_button("Donasi Sekarang")

    #ini form
    if submit_button:
        if nama and email and jumlah_donasi:
            st.session_state['donatur'].append({
                'nama': nama,
                'email': email,
                'jumlah_donasi': jumlah_donasi,
                'metode_pembayaran': metode_pembayaran,
                'pesan': pesan
            })
            
            with open("donasi_log.txt", "a") as file:
                file.write(f"{datetime.datetime.now()}, {nama}, {email}, Rp{jumlah_donasi}, {metode_pembayaran}, {pesan}\n")
            
            st.success("Donasi Anda berhasil! Terima kasih atas dukungan Anda.")
        else:
            st.error("Harap lengkapi semua informasi yang diperlukan!")

st.markdown("---")
st.write("💖 Terima kasih atas dukungan dan kebaikan Anda.")

st.header("Data Donatur")
donatur = st.session_state['donatur']
if donatur:
    df = pd.DataFrame(donatur)
    st.dataframe(df)
else:
    st.info("Belum ada data donatur.")

import streamlit as st

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Sistem Pakar Hemofilia", page_icon="🩸", layout="centered")

# --- CSS CUSTOM UNTUK TAMPILAN FORMAL ---
st.markdown("""
    <style>
    .stApp {
        background-color: #f8f9fa;
    }
    .main-title {
        color: #d90429;
        font-family: 'Times New Roman', serif;
        font-size: 32px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 30px;
        border-bottom: 2px solid #d90429;
        padding-bottom: 10px;
    }
    .login-container {
        background-color: white;
        padding: 40px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    footer {text-align: center; color: gray; font-size: 12px; margin-top: 50px;}
    </style>
    """, unsafe_allow_html=True)

# --- FUNGSI LOGIN ---
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

def login():
    st.markdown("<div class='main-title'>SISTEM PAKAR MENDIAGNOSA PENYAKIT HEMOFILIA PADA MANUSIA</div>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.markdown("<h3 style='text-align: center;'>Halaman Login</h3>", unsafe_allow_html=True)
        with st.form("login_form"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            submit = st.form_submit_button("Masuk ke Sistem")
            
            if submit:
                # Kamu bisa ganti username & password di sini
                if username == "admin" and password == "hemofilia123":
                    st.session_state['logged_in'] = True
                    st.rerun()
                else:
                    st.error("Username atau Password salah!")
        st.info("Gunakan username: **admin** dan password: **hemofilia123**")

# --- DATA MASTER ---
daftar_gejala = {
    "G01": "Mimisan mendadak dan sulit berhenti", "G02": "Pendarahan gusi tanpa sebab yang jelas",
    "G03": "Luka kecil sulit berhenti berdarah", "G04": "Memar (hematoma) lama hilang",
    "G05": "Pendarahan setelah cabut gigi", "G06": "Pendarahan pasca operasi",
    "G07": "Pendarahan pada otot", "G08": "Pendarahan pada sendi (lutut, siku, pergelangan)",
    "G09": "Nyeri pada sendi", "G10": "Pembengkakan sendi",
    "G11": "Pendarahan akibat benturan ringan", "G12": "Pendarahan spontan (tanpa sebab yang jelas)",
    "G13": "Pendarahan pada saluran pencernaan", "G14": "Pendarahan di kepala (gejala neurologis)",
    "G15": "Riwayat keluarga menderita Hemofilia"
}

daftar_solusi = {
    "S01": "Penanganan lokal (tekan, kompres, perban)", "S02": "Obat pendukung (antifibrinolitik, desmopressin)",
    "S03": "Edukasi pencegahan pendarahan", "S04": "Kesadaran terhadap risiko cedera dan pendarahan",
    "S05": "Terapi faktor pembekuan saat diperlukan (on-demand)", "S06": "Fisioterapi untuk menjaga kesehatan sendi",
    "S07": "Monitoring medis berkala", "S08": "Edukasi aktivitas (menghindari olahraga kontak berat)",
    "S09": "Terapi profilaksis rutin (faktor VIII/IX)", "S10": "Penanganan darurat untuk pendarahan internal",
    "S11": "Rehabilitasi jangka panjang", "S12": "Menghindari obat aspirin dan NSAID"
}

# --- LOGIKA TAMPILAN ---
if not st.session_state['logged_in']:
    login()
else:
    # --- TAMPILAN UTAMA SETELAH LOGIN ---
    st.sidebar.title("Navigasi")
    page = st.sidebar.radio("Pilih Menu", ["🏠 Beranda", "🩺 Diagnosa", "🚪 Keluar"])

    if page == "🏠 Beranda":
        st.markdown("<div class='main-title'>SISTEM PAKAR MENDIAGNOSA PENYAKIT HEMOFILIA PADA MANUSIA</div>", unsafe_allow_html=True)
        st.write("### Selamat Datang, Admin")
        st.write("""
        Sistem Pakar ini menggunakan metode **Forward Chaining** untuk menentukan tingkat keparahan 
        penyakit Hemofilia (Ringan, Sedang, atau Berat) berdasarkan gejala klinis yang dialami pasien.
        """)
        st.image("https://img.freepik.com/free-vector/blood-donation-concept-illustration_114360-5554.jpg", width=400)

    elif page == "🩺 Diagnosa":
        st.markdown("### Formulir Diagnosa Pasien")
        nama = st.text_input("Nama Lengkap Pasien")
        gejala_user = []
        
        st.write("---")
        st.write("**Pilih Gejala yang Terdeteksi:**")
        cols = st.columns(2)
        for i, (k, v) in enumerate(daftar_gejala.items()):
            col = cols[0] if i < 8 else cols[1]
            if col.checkbox(f"{k} - {v}"):
                gejala_user.append(k)

        if st.button("Proses Hasil Diagnosa"):
            if not nama or not gejala_user:
                st.warning("Mohon lengkapi data!")
            else:
                rules = [
                    {"nama": "Hemofilia Ringan", "gejala": ["G01", "G02", "G03", "G04", "G05", "G06", "G09", "G10", "G11", "G15"], "solusi": ["S01", "S02", "S03", "S04"]},
                    {"nama": "Hemofilia Sedang", "gejala": ["G01", "G02", "G03", "G04", "G05", "G06", "G07", "G08", "G09", "G10", "G11", "G15"], "solusi": ["S05", "S06", "S07", "S08"]},
                    {"nama": "Hemofilia Berat", "gejala": ["G01", "G02", "G04", "G06", "G07", "G08", "G09", "G10", "G12", "G13", "G14", "G15"], "solusi": ["S09", "S10", "S11", "S12"]}
                ]
                
                hasil = None
                for r in reversed(rules):
                    if any(g in gejala_user for g in r["gejala"]):
                        hasil = r
                        break
                
                if hasil:
                    st.success(f"### Hasil Diagnosa: {hasil['nama']}")
                    st.write("**Rekomendasi Tindakan:**")
                    for s in hasil['solusi']:
                        st.write(f"- {daftar_solusi[s]}")
                else:
                    st.info("Gejala tidak spesifik.")

    elif page == "🚪 Keluar":
        st.session_state['logged_in'] = False
        st.rerun()

st.markdown("<footer>&copy; 2026 Muhammad Rizal Nurrohman - Universitas Al-Khairiyah</footer>", unsafe_allow_html=True)

import streamlit as st

# ================== KONFIGURASI HALAMAN ==================
st.set_page_config(page_title="Sistem Pakar Penyakit Hemofilia", page_icon="🩸", layout="centered")

# ================== CUSTOM CSS (OPTIMASI KONTRAS & UI) ==================
st.markdown("""
    <style>
    .stApp {
        background-color: #F4F6F9 !important;
    }
    
    /* Memastikan teks terbaca jelas (Hitam Pekat) */
    p, label, span, li, div, h3, .stMarkdown {
        color: #1A1D23 !important; 
        font-weight: 500 !important;
    }

    /* Tombol Merah dengan teks Putih */
    div.stButton > button {
        background-color: #D32F2F !important;
        color: #FFFFFF !important;
        border-radius: 8px !important;
        border: none !important;
        font-weight: bold !important;
        width: 100%;
    }

    /* Kotak Header */
    .top-header-red {
        background-color: #B71C1C;
        color: #FFFFFF !important;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 20px;
    }
    .top-header-red h1 {
        color: #FFFFFF !important;
        margin: 0;
    }

    /* Checkbox agar kontras */
    div[data-testid="stCheckbox"] {
        background-color: #ffffff;
        padding: 10px;
        border-radius: 8px;
        border: 1px solid #ced4da;
        margin-bottom: 8px;
    }

    /* Card Hasil */
    .result-card {
        background-color: #FFFFFF;
        border-radius: 15px;
        padding: 25px;
        border: 2px solid #D32F2F;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    .severity-card {
        background-color: #FFFFFF;
        border-radius: 10px;
        padding: 15px;
        text-align: center;
        border: 1px solid #ddd;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# ================== DATA SISTEM PAKAR ==================
daftar_gejala = {
    "G01": "Mimisan mendadak dan sulit berhenti",
    "G02": "Pendarahan gusi tanpa sebab yang jelas",
    "G03": "Luka kecil sulit berhenti berdarah",
    "G04": "Memar (hematoma) lama hilang",
    "G05": "Pendarahan setelah cabut gigi",
    "G06": "Pendarahan pasca operasi",
    "G07": "Pendarahan pada otot",
    "G08": "Pendarahan pada sendi",
    "G09": "Nyeri pada sendi",
    "G10": "Pembengkakan sendi",
    "G11": "Pendarahan akibat benturan ringan",
    "G12": "Pendarahan spontan",
    "G13": "Pendarahan pada saluran pencernaan",
    "G14": "Pendarahan di kepala",
    "G15": "Riwayat keluarga hemofilia"
}

daftar_solusi = {
    "S01": "Penanganan lokal (tekan, kompres, perban)",
    "S02": "Obat pendukung (antifibrinoltik, desmopressin)",
    "S03": "Edukasi pencegahan",
    "S04": "Kesadaran terhadap resiko cedera dan pendarahan",
    "S05": "Terapi faktor pembekuan saat diperlukan (on-demand)",
    "S06": "Fisioterapi untuk mencegah kerusakan sendi",
    "S07": "Monitoring medis berkala",
    "S08": "Edukasi aktivitas (menghindari olahraga kontak berat)",
    "S09": "Terapi profilaksis rutin (factor VIII/IX)",
    "S10": "Penanganan darurat untuk pendarahan internal",
    "S11": "Rehabilitasi jangka panjang",
    "S12": "Menghindari obat aspirin dan NSAID karena meningkatkan resiko pendarahan"
}

rules = [
    {
        "nama": "Hemofilia A (Klasifikasi: Berat)", 
        "gejala": ["G01","G02","G04","G06","G07","G08","G09","G10","G12","G13","G14","G15"], 
        "solusi": ["S09","S10","S11","S12"]
    },
    {
        "nama": "Hemofilia B (Klasifikasi: Sedang)", 
        "gejala": ["G01","G02","G03","G04","G05","G06","G07","G08","G09","G10","G11","G15"], 
        "solusi": ["S05","S06","S07","S08"]
    },
    {
        "nama": "Hemofilia C (Klasifikasi: Ringan)", 
        "gejala": ["G01","G02","G03","G04","G05","G06","G09","G10","G11","G15"], 
        "solusi": ["S01","S02","S03","S04"]
    }
]

# ================== STATE MANAGEMENT ==================
if "page" not in st.session_state:
    st.session_state.page = "Login"
if "gejala_terpilih" not in st.session_state:
    st.session_state.gejala_terpilih = []
if "nama_pasien" not in st.session_state:
    st.session_state.nama_pasien = ""

# ================== HALAMAN LOGIN ==================
if st.session_state.page == "Login":
    st.markdown('<div class="top-header-red"><h1>🩸 LOGIN</h1></div>', unsafe_allow_html=True)
    st.write("<br>", unsafe_allow_html=True)
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("MASUK KE SISTEM"):
        if username == "admin" and password == "123":
            st.session_state.page = "Menu Utama"
            st.rerun()
        else:
            st.error("Kredensial salah!")

# ================== MENU UTAMA ==================
elif st.session_state.page == "Menu Utama":
    st.markdown('<div class="top-header-red"><h1>🏠 MENU UTAMA</h1></div>', unsafe_allow_html=True)
    
    st.markdown(f'''
        <div style="background:white; padding:20px; border-radius:15px; border-left:8px solid #B71C1C; margin-bottom:20px;">
            <h3 style="margin:0; color:#B71C1C !important;">Halo, Admin! 👋</h3>
            <p style="margin:0; font-size:14px;">Selamat datang di sistem deteksi dini Hemofilia.</p>
        </div>
    ''', unsafe_allow_html=True)

    if st.button("🚀 MULAI PENYAKIT SEKARANG"):
        st.session_state.page = "Penyakit"
        st.rerun()

    st.markdown("<br><p style='text-align:center; font-weight:bold;'>Menu Navigasi Cepat</p>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        if st.button("📖 Edukasi Penyakit"):
            st.info("Fitur edukasi dalam pengembangan.")
    with c2:
        if st.button("🚪 Keluar Akun"):
            st.session_state.page = "Login"
            st.rerun()

# ================== HALAMAN PROSES PENYAKIT ==================
elif st.session_state.page == "Penyakit":
    st.markdown('<div class="top-header-red"><h1>📋 PROSES PENYAKIT</h1></div>', unsafe_allow_html=True)
    
    with st.form("form_penyakit"):
        nama_input = st.text_input("Nama Pasien")
        umur_input = st.number_input("Umur Pasien", 0, 120)
        st.markdown("---")
        st.subheader("Ceklis Gejala yang Dirasakan:")
        
        gejala_user = []
        for kode, teks in daftar_gejala.items():
            if st.checkbox(teks, key=kode):
                gejala_user.append(kode)
        
        st.markdown("---")
        st.markdown("<p style='font-weight:bold; color:#B71C1C !important;'>Referensi Tingkat Keparahan:</p>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown('<div class="severity-card">RINGAN</div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="severity-card">SEDANG</div>', unsafe_allow_html=True)
        with col3:
            st.markdown('<div class="severity-card">BERAT</div>', unsafe_allow_html=True)
        
        st.write("<br>", unsafe_allow_html=True)
        if st.form_submit_button("PROSES HASIL PENYAKIT"):
            st.session_state.gejala_terpilih = gejala_user
            st.session_state.nama_pasien = nama_input
            st.session_state.page = "Hasil"
            st.rerun()
            
    if st.button("Kembali"):
        st.session_state.page = "Menu Utama"
        st.rerun()

# ================== HALAMAN HASIL PENYAKIT ==================
elif st.session_state.page == "Hasil":
    st.markdown('<div class="top-header-red"><h1>📊 LAPORAN HASIL PENYAKIT</h1></div>', unsafe_allow_html=True)
    
    gejala_terpilih = st.session_state.gejala_terpilih
    nama = st.session_state.nama_pasien if st.session_state.nama_pasien else "Pasien"

    if not gejala_terpilih:
        st.warning("Data penyakit belum tersedia. Silakan pilih gejala terlebih dahulu.")
    else:
        hasil_final = None
        for r in rules:
            cocok = len([g for g in r["gejala"] if g in gejala_terpilih])
            if cocok >= len(r["gejala"]) * 0.5:
                hasil_final = r
                break
        
        if hasil_final:
            st.markdown(f'''
                <div class="result-card">
                    <h3 style="color:#B71C1C !important; text-align:center;">Kesimpulan: {hasil_final['nama']}</h3>
                    <p><b>Nama Pasien:</b> {nama}</p>
                    <hr>
                    <p><b>Manifestasi Klinis Terdeteksi:</b></p>
                    <ul>
                        {"".join([f"<li>{daftar_gejala[g]}</li>" for g in gejala_terpilih])}
                    </ul>
                    <p style="margin-top:15px;"><b>Rekomendasi Tindakan:</b></p>
                    <ul style="color:#B71C1C !important; font-weight:bold;">
                        {"".join([f"<li>{daftar_solusi[s]}</li>" for s in hasil_final['solusi']])}
                    </ul>
                </div>
            ''', unsafe_allow_html=True)
            st.write("<br>", unsafe_allow_html=True)
            st.button("UNDUH LAPORAN (PDF)")
        else:
            st.error("Sistem tidak menemukan indikasi spesifik berdasarkan kriteria database kami.")

    if st.button("KEMBALI KE MENU UTAMA"):
        st.session_state.gejala_terpilih = []
        st.session_state.page = "Menu Utama"
        st.rerun()

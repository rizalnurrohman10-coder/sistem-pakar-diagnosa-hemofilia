import streamlit as st

# ================== KONFIGURASI HALAMAN ==================
st.set_page_config(page_title="Sistem Pakar Hemofilia", page_icon="🩸", layout="centered")

# ================== CUSTOM CSS (REDESIGN UI MOBILE) ==================
st.markdown("""
    <style>
    /* Mengatur background utama dan menyembunyikan elemen bawaan Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .stApp {
        background-color: #E8ECEF;
        background-image: radial-gradient(circle at 50% top, #3A404A 0%, #1A1D24 100%);
        background-attachment: fixed;
    }

    /* Container untuk mensimulasikan layar HP */
    .mobile-container {
        max-width: 450px;
        margin: 0 auto;
        padding-top: 2rem;
    }

    /* ============ LOGIN PAGE ============ */
    .glass-login {
        background: rgba(255, 255, 255, 0.85);
        backdrop-filter: blur(15px);
        border-radius: 20px;
        padding: 30px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        border: 1px solid rgba(255,255,255,0.5);
    }
    .login-logo {
        text-align: center;
        color: #B71C1C;
        font-size: 24px;
        font-weight: 800;
        margin-bottom: 5px;
    }
    .login-welcome {
        text-align: center;
        color: #333;
        font-size: 18px;
        font-weight: bold;
        margin-bottom: 20px;
    }

    /* ============ MAIN DASHBOARD ============ */
    .dash-bg {
        background-color: #F4F6F9 !important;
    }
    .top-header-red {
        background-color: #B71C1C;
        color: white;
        padding: 20px;
        border-radius: 0 0 25px 25px;
        text-align: left;
        font-weight: bold;
        font-size: 20px;
        margin-top: -3rem;
        margin-bottom: 20px;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    .welcome-text {
        color: #333;
        font-weight: bold;
        padding: 0 10px;
        margin-bottom: 10px;
    }
    
    /* Panel Banner Hidup Sehat */
    .health-banner {
        background: linear-gradient(135deg, #D32F2F, #B71C1C);
        border-radius: 15px;
        padding: 20px;
        color: white;
        margin-top: 20px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }

    /* ============ CARDS & BUTTONS ============ */
    .stButton > button {
        background-color: #D32F2F !important;
        color: white !important;
        border-radius: 12px !important;
        border: none !important;
        padding: 10px 20px !important;
        font-weight: bold !important;
        width: 100%;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(211, 47, 47, 0.3);
    }
    .stButton > button:hover {
        background-color: #B71C1C !important;
        transform: translateY(-2px);
    }
    .btn-secondary > button {
        background-color: #FFFFFF !important;
        color: #D32F2F !important;
        border: 2px solid #D32F2F !important;
        box-shadow: none !important;
    }

    /* Kartu Gejala & Keparahan */
    .severity-card {
        background-color: white;
        border-radius: 10px;
        padding: 15px 10px;
        text-align: center;
        border: 1px solid #ddd;
        font-size: 12px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }
    .sev-ringan { border-top: 4px solid #FFCDD2; }
    .sev-sedang { border-top: 4px solid #E57373; }
    .sev-berat { border-top: 4px solid #B71C1C; background-color: #B71C1C; color: white; }

    /* Hasil Card */
    .result-card {
        background-color: white;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        border: 1px solid #eee;
    }
    .result-header {
        text-align: center;
        font-weight: 800;
        color: #333;
        font-size: 18px;
        margin-bottom: 15px;
        border-bottom: 2px solid #eee;
        padding-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# ================== STATE MANAGEMENT ==================
if "page" not in st.session_state:
    st.session_state.page = "Login"
if "gejala_terpilih" not in st.session_state:
    st.session_state.gejala_terpilih = []

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
    "S02": "Pemberian obat antifibrinolitik",
    "S03": "Edukasi pencegahan perdarahan berulang",
    "S04": "Profilaksis cedera fisik",
    "S05": "Terapi penggantian faktor pembekuan darah",
    "S06": "Fisioterapi rutin",
    "S07": "Monitoring medis berkala",
    "S08": "Pembatasan aktivitas fisik intensitas tinggi",
    "S09": "Terapi rutin konsentrat faktor VIII/IX",
    "S10": "Penanganan medis darurat segera",
    "S11": "Rehabilitasi fungsional",
    "S12": "Kontraindikasi penggunaan aspirin dan NSAID"
}

rules = [
    {"nama": "HEMOFILIA A - BERAT", "gejala": ["G01","G02","G04","G06","G07","G08","G09","G10","G12","G13","G14","G15"], "solusi": ["S09","S10","S11","S12"]},
    {"nama": "HEMOFILIA B - SEDANG", "gejala": ["G01","G02","G03","G04","G05","G06","G07","G08","G09","G10","G11","G15"], "solusi": ["S05","S06","S07","S08"]},
    {"nama": "HEMOFILIA C - RINGAN", "gejala": ["G01","G02","G03","G04","G05","G06","G09","G10","G11","G15"], "solusi": ["S01","S02","S03","S04"]}
]

# =======================================================
# ================== HALAMAN LOGIN ======================
# =======================================================
if st.session_state.page == "Login":
    st.markdown('<div class="mobile-container">', unsafe_allow_html=True)
    st.markdown('''
        <div class="glass-login">
            <div class="login-logo">🩸 SISTEM PAKAR<br>HEMOFILIA</div>
            <div class="login-welcome">Selamat Datang,<br><span style="font-size:12px; font-weight:normal;">Mulai penelusuran deteksi dini di sini.</span></div>
        </div>
    ''', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    username = st.text_input("Username", placeholder="Masukkan username", label_visibility="collapsed")
    password = st.text_input("Kata Sandi", type="password", placeholder="••••••••", label_visibility="collapsed")
    
    if st.button("Masuk"):
        if username == "admin" and password == "123":
            st.session_state.page = "Dashboard"
            st.rerun()
        else:
            st.error("Kredensial Salah!")
            
    st.markdown('''
        <div style="display:flex; justify-content:space-between; margin-top:15px; font-size:12px; color:white;">
            <span>Lupa Kata Sandi?</span>
            <span>Daftar Akun</span>
        </div>
    ''', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# =======================================================
# ================== HALAMAN DASHBOARD ==================
# =======================================================
elif st.session_state.page == "Dashboard":
    # Ubah background menjadi putih/abu terang
    st.markdown('<style>.stApp { background-image: none; background-color: #F4F6F9; }</style>', unsafe_allow_html=True)
    
    st.markdown('<div class="top-header-red">🩸 SISTEM PAKAR HEMOFILIA</div>', unsafe_allow_html=True)
    st.markdown('<div class="welcome-text">Welcome back, Pengguna! 👋</div>', unsafe_allow_html=True)
    
    # Card Main Button
    st.markdown('''
        <div style="background:white; border-radius:15px; padding:30px; text-align:center; box-shadow:0 4px 10px rgba(0,0,0,0.05); margin-bottom:15px;">
            <div style="font-size:40px; color:#D32F2F; margin-bottom:10px;">▶️</div>
            <h3 style="color:#333; margin:0;">Mulai Diagnosis</h3>
        </div>
    ''', unsafe_allow_html=True)
    if st.button("KLIK UNTUK MULAI DIAGNOSIS", key="btn_mulai"):
        st.session_state.page = "Diagnosis"
        st.rerun()

    # 3 Kolom Menu Bawah
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div style="background:white; border-radius:10px; padding:15px 5px; text-align:center; font-size:11px; font-weight:bold; box-shadow:0 2px 5px rgba(0,0,0,0.05);">🕘<br>Riwayat<br>Diagnosa</div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div style="background:white; border-radius:10px; padding:15px 5px; text-align:center; font-size:11px; font-weight:bold; box-shadow:0 2px 5px rgba(0,0,0,0.05);">ℹ️<br>Informasi<br>Tersedia</div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div style="background:white; border-radius:10px; padding:15px 5px; text-align:center; font-size:11px; font-weight:bold; box-shadow:0 2px 5px rgba(0,0,0,0.05);">📰<br>Berita<br>Terkini</div>', unsafe_allow_html=True)

    # Banner Bawah
    st.markdown('''
        <div class="health-banner">
            <h3 style="margin:0;">Panduan Hidup Sehat 🏃‍♀️</h3>
            <p style="font-size:12px; margin-top:5px; opacity:0.9;">Panduan gaya hidup sehat yang disarankan untuk penderita gangguan perdarahan.</p>
        </div>
    ''', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="btn-secondary">', unsafe_allow_html=True)
    if st.button("Keluar Akun"):
        st.session_state.page = "Login"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# =======================================================
# ================== HALAMAN DIAGNOSIS ==================
# =======================================================
elif st.session_state.page == "Diagnosis":
    st.markdown('<style>.stApp { background-image: none; background-color: #F4F6F9; }</style>', unsafe_allow_html=True)
    st.markdown('<div class="top-header-red">📋 PROSES DIAGNOSIS</div>', unsafe_allow_html=True)
    
    with st.form("form_diagnosis"):
        st.write("**Ceklis Gejala yang Dialami Pasien:**")
        st.markdown("<hr style='margin-top:0; margin-bottom:15px;'>", unsafe_allow_html=True)
        
        gejala_terpilih = []
        for kode, gejala in daftar_gejala.items():
            if st.checkbox(gejala, key=kode):
                gejala_terpilih.append(kode)

        st.markdown("<br><b>Opsi Pemilihan Tingkat Keparahan (Referensi):</b>", unsafe_allow_html=True)
        
        # Tampilan 3 Kartu Keparahan layaknya di gambar
        col_r, col_s, col_b = st.columns(3)
        with col_r:
            st.markdown('<div class="severity-card sev-ringan"><b>RINGAN</b><br><br>Lebam minimal, perdarahan sesekali</div>', unsafe_allow_html=True)
        with col_s:
            st.markdown('<div class="severity-card sev-sedang"><b>SEDANG</b><br><br>Lebam sedang, perdarahan sendi terkontrol</div>', unsafe_allow_html=True)
        with col_b:
            st.markdown('<div class="severity-card sev-berat"><b>BERAT</b><br><br>Perdarahan spontan, sering, nyeri berat</div>', unsafe_allow_html=True)
            
        st.markdown("<br>", unsafe_allow_html=True)
        
        submitted = st.form_submit_button("TERAPKAN PILIHAN & LIHAT HASIL")
        if submitted:
            st.session_state.gejala_terpilih = gejala_terpilih
            st.session_state.page = "Hasil"
            st.rerun()
            
    if st.button("Kembali"):
        st.session_state.page = "Dashboard"
        st.rerun()

# =======================================================
# ================== HALAMAN HASIL ======================
# =======================================================
elif st.session_state.page == "Hasil":
    st.markdown('<style>.stApp { background-image: none; background-color: #F4F6F9; }</style>', unsafe_allow_html=True)
    
    # Header Banner Image placeholder
    st.markdown('''
        <div style="background-image: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.7)), url('https://img.freepik.com/free-vector/red-blood-cells-background_1048-5221.jpg'); 
        background-size: cover; background-position: center; padding: 40px 20px; text-align: center; color: white; border-radius: 0 0 20px 20px; margin-top: -3rem; margin-bottom: 20px;">
            <h2 style="margin:0;">HASIL DIAGNOSIS</h2>
            <p style="font-size:12px; opacity:0.8; margin:0;">Berdasarkan Gejala yang Anda Ceklis</p>
        </div>
    ''', unsafe_allow_html=True)

    gejala_terpilih = st.session_state.gejala_terpilih

    if not gejala_terpilih:
        st.warning("Belum ada gejala yang dipilih.")
    else:
        hasil = None
        # Logika Pencocokan Aturan Sistem Pakar
        for r in rules:
            cocok = len([g for g in r["gejala"] if g in gejala_terpilih])
            if cocok >= len(r["gejala"]) * 0.5:
                hasil = r
                break

        if hasil:
            # Build HTML list untuk Gejala
            list_gejala_html = "".join([f"<li>✔️ {daftar_gejala[g]}</li>" for g in gejala_terpilih])
            # Build HTML list untuk Solusi
            list_solusi_html = "".join([f"<li>📌 <b>{daftar_solusi[s]}</b></li>" for s in hasil["solusi"]])

            st.markdown(f'''
            <div class="result-card">
                <div class="result-header">
                    DIAGNOSIS:<br>KEMUNGKINAN BESAR {hasil['nama']}
                </div>
                
                <p style="font-size:14px; font-weight:bold; margin-bottom:5px;">Gejala yang Dilaporkan:</p>
                <ul style="font-size:13px; color:#555; padding-left:15px; margin-top:0;">
                    {list_gejala_html}
                </ul>
                
                <p style="font-size:14px; font-weight:bold; margin-bottom:5px; margin-top:15px;">Solusi & Saran Lanjutan:</p>
                <ul style="font-size:13px; color:#555; padding-left:15px; margin-top:0;">
                    {list_solusi_html}
                </ul>
            </div>
            ''', unsafe_allow_html=True)
        else:
            st.error("Data gejala tidak cukup untuk menghasilkan diagnosis spesifik.")

    st.markdown("<br>", unsafe_allow_html=True)
    
    # Dua Tombol di bawah
    if st.button("CETAK HASIL"):
        st.success("Fungsi cetak PDF akan dijalankan.")
        
    if st.button("KEMBALI KE MENU UTAMA"):
        st.session_state.gejala_terpilih = []
        st.session_state.page = "Dashboard"
        st.rerun()
